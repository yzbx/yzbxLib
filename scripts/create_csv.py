# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os.path

# This is a tiny script to help you creating a CSV file from a face
# database with a similar hierarchie:
#
#  philipp@mango:~/facerec/data/at$ tree
#  .
#  |-- README
#  |-- s1
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  |-- s2
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  ...
#  |-- s40
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "usage: create_csv <base_path> [label.csv] [label.txt]"
        sys.exit(1)

    label_csv="label.csv"
    if len(sys.argv) > 2:
        label_csv=sys.argv[2]
    file_csv= open(label_csv, "w")

    label_txt="label.txt"
    if len(sys.argv) > 3:
        label_txt=sys.argv[3]
    file_txt=open(label_txt,"w")

    imgsuffix=('jpg','jpeg','pgm','png','bmp')
    BASE_PATH=sys.argv[1]
    SEPARATOR=";"

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                lowcase_filename=filename.lower()
                if lowcase_filename.endswith(imgsuffix):
                    abs_path = "%s/%s" % (subject_path, filename)
                    print "%s%s%d" % (abs_path, SEPARATOR, label)
                    file_csv.write("%s%s%d\n" % (abs_path, SEPARATOR, label))
            file_txt.write("%s%s%d\n" % (subdirname, SEPARATOR, label))
            label = label + 1

    file_csv.close()
    file_txt.close()