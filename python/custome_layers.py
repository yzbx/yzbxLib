# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""
use the code from:
https://github.com/bonlime/keras-deeplab-v3-plus/blob/master/model.py
"""

from keras.engine import Layer
from keras.engine import InputSpec
from keras.utils import conv_utils
from keras import backend as K
from keras import layers as KL

class BilinearUpsampling(Layer):
    """Just a simple bilinear upsampling layer. Works only with TF.
       Args:
           upsampling: tuple of 2 numbers > 0. The upsampling ratio for h and w
           output_size: used instead of upsampling arg if passed!
    """

    def __init__(self, upsampling=(2, 2), output_size=None, data_format=None, **kwargs):

        super(BilinearUpsampling, self).__init__(**kwargs)

        self.data_format = conv_utils.normalize_data_format(data_format)
        self.input_spec = InputSpec(ndim=4)
        if output_size:
            self.output_size = conv_utils.normalize_tuple(
                output_size, 2, 'output_size')
            self.upsampling = None
        else:
            self.output_size = None
            self.upsampling = conv_utils.normalize_tuple(
                upsampling, 2, 'upsampling')

    def compute_output_shape(self, input_shape):
        if self.upsampling:
            height = self.upsampling[0] * \
                input_shape[1] if input_shape[1] is not None else None
            width = self.upsampling[1] * \
                input_shape[2] if input_shape[2] is not None else None
        else:
            height = self.output_size[0]
            width = self.output_size[1]
        return (input_shape[0],
                height,
                width,
                input_shape[3])

    def call(self, inputs):
        if self.upsampling:
            return K.tf.image.resize_bilinear(inputs, (inputs.shape[1] * self.upsampling[0],
                                                       inputs.shape[2] * self.upsampling[1]),
                                              align_corners=True)
        else:
            return K.tf.image.resize_bilinear(inputs, (self.output_size[0],
                                                       self.output_size[1]),
                                              align_corners=True)

    def get_config(self):
        config = {'upsampling': self.upsampling,
                  'output_size': self.output_size,
                  'data_format': self.data_format}
        base_config = super(BilinearUpsampling, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

def relu6(x):
    return K.relu(x, max_value=6)

def duc(x, factor=8, output_shape=(224, 224, 1),name=None):
    if K.image_data_format() == 'channels_last':
        bn_axis = -1
    else:
        bn_axis = 1
        
    if name is None:
        name='duc_%s'%factor
    H, W, c, r = output_shape[0], output_shape[1], output_shape[2], factor
    h = H // r
    w = W // r
    x = KL.Conv2D(
            c*r*r,
            (3, 3),
            padding='same',
            name='conv_%s'%name)(x)
    x = KL.BatchNormalization(axis=bn_axis,name='bn_%s'%name)(x)
    x = KL.Activation('relu')(x)
    x = KL.Permute((3, 1, 2))(x)
    x = KL.Reshape((c, r, r, h, w))(x)
    x = KL.Permute((1, 4, 2, 5, 3))(x)
    x = KL.Reshape((c, H, W))(x)
    x = KL.Permute((2, 3, 1))(x)

    return x