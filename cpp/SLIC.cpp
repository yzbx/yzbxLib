#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/video/tracking.hpp"
#include <iostream>

//#include "../../../git/tracking/ustc_src/shrinkBGS/SLIC/image/ImageConcept.h"
#include "../../../git/tracking/ustc_src/shrinkBGS/SLIC/SLIC.h"
#include "../../../git/tracking/ustc_src/shrinkBGS/SLIC/Rgb2Lab.h"

using namespace cv;
using namespace std;

int main(int argc, char *argv[])
{
    Mat img=imread("lena.jpg");
//    img.resize(240,360);
    int img_rows=img.rows;
    int img_cols=img.cols;
    Size img_size=img.size();

    ImageSimpleUChar rImg,gImg,bImg;
    rImg.Create(img_rows,img_cols);
    gImg.Create(img_rows,img_cols);
    bImg.Create(img_rows,img_cols);

//    rImg.Create(img_cols,img_rows);
//    gImg.Create(img_cols,img_rows);
//    bImg.Create(img_cols,img_rows);
    cv::vector<Mat> mats;
    Mat input8UC3;
    input8UC3=img;
//    input32FC3.convertTo(input8UC3,CV_8UC3,255);
    split(input8UC3,mats);
    for(int i=0; i<img_rows; i++)
    {
        for(int j=0; j<img_cols; j++)
        {
            rImg.Pixel(i,j)=mats[0].at<uchar>(i,j);
            gImg.Pixel(i,j)=mats[1].at<uchar>(i,j);
            bImg.Pixel(i,j)=mats[2].at<uchar>(i,j);
//            rImg.Pixel(i,j)=mats[0].at<float>(j,i);
//            gImg.Pixel(i,j)=mats[1].at<float>(j,i);
//            bImg.Pixel(i,j)=mats[2].at<float>(j,i);
        }
    }

    imshow("R",mats[0]);
    imshow("G",mats[1]);
    imshow("RGB_B",mats[2]);

    ImageSimpleFloat LImg,AImg,BImg;
    LImg.Create(img_rows,img_cols);
    AImg.Create(img_rows,img_cols);
    BImg.Create(img_rows,img_cols);
//    LImg.Create(img_cols,img_rows);
//    AImg.Create(img_cols,img_rows);
//    BImg.Create(img_cols,img_rows);
//    Rgb2Lab(ImageSimpleUChar &rImg, ImageSimpleUChar &gImg, ImageSimpleUChar &bImg,\
//            ImageSimpleFloat &LImg, ImageSimpleFloat &AImg, ImageSimpleFloat &BImg);
    Rgb2Lab(rImg,gImg,bImg,LImg,AImg,BImg);

//    Mat LAB,LAB32FC3;
//    cvtColor(img,LAB,CV_RGB2Lab);
//    LAB.convertTo(LAB32FC3,CV_32FC3);
////     vector<Mat> mv;
//    mats.clear();
//    split(LAB32FC3,mats);
//    for(int i=0; i<img_rows; i++)
//    {
//        for(int j=0; j<img_cols; j++)
//        {
//            LImg.Pixel(i,j)=mats[0].at<float>(i,j);
//            AImg.Pixel(i,j)=mats[1].at<float>(i,j);
//            BImg.Pixel(i,j)=mats[2].at<float>(i,j);
////            rImg.Pixel(i,j)=mats[0].at<float>(j,i);
////            gImg.Pixel(i,j)=mats[1].at<float>(j,i);
////            bImg.Pixel(i,j)=mats[2].at<float>(j,i);
//        }
//    }

    ImageSimpleUInt idxImg;
    idxImg.Create(img_rows,img_cols);
    Run_SLIC_GivenPatchSize(LImg,AImg,BImg,25,20,idxImg);

    Mat cvLImg(img_size,CV_32F),cvAImg(img_size,CV_32F),cvBImg(img_size,CV_32F);
    cout<<idxImg.Width()<<" "<<img_rows<<endl;

    Mat cvIdxImg(img_size,CV_8U);
    for(int i=0; i<img_rows; i++)
    {
        for(int j=0; j<img_cols; j++)
        {
            cvIdxImg.at<uchar>(i,j)=(uchar)idxImg.Pixel(i,j);
            cvLImg.at<float>(i,j)=LImg.Pixel(i,j);
            cvAImg.at<float>(i,j)=AImg.Pixel(i,j);
            cvBImg.at<float>(i,j)=BImg.Pixel(i,j);
//            cvLImg.at<float>(i,j)=LImg.Pixel(j,i);
//            cvAImg.at<float>(i,j)=AImg.Pixel(j,i);
//            cvBImg.at<float>(i,j)=BImg.Pixel(j,i);
        }
    }

    imshow("L",cvLImg);
    imshow("A",cvAImg);
    imshow("LAB_B",cvBImg);

    int lowThreshold=3;
    int const max_lowThreshold = 100;
    int ratio = 3;
    int kernel_size = 3;

    Mat edges;
    Canny(cvIdxImg,edges,lowThreshold,lowThreshold*ratio,kernel_size);
    imshow("lena",img);
    imshow("cvIdxImg",cvIdxImg);

    Mat edges3d;
//     vector<Mat> mats;
    for(int i=0; i<3; i++)
    {
        mats[i]=edges;
    }
    merge(mats,edges3d);

    Mat imgEdges=img+edges3d;

//     add(img,Scalar(255,255,255),imgEdges,edges3d);
    imshow("edges",imgEdges);
    waitKey(0);

    return 0;
}




