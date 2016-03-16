// take number image type number (from cv::Mat.type()), get OpenCV's enum string.
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;
string getImgType(int imgTypeInt)
{
    int numImgTypes = 35; // 7 base types, with five channel options each (none or C1, ..., C4)

    int enum_ints[] =       {CV_8U,  CV_8UC1,  CV_8UC2,  CV_8UC3,  CV_8UC4,
                             CV_8S,  CV_8SC1,  CV_8SC2,  CV_8SC3,  CV_8SC4,
                             CV_16U, CV_16UC1, CV_16UC2, CV_16UC3, CV_16UC4,
                             CV_16S, CV_16SC1, CV_16SC2, CV_16SC3, CV_16SC4,
                             CV_32S, CV_32SC1, CV_32SC2, CV_32SC3, CV_32SC4,
                             CV_32F, CV_32FC1, CV_32FC2, CV_32FC3, CV_32FC4,
                             CV_64F, CV_64FC1, CV_64FC2, CV_64FC3, CV_64FC4};

    string enum_strings[] = {"CV_8U",  "CV_8UC1",  "CV_8UC2",  "CV_8UC3",  "CV_8UC4",
                             "CV_8S",  "CV_8SC1",  "CV_8SC2",  "CV_8SC3",  "CV_8SC4",
                             "CV_16U", "CV_16UC1", "CV_16UC2", "CV_16UC3", "CV_16UC4",
                             "CV_16S", "CV_16SC1", "CV_16SC2", "CV_16SC3", "CV_16SC4",
                             "CV_32S", "CV_32SC1", "CV_32SC2", "CV_32SC3", "CV_32SC4",
                             "CV_32F", "CV_32FC1", "CV_32FC2", "CV_32FC3", "CV_32FC4",
                             "CV_64F", "CV_64FC1", "CV_64FC2", "CV_64FC3", "CV_64FC4"};

    for(int i=0; i<numImgTypes; i++)
    {
        if(imgTypeInt == enum_ints[i]) return enum_strings[i];
    }
    return "unknown image type";
}

std::string getImageType(int number)
{
    // find type
    int imgTypeInt = number%8;
    std::string imgTypeString;

    switch (imgTypeInt)
    {
        case 0:
            imgTypeString = "8U";
            break;
        case 1:
            imgTypeString = "8S";
            break;
        case 2:
            imgTypeString = "16U";
            break;
        case 3:
            imgTypeString = "16S";
            break;
        case 4:
            imgTypeString = "32S";
            break;
        case 5:
            imgTypeString = "32F";
            break;
        case 6:
            imgTypeString = "64F";
            break;
        default:
            break;
    }

    // find channel
    int channel = (number/8) + 1;

    std::stringstream type;
    type<<"CV_"<<imgTypeString<<"C"<<channel;

    return type.str();
}

//  Connected Component Analysis/Labeling By Two-Pass Algorithm   
//  Author:  www.icvpr.com    
//  Blog  :  http://blog.csdn.net/icvpr   
//  http://blog.csdn.net/augusdi/article/details/9008921
#include <iostream>  
#include <string>  
#include <list>  
#include <vector>  
#include <map>  
  
#include <opencv2/imgproc/imgproc.hpp>  
#include <opencv2/highgui/highgui.hpp>  
  
  
void icvprCcaByTwoPass(const cv::Mat& _binImg, cv::Mat& _lableImg)  
{  
    // connected component analysis (4-component)  
    // use two-pass algorithm  
    // 1. first pass: label each foreground pixel with a label  
    // 2. second pass: visit each labeled pixel and merge neighbor labels  
    //   
    // foreground pixel: _binImg(x,y) = 1  
    // background pixel: _binImg(x,y) = 0  
  
  
    if (_binImg.empty() ||  
        _binImg.type() != CV_8UC1)  
    {  
        return ;  
    }  
  
    // 1. first pass  
  
    _lableImg.release() ;  
    _binImg.convertTo(_lableImg, CV_32SC1) ;  
  
    int label = 1 ;  // start by 2  
    std::vector<int> labelSet ;  
    labelSet.push_back(0) ;   // background: 0  
    labelSet.push_back(1) ;   // foreground: 1  
  
    int rows = _binImg.rows - 1 ;  
    int cols = _binImg.cols - 1 ;  
    for (int i = 1; i < rows; i++)  
    {  
        int* data_preRow = _lableImg.ptr<int>(i-1) ;  
        int* data_curRow = _lableImg.ptr<int>(i) ;  
        for (int j = 1; j < cols; j++)  
        {  
            if (data_curRow[j] == 1)  
            {  
                std::vector<int> neighborLabels ;  
                neighborLabels.reserve(2) ;  
                int leftPixel = data_curRow[j-1] ;  
                int upPixel = data_preRow[j] ;  
                if ( leftPixel > 1)  
                {  
                    neighborLabels.push_back(leftPixel) ;  
                }  
                if (upPixel > 1)  
                {  
                    neighborLabels.push_back(upPixel) ;  
                }  
  
                if (neighborLabels.empty())  
                {  
                    labelSet.push_back(++label) ;  // assign to a new label  
                    data_curRow[j] = label ;  
                    labelSet[label] = label ;  
                }  
                else  
                {  
                    std::sort(neighborLabels.begin(), neighborLabels.end()) ;  
                    int smallestLabel = neighborLabels[0] ;    
                    data_curRow[j] = smallestLabel ;  
  
                    // save equivalence  
                    for (size_t k = 1; k < neighborLabels.size(); k++)  
                    {  
                        int tempLabel = neighborLabels[k] ;  
                        int& oldSmallestLabel = labelSet[tempLabel] ;  
                        if (oldSmallestLabel > smallestLabel)  
                        {                             
                            labelSet[oldSmallestLabel] = smallestLabel ;  
                            oldSmallestLabel = smallestLabel ;  
                        }                         
                        else if (oldSmallestLabel < smallestLabel)  
                        {  
                            labelSet[smallestLabel] = oldSmallestLabel ;  
                        }  
                    }  
                }                 
            }  
        }  
    }  
  
    // update equivalent labels  
    // assigned with the smallest label in each equivalent label set  
    for (size_t i = 2; i < labelSet.size(); i++)  
    {  
        int curLabel = labelSet[i] ;  
        int preLabel = labelSet[curLabel] ;  
        while (preLabel != curLabel)  
        {  
            curLabel = preLabel ;  
            preLabel = labelSet[preLabel] ;  
        }  
        labelSet[i] = curLabel ;  
    }  
  
  
    // 2. second pass  
    for (int i = 0; i < rows; i++)  
    {  
        int* data = _lableImg.ptr<int>(i) ;  
        for (int j = 0; j < cols; j++)  
        {  
            int& pixelLabel = data[j] ;  
            pixelLabel = labelSet[pixelLabel] ;   
        }  
    }  
}

