#!/bin/tcsh

#AFNI needs some information about the acquisition in order to properly \
#construct a dataset from the images.  This information is sent to AFNI  
#as a series of command strings.  A sample set of command strings is
#given below:
   #ACQUISITION_TYPE 2D+zt
   #TR 5.0
   #XYFOV 240.0 240.0 112.0
   #ZNUM 16
   #XYZAXES S-I A-P L-R
   #DATUM short
   #XYMATRIX 64 64
#Ver em README.realtime todas variáveis necessárias

#Set Trust Host
setenv AFNI_TRUSTHOST 10.30.160.221

realtime_receiver.py -show_data yes	\
	-show_demo_gui yes -data_choice diff_ratio  

#Start real time receiver
#This program listens for connections at TCP port 53214

#-show_data yes 			display incoming data in terminal window 
#-show_demo_gui            		demonstrate a feedback GUI
#-data_choice diff_ratio 		pick which data to send as feedback. In this case (a-b)/(abs(a)+abs(b))

setenv AFNI_REALTIME_Registration  3D:_realtime
setenv AFNI_REALTIME_Base_Image    2
setenv AFNI_REALTIME_Graph         Realtime
setenv AFNI_REALTIME_MP_HOST_PORT  localhost:53214
setenv AFNI_REALTIME_SEND_VER      YES
setenv AFNI_REALTIME_SHOW_TIMES    YES
setenv AFNI_REALTIME_Mask_Vals     ROI_means
setenv AFNI_REALTIME_Function 	   FIM

cd ../afni
afni -rt -yesplugouts                     \
     -com "SWITCH_UNDERLAY epi_r1+orig"   \
     -com "SWITCH_OVERLAY func_slim+orig" &

prompt_user -pause        "         \
 - open graph window                \
 - FIM->Ignore->2                   \
 - FIM->Pick Ideal->epi_r1_ideal.1D \
 - close graph window"
