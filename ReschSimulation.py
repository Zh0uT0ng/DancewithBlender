import bpy
import bmesh
import math
import numpy as np

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

motionList=np.loadtxt('/Users/zhoutong/Desktop/motionList.csv',delimiter=",")
potRefLIST=np.loadtxt('/Users/zhoutong/Desktop/potRefLIST.csv',delimiter=",")
thetaLIST=np.loadtxt('/Users/zhoutong/Desktop/thetaLIST.csv',delimiter=",")
vecMoveLIST=np.loadtxt('/Users/zhoutong/Desktop/vecMoveLIST.csv',delimiter=",")

def drawPlane(name,p1,p2,p3):
    
    bpy.ops.mesh.primitive_plane_add(size=1,location=(0,0,0))
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.mesh.select_mode(type = "VERT")
    
    # select randomly two points
    bm = bmesh.from_edit_mesh(bpy.context.object.data)
    bm.verts.ensure_lookup_table()
    bm.verts[0].select = True # [0~N]按照某种方式排列
    bm.verts[1].select = True # [0~N]按照某种方式排列
    
    bpy.ops.mesh.merge(type='CENTER')
    bpy.ops.mesh.select_all(action="DESELECT")
    
    # frame data
    bm.verts.ensure_lookup_table()
    bm.verts[0].co=p1
    bm.verts[1].co=p2
    bm.verts[2].co=p3
    
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.context.object.name = name

    bpy.ops.object.select_all(action='DESELECT')


# define the planes
topoPlane=[[1,2,3],[1,4,5],[2,6,7],[3,8,9],
           [1,2,10],[1,5,10],[2,6,10],
           [2,3,11],[2,7,11],[3,9,11],
           [1,3,12],[3,8,12],[1,4,12]]

point0=motionList[0]


# draw the bodies
for j in range(len(topoPlane)):
    topoj=topoPlane[j]
    
    pA=point0[3*(topoj[0]-1):3*topoj[0]]
    pB=point0[3*(topoj[1]-1):3*topoj[1]]
    pC=point0[3*(topoj[2]-1):3*topoj[2]]

    name='body'+str(j)
    
    drawPlane(name,pA,pB,pC)

obj_0 = bpy.data.objects['body0'] 
obj_1 = bpy.data.objects['body1'] 
obj_2 = bpy.data.objects['body2'] 
obj_3 = bpy.data.objects['body3'] 
obj_4 = bpy.data.objects['body4'] 
obj_5 = bpy.data.objects['body5']
obj_6 = bpy.data.objects['body6'] 
obj_7 = bpy.data.objects['body7'] 
obj_8 = bpy.data.objects['body8'] 
obj_9 = bpy.data.objects['body9'] 
obj_10= bpy.data.objects['body10'] 
obj_11= bpy.data.objects['body11'] 
obj_12= bpy.data.objects['body12'] 


## initial the first frame
frame_number=0
bpy.context.scene.frame_set(frame_number)
# change the rotation center of the bodies
rotateCenter0=potRefLIST[0]

rc0=rotateCenter0[0:3]
rc1=rotateCenter0[3:6]
rc2=rotateCenter0[6:9]
rc3=rotateCenter0[9:12]
rc4=rotateCenter0[12:15]
rc5=rotateCenter0[15:18]
rc6=rotateCenter0[18:21]
rc7=rotateCenter0[21:24]
rc8=rotateCenter0[24:27]
rc9=rotateCenter0[27:30]
rc10=rotateCenter0[30:33]
rc11=rotateCenter0[33:36]
rc12=rotateCenter0[36:39]
    