//  Connected Component Analysis/Labeling By Seed-Filling Algorithm   
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
  
  
void icvprCcaBySeedFill(const cv::Mat& _binImg, cv::Mat& _lableImg)  
{  
    // connected component analysis (4-component)  
    // use seed filling algorithm  
    // 1. begin with a foreground pixel and push its foreground neighbors into a stack;  
    // 2. pop the top pixel on the stack and label it with the same label until the stack is empty  
    //   
    // foreground pixel: _binImg(x,y) = 1  
    // background pixel: _binImg(x,y) = 0  
  
  
    if (_binImg.empty() ||  
        _binImg.type() != CV_8UC1)  
    {  
        return ;  
    }  
  
    _lableImg.release() ;  
    _binImg.convertTo(_lableImg, CV_32SC1) ;  
  
    int label = 1 ;  // start by 2  
  
    int rows = _binImg.rows - 1 ;  
    int cols = _binImg.cols - 1 ;  
    for (int i = 1; i < rows-1; i++)  
    {  
        int* data= _lableImg.ptr<int>(i) ;  
        for (int j = 1; j < cols-1; j++)  
        {  
            if (data[j] == 1)  
            {  
                std::stack<std::pair<int,int>> neighborPixels ;     
                neighborPixels.push(std::pair<int,int>(i,j)) ;     // pixel position: <i,j>  
                ++label ;  // begin with a new label  
                while (!neighborPixels.empty())  
                {  
                    // get the top pixel on the stack and label it with the same label  
                    std::pair<int,int> curPixel = neighborPixels.top() ;  
                    int curX = curPixel.first ;  
                    int curY = curPixel.second ;  
                    _lableImg.at<int>(curX, curY) = label ;  
  
                    // pop the top pixel  
                    neighborPixels.pop() ;  
  
                    // push the 4-neighbors (foreground pixels)  
                    if (_lableImg.at<int>(curX, curY-1) == 1)  
                    {// left pixel  
                        neighborPixels.push(std::pair<int,int>(curX, curY-1)) ;  
                    }  
                    if (_lableImg.at<int>(curX, curY+1) == 1)  
                    {// right pixel  
                        neighborPixels.push(std::pair<int,int>(curX, curY+1)) ;  
                    }  
                    if (_lableImg.at<int>(curX-1, curY) == 1)  
                    {// up pixel  
                        neighborPixels.push(std::pair<int,int>(curX-1, curY)) ;  
                    }  
                    if (_lableImg.at<int>(curX+1, curY) == 1)  
                    {// down pixel  
                        neighborPixels.push(std::pair<int,int>(curX+1, curY)) ;  
                    }  
                }         
            }  
        }  
    }  
}

//  Connected Component Analysis/Labeling -- Color Labeling   
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
  
cv::Scalar icvprGetRandomColor()  
{  
    uchar r = 255 * (rand()/(1.0 + RAND_MAX));  
    uchar g = 255 * (rand()/(1.0 + RAND_MAX));  
    uchar b = 255 * (rand()/(1.0 + RAND_MAX));  
    return cv::Scalar(b,g,r) ;  
}  
  
  
void icvprLabelColor(const cv::Mat& _labelImg, cv::Mat& _colorLabelImg)   
{  
    if (_labelImg.empty() ||  
        _labelImg.type() != CV_32SC1)  
    {  
        return ;  
    }  
  
    std::map<int, cv::Scalar> colors ;  
  
    int rows = _labelImg.rows ;  
    int cols = _labelImg.cols ;  
  
    _colorLabelImg.release() ;  
    _colorLabelImg.create(rows, cols, CV_8UC3) ;  
    _colorLabelImg = cv::Scalar::all(0) ;  
  
    for (int i = 0; i < rows; i++)  
    {  
        const int* data_src = (int*)_labelImg.ptr<int>(i) ;  
        uchar* data_dst = _colorLabelImg.ptr<uchar>(i) ;  
        for (int j = 0; j < cols; j++)  
        {  
            int pixelValue = data_src[j] ;  
            if (pixelValue > 1)  
            {  
                if (colors.count(pixelValue) <= 0)  
                {  
                    colors[pixelValue] = icvprGetRandomColor() ;  
                }  
                cv::Scalar color = colors[pixelValue] ;  
                *data_dst++   = color[0] ;  
                *data_dst++ = color[1] ;  
                *data_dst++ = color[2] ;  
            }  
            else  
            {  
                data_dst++ ;  
                data_dst++ ;  
                data_dst++ ;  
            }  
        }  
    }  
}  

