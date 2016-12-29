#!/bin/tcsh

setenv AFNI_REALTIME_Registration  	3D:_realtime
setenv AFNI_REALTIME_Base_Image    	2
setenv AFNI_REALTIME_Graph         	Realtime
setenv AFNI_REALTIME_MP_HOST_PORT  	localhost:53214
setenv AFNI_REALTIME_SEND_VER      	YES
setenv AFNI_REALTIME_SHOW_TIMES    	YES
setenv AFNI_REALTIME_Mask_Vals     	ROI_means
setenv AFNI_REALTIME_Function 	   	FIM
setenv AFNI_TRUSTHOST		   	10.30.160.183

setenv RECEIVED_IMAGES_DIR_BASE		imagesAFNI
setenv RECEIVED_IMAGES_DIR		`date +%Y-%m-%d.%H:%M:%S`

if ( ! -d $RECEIVED_IMAGES_DIR_BASE ) mkdir $RECEIVED_IMAGES_DIR_BASE
endif

cd $RECEIVED_IMAGES_DIR_BASE	

mkdir $RECEIVED_IMAGES_DIR

cd $RECEIVED_IMAGES_DIR

afni 	-rt 					\
	-yesplugouts				\
	-ignore 2				\
	-layout afni.startup_script &

#-com "SWITCH_UNDERLAY epi_r1+orig"   \
#-com "SWITCH_OVERLAY func_slim+orig"


prompt_user -pause        "         \
 - open graph window                \
 - FIM->Pick Ideal->epi_r1_ideal.1D \
 - close graph window"