bpy.context.scene.cursor.location =(rc0[0],rc0[1],rc0[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_0.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_0.location = (rc0[0],rc0[1],rc0[2])
obj_0.keyframe_insert(data_path = "location",index = -1)
obj_0.rotation_euler =(0,0,0)
obj_0.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc1[0],rc1[1],rc1[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_1.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_1.location = (rc1[0],rc1[1],rc1[2])
obj_1.keyframe_insert(data_path = "location",index = -1)
obj_1.rotation_euler =(0,0,0)
obj_1.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc2[0],rc2[1],rc2[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_2.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_2.location = (rc2[0],rc2[1],rc2[2])
obj_2.keyframe_insert(data_path = "location",index = -1)
obj_2.rotation_euler =(0,0,0)
obj_2.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc3[0],rc3[1],rc3[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_3.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_3.location = (rc3[0],rc3[1],rc3[2])
obj_3.keyframe_insert(data_path = "location",index = -1)
obj_3.rotation_euler =(0,0,0)
obj_3.keyframe_insert(data_path ='rotation_euler', index=-1)



bpy.context.scene.cursor.location =(rc4[0],rc4[1],rc4[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_4.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_4.location = (rc4[0],rc4[1],rc4[2])
obj_4.keyframe_insert(data_path = "location",index = -1)
obj_4.rotation_euler =(0,0,0)
obj_4.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc5[0],rc5[1],rc5[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_5.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_5.location = (rc5[0],rc5[1],rc5[2])
obj_5.keyframe_insert(data_path = "location",index = -1)
obj_5.rotation_euler =(0,0,0)
obj_5.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc6[0],rc6[1],rc6[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_6.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_6.location = (rc6[0],rc6[1],rc6[2])
obj_6.keyframe_insert(data_path = "location",index = -1)
obj_6.rotation_euler =(0,0,0)
obj_6.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc7[0],rc7[1],rc7[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_7.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_7.location = (rc7[0],rc7[1],rc7[2])
obj_7.keyframe_insert(data_path = "location",index = -1)
obj_7.rotation_euler =(0,0,0)
obj_7.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc8[0],rc8[1],rc8[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_8.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_8.location = (rc8[0],rc8[1],rc8[2])
obj_8.keyframe_insert(data_path = "location",index = -1)
obj_8.rotation_euler =(0,0,0)
obj_8.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc9[0],rc9[1],rc9[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_9.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_9.location = (rc9[0],rc9[1],rc9[2])
obj_9.keyframe_insert(data_path = "location",index = -1)
obj_9.rotation_euler =(0,0,0)
obj_9.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc10[0],rc10[1],rc10[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_10.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_10.location = (rc10[0],rc10[1],rc10[2])
obj_10.keyframe_insert(data_path = "location",index = -1)
obj_10.rotation_euler =(0,0,0)
obj_10.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc11[0],rc11[1],rc11[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_11.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_11.location = (rc11[0],rc11[1],rc11[2])
obj_11.keyframe_insert(data_path = "location",index = -1)
obj_11.rotation_euler =(0,0,0)
obj_11.keyframe_insert(data_path ='rotation_euler', index=-1)


bpy.context.scene.cursor.location =(rc12[0],rc12[1],rc12[2])
bpy.ops.object.select_all(action='DESELECT')  #deselect first
obj_12.select_set(True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

obj_12.location = (rc12[0],rc12[1],rc12[2])
obj_12.keyframe_insert(data_path = "location",index = -1)
obj_12.rotation_euler =(0,0,0)
obj_12.keyframe_insert(data_path ='rotation_euler', index=-1)
    
# deal with the other frames
frameInterval=5
frame_number+=frameInterval
for i in range(1,len(thetaLIST)):

    vecMovelist=vecMoveLIST[i-1]
    vm0=vecMovelist[0:3]
    vm1=vecMovelist[3:6]
    vm2=vecMovelist[6:9]
    vm3=vecMovelist[9:12]
    vm4=vecMovelist[12:15]
    vm5=vecMovelist[15:18]
    vm6=vecMovelist[18:21]
    vm7=vecMovelist[21:24]
    vm8=vecMovelist[24:27]
    vm9=vecMovelist[27:30]
    vm10=vecMovelist[30:33]
    vm11=vecMovelist[33:36]
    vm12=vecMovelist[36:39]
    
    thetalist=thetaLIST[i-1]
    theta0=thetalist[0:3]
    theta1=thetalist[3:6]
    theta2=thetalist[6:9]
    theta3=thetalist[9:12]
    theta4=thetalist[12:15]
    theta5=thetalist[15:18]
    theta6=thetalist[18:21]
    theta7=thetalist[21:24]
    theta8=thetalist[24:27]
    theta9=thetalist[27:30]
    theta10=thetalist[30:33]
    theta11=thetalist[33:36]
    theta12=thetalist[36:39]
    
    rotateCenteri=potRefLIST[i]
    rc0=rotateCenteri[0:3]
    rc1=rotateCenteri[3:6]
    rc2=rotateCenteri[6:9]
    rc3=rotateCenteri[9:12]
    rc4=rotateCenteri[12:15]
    rc5=rotateCenteri[15:18]
    rc6=rotateCenteri[18:21]
    rc7=rotateCenteri[21:24]
    rc8=rotateCenteri[24:27]
    rc9=rotateCenteri[27:30]
    rc10=rotateCenteri[30:33]
    rc11=rotateCenteri[33:36]
    rc12=rotateCenteri[36:39]
    
    bpy.context.scene.frame_set(frame_number)
    
    obj_0.location = (rc0[0]+vm0[0],rc0[1]+vm0[1],rc0[2]+vm0[2])
    obj_0.keyframe_insert(data_path = "location",index = -1)
    obj_0.rotation_euler =(theta0[0]/180*np.pi,theta0[1]/180*np.pi,theta0[2]/180*np.pi)
    obj_0.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_1.location = (rc1[0]+vm1[0],rc1[1]+vm1[1],rc1[2]+vm1[2])
    obj_1.keyframe_insert(data_path = "location",index = -1)
    obj_1.rotation_euler =(theta1[0]/180*np.pi,theta1[1]/180*np.pi,theta1[2]/180*np.pi)
    obj_1.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_2.location = (rc2[0]+vm2[0],rc2[1]+vm2[1],rc2[2]+vm2[2])
    obj_2.keyframe_insert(data_path = "location",index = -1)
    obj_2.rotation_euler =(theta2[0]/180*np.pi,theta2[1]/180*np.pi,theta2[2]/180*np.pi)
    obj_2.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_3.location = (rc3[0]+vm3[0],rc3[1]+vm3[1],rc3[2]+vm3[2])
    obj_3.keyframe_insert(data_path = "location",index = -1)
    obj_3.rotation_euler =(theta3[0]/180*np.pi,theta3[1]/180*np.pi,theta3[2]/180*np.pi)
    obj_3.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_4.location =(rc4[0]+vm4[0],rc4[1]+vm4[1],rc4[2]+vm4[2])
    obj_4.keyframe_insert(data_path = "location",index = -1)
    obj_4.rotation_euler =(theta4[0]/180*np.pi,theta4[1]/180*np.pi,theta4[2]/180*np.pi)
    obj_4.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_5.location = (rc5[0]+vm5[0],rc5[1]+vm5[1],rc5[2]+vm5[2])
    obj_5.keyframe_insert(data_path = "location",index = -1)
    obj_5.rotation_euler =(theta5[0]/180*np.pi,theta5[1]/180*np.pi,theta5[2]/180*np.pi)
    obj_5.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_6.location = (rc6[0]+vm6[0],rc6[1]+vm6[1],rc6[2]+vm6[2])
    obj_6.keyframe_insert(data_path = "location",index = -1)
    obj_6.rotation_euler =(theta6[0]/180*np.pi,theta6[1]/180*np.pi,theta6[2]/180*np.pi)
    obj_6.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_7.location = (rc7[0]+vm7[0],rc7[1]+vm7[1],rc7[2]+vm7[2])
    obj_7.keyframe_insert(data_path = "location",index = -1)
    obj_7.rotation_euler =(theta7[0]/180*np.pi,theta7[1]/180*np.pi,theta7[2]/180*np.pi)
    obj_7.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_8.location = (rc8[0]+vm8[0],rc8[1]+vm8[1],rc8[2]+vm8[2])
    obj_8.keyframe_insert(data_path = "location",index = -1)
    obj_8.rotation_euler =(theta8[0]/180*np.pi,theta8[1]/180*np.pi,theta8[2]/180*np.pi)
    obj_8.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_9.location = (rc9[0]+vm9[0],rc9[1]+vm9[1],rc9[2]+vm9[2])
    obj_9.keyframe_insert(data_path = "location",index = -1)
    obj_9.rotation_euler =(theta9[0]/180*np.pi,theta9[1]/180*np.pi,theta9[2]/180*np.pi)
    obj_9.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_10.location = (rc10[0]+vm10[0],rc10[1]+vm10[1],rc10[2]+vm10[2])
    obj_10.keyframe_insert(data_path = "location",index = -1)
    obj_10.rotation_euler =(theta10[0]/180*np.pi,theta10[1]/180*np.pi,theta10[2]/180*np.pi)
    obj_10.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_11.location = (rc11[0]+vm11[0],rc11[1]+vm11[1],rc11[2]+vm11[2])
    obj_11.keyframe_insert(data_path = "location",index = -1)
    obj_11.rotation_euler =(theta11[0]/180*np.pi,theta11[1]/180*np.pi,theta11[2]/180*np.pi)
    obj_11.keyframe_insert(data_path ='rotation_euler', index=-1)

    obj_12.location = (rc12[0]+vm12[0],rc12[1]+vm12[1],rc12[2]+vm12[2])
    obj_12.keyframe_insert(data_path = "location",index = -1)
    obj_12.rotation_euler =(theta12[0]/180*np.pi,theta12[1]/180*np.pi,theta12[2]/180*np.pi)
    obj_12.keyframe_insert(data_path ='rotation_euler', index=-1)
    
    frame_number += 4










