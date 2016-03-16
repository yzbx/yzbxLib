function Analyse_PixelValue()
%%% analyse the pixelValue-frameNum scatter figure at point of roi.
%%% point: [100,100]
%%% roi: [0,7000];

% root='D:\firefoxDownload\matlab\dataset2012\dataset\shadow\bungalows';
% root='D:\firefoxDownload\matlab\dataset2012\dataset\dynamicBackground\fall';
% root='D:\firefoxDownload\matlab\dataset2012\dataset\dynamicBackground\boats';
close all

root='/media/yzbx/D/firefoxDownload/matlab/dataset2012/dataset/dynamicBackground/boats';
roi=[6900,7500];
% point=[80,190];
point=[150,150];
show(roi,point);

% img=imread([groundTruthPath,'\',filelist{frameNum+2}]);
    function frame=getFrame(filepath,filelist,frameNum)
        frame=imread([filepath,'/',filelist{frameNum+2}]);
    end

    function show(roi,point)
        
        groundTruthPath=[root,'/groundtruth'];
        infolist=dir(groundTruthPath);
        filelist={infolist.name};
        
        inputPath=[root,'/input'];
        infolist=dir(inputPath);
        inputlist={infolist.name};
        
        
        frameNum=roi(1);
        
        a=point(1);
        b=point(2);
        
        
        %             shadow=[];
        ground=zeros(roi(2)-roi(1),3);
        label=zeros(roi(2)-roi(1),1);

        while frameNum<=roi(2)
            groundTruth=getFrame(groundTruthPath,filelist,frameNum);
            input=getFrame(inputPath,inputlist,frameNum);
            input=rgb2lab(input);
            if(frameNum==roi(1))
                inputSample=input;
                groundTruthSample=groundTruth;
            end
            
            frameNum=frameNum+1;
            %                 inputLBP=getLBP(input,a,b);

            info=input(a,b,:);
            for i=1:3
                ground(frameNum-roi(1),i)=info(i);
            end
            
            label(frameNum-roi(1))=0;
            %                 display(info);
            if(groundTruth(a,b)==255)
                label(frameNum-roi(1))=1;
            end
            subplot(231),imshow(lableImg(groundTruth,a,b)),title('groundTruth');
            subplot(232),imshow(lableImg(input,a,b)),title('input');
            subplot(233),scatter(1:length(label),ground(:,1),3,label,'filled');
            subplot(234),scatter(1:length(label),ground(:,2),3,label,'filled');
            subplot(235),scatter(1:length(label),ground(:,3),3,label,'filled');
            
            pause(0.1);
        end
       
%         h=figure;
        subplot(221),imshow(lableImg(groundTruthSample,a,b)),title('groundTruth');
        subplot(222),imshow(lableImg(inputSample,a,b)),title('input');
        subplot(223),scatter(1:length(label),ground(:,1),3,label,'filled');
%         saveas(h,['localWave-',int2str(i),'-',int2str(a),'-',int2str(b)],'bmp');
    end

    function img=lableImg(img,a,b)
        %         lable the sample position in img
        [m,n,c]=size(img);
        if(c==1)
            g1=im2double(img);
            %           g1(img)=1;
            img=cat(3,g1,g1,g1);
        else
            img=im2double(img);
        end
        
        color=[1,0,0];
        for i=a-5:a+5
            for j=b-5:b+5
                if(i>=1&&j>=1&&i<=m&&j<=n)
                    img(i,j,:)=color(:);
                end
            end
        end
        
    end

end