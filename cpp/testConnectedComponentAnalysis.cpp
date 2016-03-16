//  Connected Component Analysis/Labeling -- Test code  
//  Author:  www.icvpr.com    
//  Blog  :  http://blog.csdn.net/icvpr   
#include <iostream>  
#include <string>  
#include <list>  
#include <vector>  
#include <map>  
#include <stack>  
  
#include <opencv2/imgproc/imgproc.hpp>  
#include <opencv2/highgui/highgui.hpp>  
  
int main(int argc, char** argv)  
{  
    cv::Mat binImage = cv::imread("../icvpr.com.jpg", 0) ;  
    cv::threshold(binImage, binImage, 50, 1, CV_THRESH_BINARY_INV) ;  
  
    // connected component labeling  
    cv::Mat labelImg ;  
    icvprCcaByTwoPass(binImage, labelImg) ;  
    //icvprCcaBySeedFill(binImage, labelImg) ;  
  
    // show result  
    cv::Mat grayImg ;  
    labelImg *= 10 ;  
    labelImg.convertTo(grayImg, CV_8UC1) ;  
    cv::imshow("labelImg", grayImg) ;  
  
    cv::Mat colorLabelImg ;  
    icvprLabelColor(labelImg, colorLabelImg) ;  
    cv::imshow("colorImg", colorLabelImg) ;  
    cv::waitKey(0) ;  
  
    return 0 ;  
}