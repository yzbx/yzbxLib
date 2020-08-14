# -*- coding: utf-8 -*-
import os
import glob
import zipfile

def zip_files(dir_path, zip_path):
    """
    :param dir_path: 需要压缩的文件目录
    :param zip_path: 压缩后的目录
    :return:
    """
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as f:
        for root, _, file_names in os.walk(dir_path):
            for filename in file_names:
                f.write(os.path.join(root, filename), filename)
                
if __name__ == '__main__':
    zip_files(os.path.expanduser('~/git/sketch/pytorch-gan/data/demo/A'),'/tmp/test.zip')