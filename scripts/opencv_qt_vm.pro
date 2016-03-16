win32 {
	
}
unix {
# opencv 2.4.8 without nonfree
	INCLUDEPATH+=/usr/include/opencv \
		/usr/include/opencv2 \
		/usr/include \

	cvLibRoot=/usr/lib/x86_64-linux-gnu

	LIBS += $$cvLibRoot/libopencv_videostab.so \
		$$cvLibRoot/libopencv_video.so \
		$$cvLibRoot/libopencv_ts.so \
		$$cvLibRoot/libopencv_superres.so \
		$$cvLibRoot/libopencv_stitching.so \
		$$cvLibRoot/libopencv_photo.so \
		$$cvLibRoot/libopencv_ocl.so \
		$$cvLibRoot/libopencv_objdetect.so \
		$$cvLibRoot/libopencv_ml.so \
		$$cvLibRoot/libopencv_legacy.so \
		$$cvLibRoot/libopencv_imgproc.so \
		$$cvLibRoot/libopencv_highgui.so \
		$$cvLibRoot/libopencv_gpu.so \
		$$cvLibRoot/libopencv_flann.so \
		$$cvLibRoot/libopencv_features2d.so \
		$$cvLibRoot/libopencv_core.so \
		$$cvLibRoot/libopencv_contrib.so \
		$$cvLibRoot/libopencv_calib3d.so \
                $$cvLibRoot/libopencv_nonfree.so
}
