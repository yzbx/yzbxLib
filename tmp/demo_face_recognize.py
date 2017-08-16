import face_recognition
import cv2
import sys, os
import imageio
import matplotlib.pyplot as plt
import numpy as np


suffix = ('jpg', 'jpeg', 'bmp', 'png')
img_suffix = []
for s in suffix:
    img_suffix.append(s)
    img_suffix.append(s.upper())

img_suffix = tuple(img_suffix)

class Face_Search_Class:
    def __init__(self, imgpath):
        filelist = os.listdir(imgpath)

        self.face_names = []
        self.face_encodings = []
        for f in filelist:
            img = os.path.join(imgpath, f)
            if img.endswith(img_suffix) and os.path.isfile(img):
                image = face_recognition.load_image_file(img)

                if image is None:
                    print('image is None for file ',img)
                    continue

                face_encodings = face_recognition.face_encodings(image)[0]
                self.face_encodings.append(face_encodings)
                face_name = os.path.splitext(f)[0]
                self.face_names.append(face_name)

    def process(self, image_search_path, show=True):
        shrink_scale = 2.0
        image_search = cv2.imread(image_search_path)
        image = cv2.resize(image_search, (0, 0), fx=1.0 / shrink_scale, fy=1.0 / shrink_scale)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 0:
            print('cannot find face in image', image_search_path)
            return None

        face_encodings = face_recognition.face_encodings(image, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(self.face_encodings, face_encoding)
            name = "Unknown"

            print(match.__class__)
            for idx in range(len(match)):
                if match[idx]:
                    name = self.face_names[idx]
            face_names.append(name)

        face_infos = []
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= shrink_scale
            right *= shrink_scale
            bottom *= shrink_scale
            left *= shrink_scale

            locations = {'top': int(top), 'right': int(right), 'bottom': int(bottom), 'left': int(left)}
            face_name = {'name': name}

            face_info = {'location': locations, 'name': face_name}
            face_infos.append(face_info)

            left=int(left)
            top=int(top)
            right=int(right)
            bottom=int(bottom)
            # Draw a box around the face
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            text_org=(left+6,min(bottom-6,0))

            print('type(image)',type(image))
            print('type(name)',type(name),name)
            print('type(text_org)',type(text_org))
            print('type(font)',type(font))
            cv2.putText(img=image, text=name, org=text_org, fontFace=font, fontScale=1.0, color=(255, 255, 255), thickness=1)

        return_data = {'image_path': image_search_path, 'face_infos': face_infos, 'labeled_image':image}
        print(return_data)

        if show:
            #cv2.imshow('labeled image',image)
            #cv2.waitKey(0)
            #img = mpimg.imread('stinkbug.png')
            imgplot = plt.imshow(image)
            plt.show()

        return return_data


if __name__ == '__main__':
    fsc=Face_Search_Class('data/train')
    for f in os.listdir('data/test'):
        image_search_path=os.path.join('data/test',f)
        if os.path.isfile(image_search_path) and f.endswith(img_suffix):
            fsc.process(image_search_path)
