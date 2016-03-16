win32 {

}
unix {
cvroot=/mnt/hgfs/D/git
bgsroot=$$cvroot/detection/bgslibrary

INCLUDEPATH+=$$bgsroot/package_bgs \
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
exists($$bgslib){
# LIBS +=$$bgslib \
#$ ls -l libbgs.so
#-rwxrwxrwx 1 root root 1043581 Mar 13 09:02 libbgs.so
#$ ls -l ../build/libbgs.so
#-rwxrwxrwx 1 root root 1350439 Mar 13 08:47 ../build/libbgs.so
#$ ls -l ../Debug/libbgs.so
#-rwxrwxrwx 1 root root 12847455 Mar 13 09:04 ../Debug/libbgs.so

	release {
		LIBS +=$$bgsroot/Release/libbgs.so
	}
	
	debug {
		LIBS +=$$bgsroot/Debug/libbgs.so
	}
}

!exists($$bgslib){
SOURCES +=$$bgsroot/package_bgs/AdaptiveBackgroundLearning.cpp \
$$bgsroot/package_bgs/AdaptiveSelectiveBackgroundLearning.cpp \
$$bgsroot/package_bgs/ae/KDE.cpp \
$$bgsroot/package_bgs/ae/KernelTable.cpp \
$$bgsroot/package_bgs/ae/NPBGmodel.cpp \
$$bgsroot/package_bgs/ae/NPBGSubtractor.cpp \
$$bgsroot/package_bgs/av/TBackground.cpp \
$$bgsroot/package_bgs/av/TBackgroundVuMeter.cpp \
$$bgsroot/package_bgs/av/VuMeter.cpp \
$$bgsroot/package_bgs/bl/sdLaMa091.cpp \
$$bgsroot/package_bgs/bl/SigmaDeltaBGS.cpp \
$$bgsroot/package_bgs/ck/graph.cpp \
$$bgsroot/package_bgs/ck/LbpMrf.cpp \
$$bgsroot/package_bgs/ck/maxflow.cpp \
$$bgsroot/package_bgs/ck/MEDefs.cpp \
$$bgsroot/package_bgs/ck/MEHistogram.cpp \
$$bgsroot/package_bgs/ck/MEImage.cpp \
$$bgsroot/package_bgs/ck/MotionDetection.cpp \
$$bgsroot/package_bgs/db/imbs.cpp \
$$bgsroot/package_bgs/db/IndependentMultimodalBGS.cpp \
$$bgsroot/package_bgs/dp/AdaptiveMedianBGS.cpp \
$$bgsroot/package_bgs/dp/DPAdaptiveMedianBGS.cpp \
$$bgsroot/package_bgs/dp/DPEigenbackgroundBGS.cpp \
$$bgsroot/package_bgs/dp/DPGrimsonGMMBGS.cpp \
$$bgsroot/package_bgs/dp/DPMeanBGS.cpp \
$$bgsroot/package_bgs/dp/DPPratiMediodBGS.cpp \
$$bgsroot/package_bgs/dp/DPTextureBGS.cpp \
$$bgsroot/package_bgs/dp/DPWrenGABGS.cpp \
$$bgsroot/package_bgs/dp/DPZivkovicAGMMBGS.cpp \
$$bgsroot/package_bgs/dp/Eigenbackground.cpp \
$$bgsroot/package_bgs/dp/Error.cpp \
$$bgsroot/package_bgs/dp/GrimsonGMM.cpp \
$$bgsroot/package_bgs/dp/Image.cpp \
$$bgsroot/package_bgs/dp/MeanBGS.cpp \
$$bgsroot/package_bgs/dp/PratiMediodBGS.cpp \
$$bgsroot/package_bgs/dp/TextureBGS.cpp \
$$bgsroot/package_bgs/dp/WrenGA.cpp \
$$bgsroot/package_bgs/dp/ZivkovicAGMM.cpp \
$$bgsroot/package_bgs/FrameDifferenceBGS.cpp \
$$bgsroot/package_bgs/GMG.cpp \
$$bgsroot/package_bgs/jmo/blob.cpp \
$$bgsroot/package_bgs/jmo/BlobExtraction.cpp \
$$bgsroot/package_bgs/jmo/BlobResult.cpp \
$$bgsroot/package_bgs/jmo/CMultiLayerBGS.cpp \
$$bgsroot/package_bgs/jmo/LocalBinaryPattern.cpp \
$$bgsroot/package_bgs/jmo/MultiLayerBGS.cpp \
$$bgsroot/package_bgs/lb/BGModel.cpp \
$$bgsroot/package_bgs/lb/BGModelFuzzyGauss.cpp \
$$bgsroot/package_bgs/lb/BGModelFuzzySom.cpp \
$$bgsroot/package_bgs/lb/BGModelGauss.cpp \
$$bgsroot/package_bgs/lb/BGModelMog.cpp \
$$bgsroot/package_bgs/lb/BGModelSom.cpp \
$$bgsroot/package_bgs/lb/LBAdaptiveSOM.cpp \
$$bgsroot/package_bgs/lb/LBFuzzyAdaptiveSOM.cpp \
$$bgsroot/package_bgs/lb/LBFuzzyGaussian.cpp \
$$bgsroot/package_bgs/lb/LBMixtureOfGaussians.cpp \
$$bgsroot/package_bgs/lb/LBSimpleGaussian.cpp \
$$bgsroot/package_bgs/MixtureOfGaussianV1BGS.cpp \
$$bgsroot/package_bgs/MixtureOfGaussianV2BGS.cpp \
$$bgsroot/package_bgs/my/MyBGS.cpp \
$$bgsroot/package_bgs/pl/BackgroundSubtractorLBSP.cpp \
$$bgsroot/package_bgs/pl/BackgroundSubtractorLOBSTER.cpp \
$$bgsroot/package_bgs/pl/BackgroundSubtractorSuBSENSE.cpp \
$$bgsroot/package_bgs/pl/LBSP.cpp \
$$bgsroot/package_bgs/pl/LOBSTER.cpp \
$$bgsroot/package_bgs/pl/SuBSENSE.cpp \
$$bgsroot/package_bgs/sjn/SJN_MultiCueBGS.cpp \
$$bgsroot/package_bgs/StaticFrameDifferenceBGS.cpp \
$$bgsroot/package_bgs/tb/FuzzyChoquetIntegral.cpp \
$$bgsroot/package_bgs/tb/FuzzySugenoIntegral.cpp \
$$bgsroot/package_bgs/tb/FuzzyUtils.cpp \
$$bgsroot/package_bgs/tb/MRF.cpp \
$$bgsroot/package_bgs/tb/PerformanceUtils.cpp \
$$bgsroot/package_bgs/tb/PixelUtils.cpp \
$$bgsroot/package_bgs/tb/T2FGMM.cpp \
$$bgsroot/package_bgs/tb/T2FGMM_UM.cpp \
$$bgsroot/package_bgs/tb/T2FGMM_UV.cpp \
$$bgsroot/package_bgs/tb/T2FMRF.cpp \
$$bgsroot/package_bgs/tb/T2FMRF_UM.cpp \
$$bgsroot/package_bgs/tb/T2FMRF_UV.cpp \
$$bgsroot/package_bgs/WeightedMovingMeanBGS.cpp \
$$bgsroot/package_bgs/WeightedMovingVarianceBGS.cpp \

}
}
