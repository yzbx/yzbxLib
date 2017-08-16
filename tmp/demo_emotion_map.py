import os,sys
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Circle
# Get an example image
import matplotlib.cbook as cbook
import imageio
import cv2
import skimage
from skimage.viewer import ImageViewer

minutes=100
y_emotion=[]
y_ticks=['anger','happy','sad','surprise','disgust','fear','neutral']
emotions_num=len(y_ticks)
emotions_distribution=[0.1,0.1,0.1,0.1,0.1,0.1,0.4]

def draw_line_image():
    x_time=range(minutes)
    y_emotion=np.random.choice(np.arange(emotions_num),size=minutes,p=emotions_distribution).tolist()

    f1=plt.figure()
    plt.yticks(range(emotions_num),y_ticks)
    plt.plot(x_time,y_emotion)
    plt.title('emotion line')
    f1.draw

def draw_map_image(x,y):
    f2,ax=plt.subplots()
    image_file = cbook.get_sample_data('/mnt/hgfs/I/ComputerVision/ISCAS/housemap001.jpg')
    img = plt.imread(image_file)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #img=img[:,:,0]
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title('emotion map')

    # Show the image
    plt.imshow(img)

    # matplotColors=['blue','green','red','cyan','magenta','yellow','black','white']
    colors = ['red', 'blue', 'yellow', 'green', 'cyan', 'black', 'magenta']
    assert len(colors) == emotions_num
    # Now, loop through coord arrays, and create a circle at each x,y pair
    for xx,yy in zip(x,y):
        emotion = np.random.choice(np.arange(emotions_num), p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4])
        p = Circle((xx, yy), 5, color=colors[emotion])
        ax.add_patch(p)

    # draw legend
    patches=[]
    for color,label in zip(colors,y_ticks):
        patch=Circle(color=color,label=label,xy=(5,5))
        patches.append(patch)

    plt.legend(handles=patches)

    #f2.draw
    #f2.canvas.draw()
    return f2


def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return data

if __name__ == '__main__':
    plt.ion()
    draw_line_image()
    plt.savefig('emotion_line.png')
    plt.close()

    image_file = cbook.get_sample_data('/mnt/hgfs/I/ComputerVision/ISCAS/housemap001.jpg')
    img = plt.imread(image_file)
    #img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # Make some example data
    x = np.random.rand(100)*img.shape[1]
    y = np.random.rand(100)*img.shape[0]

    writer = imageio.get_writer('emotion_map.mp4', fps=1)
    #x=[65,124,161,140]
    #y=[85,102,132,64]
    #x=x[0:3]
    #y=y[0:3]
    for frameNum in range(300):
        x = np.random.rand(100) * img.shape[1]
        y = np.random.rand(100) * img.shape[0]

        f2=draw_map_image(x,y)
        f2_img=fig2data(f2)

        #viewer=ImageViewer(f2_img)
        #viewer.show()
        writer.append_data(f2_img)
        plt.pause(0.5)

        if frameNum != 9:
            plt.close()

    writer.close()
    plt.ioff()
    plt.show()