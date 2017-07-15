# failed!!! wait to implement more!!!
import execnet

def call_python_version(Version, Module, Function, ArgumentList):
    gw = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        import numpy as np
        from %s import %s as the_function
        dict=*channel.receive()
        image=np.asarray(dict['image']).reshape(dict['shape'])
        channel.send(the_function(image))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

# config
gnu_code_path = '/home/yzbx/git/gnu/face_classification'

class FaceDetection:
    def __init__(self,srccode="opencv"):
        if srccode not in ["opencv","dlib"]:
            self.srccode = "opencv"
        self.srccode=srccode
        detection_model_path = os.path.join(gnu_code_path,
                                            'trained_models/detection_models/haarcascade_frontalface_default.xml')
        self.opencv_face_detection = cv2.CascadeClassifier(detection_model_path)

    def process(self,image):
        if self.srccode=="opencv":
            if len(image.shape)==2:
                gray=image
            else:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.opencv_face_detection.detectMultiScale(gray, 1.3, 5)
        elif self.srccode=="dlib":
            # to avoid package conflict
            # from face_recognition import face_locations
            # face_locations = face_locations(image)
            imageList=image.tolist()
            shape=image.shape
            dict={"image":imageList,"shape":shape}
            face_locations=call_python_version("3","face_recognition","face_locations",dict)
            faces=[]
            for (t,r,b,l) in face_locations:
                faces.append((t,l,r-l,b-t))
        #todo elif self.srccode=='facenet':
        else:
            print('undefine srccode %s'%self.srccode)
            faces=[]
        return faces
