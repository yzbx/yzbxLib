#!/bin/bash

for f in `ls ../*.png`
do
    echo $f
    target=`basename $f`
    convert $f -colorspace Gray gray_${target}
done
