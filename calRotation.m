function [potRef,vecMove,thetaX,thetaY,thetaZ]=calRotation(points1,points2)
    p1=points1(1,:)';
    p2=points1(2,:)';
    p3=points1(3,:)';

    p1_=points2(1,:)';
    p2_=points2(2,:)';
    p3_=points2(3,:)';

    v1=cross(p1-p2,p1-p3);
    v2=cross(p1_-p2_,p1_-p3_);

    v1n=v1/norm(v1);
    v2n=v2/norm(v2);

    refOffset=0.5*dist(p1',p2);
    p1Ref=p1+v1n*refOffset;
    p2Ref=p1_+v2n*refOffset;
    potRef=p1Ref;

    vecMove=p2Ref-p1Ref;
    points1=points1+vecMove';

    rotateMat=calRotateMatrix(points1,points2,p2Ref);
    thetaZYX=rotm2eul(rotateMat,'ZYX')/pi*180;

    thetaX=thetaZYX(3);
    thetaY=thetaZYX(2);
    thetaZ=thetaZYX(1);
end



function rotateMatrix=calRotateMatrix(points1,points2,rotateOri)
    deltaLoc=[0;0;0];

    matLoc=zeros(size(points2,1),size(deltaLoc,1));
    matOri=zeros(size(points2,1),size(deltaLoc,1));
    for i=1:size(matLoc,1)
        matLoc(i,:)=deltaLoc';
        matOri(i,:)=rotateOri';
    end

    points1=points1-matOri;
    points2=points2-matOri;

    points2=points2-matLoc;
    points2=points2';
    points1=points1';

    rotateMatrix=points2*pinv(points1);

end
