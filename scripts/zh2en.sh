#!/bin/bash

mv ~/下载 ~/Downloads
mv ~/文档 ~/Documents
mv ~/图片 ~/Pictures
mv ~/桌面 ~/Desktop
mv ~/视频 ~/Videos
mv ~/音乐 ~/Music
ln -s ~/Downloads ~/下载 
ln -s ~/Documents ~/文档 
ln -s ~/Pictures ~/图片 
ln -s ~/Desktop ~/桌面 
ln -s ~/Videos ~/视频 
ln -s ~/Music ~/音乐 

mv 模板 Templates && ln -s Templates 模板
mv 公共的 Public && ln -s Public 公共的

