function result=getResult(inputPath,groundTruthPath,roiTemporal)
    
    bin=[];
    gt=[];
    TP=0;TN=0;FP=0;FN=0;
    for frameNum=roiTemporal(1):roiTemporal(2)
        readFrame();
        accmulator(gt,bin);
        frameNum=frameNum+1;
    end
    P=TP/(TP+TN);
    R=TP/(TP+FN);
    
    if(TP==0)
        warning('TP==0');
        F=0;
    else
        F=2*P*R/(P+R);
    end

    fprintf('P=%f,R=%f,F=%f\n',P,R,F);
    
    
    function readFrame()
        bin=imread([inputPath,'\',num2str(frameNum,6),'.png']);
        gt=imread([groundTruthPath,'\gt',num2str(frameNum,6),'.png']);
        gt=gt>170;
    end

    function F=accumulator(imGT,imBinary)
        TP = TP+sum(sum(imGT==255&imBinary==1));		% True Positive 
        TN = TN+sum(sum(imGT<=50&imBinary==0));		% True Negative
        FP = FP+sum(sum((imGT<=50)&imBinary==1));	% False Positive
        FN = FN+sum(sum(imGT==255&imBinary==0));		% False Negative
    end
end
