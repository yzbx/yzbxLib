win32 {
message (bgslibrary error: windows support need!!!)
}
unix {
message (bgslibrary: unix support okay!!!)
bgsroot=/home/yzbx/git/bgslibrary

INCLUDEPATH+=$$bgsroot \
$$bgsroot/package_bgs \
$$bgsroot/package_bgs/ae \
$$bgsroot/package_bgs/av \
$$bgsroot/package_bgs/bl \
$$bgsroot/package_bgs/ck \
$$bgsroot/package_bgs/db \
$$bgsroot/package_bgs/dp \
$$bgsroot/package_bgs/jmo \
$$bgsroot/package_bgs/lb \
$$bgsroot/package_bgs/my \
$$bgsroot/package_bgs/pl \
$$bgsroot/package_bgs/sjn \
$$bgsroot/package_bgs/tb \

bgslib=$$bgsroot/build/libbgs.so
#LIBS +=$$bgsroot/debug/libbgs.so
LIBS +=$$bgslib
message (find libbgs.so)
}
