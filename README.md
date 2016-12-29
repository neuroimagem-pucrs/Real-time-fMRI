# Real-time-fMRI
Real time fmri and fmri motion viewer files

Developed by:
Maicon Munch (engmdiogo@gmail.com)
Alexandre R. Franco (eng.franco@gmail.com)

This is the realtime fmri system that works on a GE Heathcare HDxt 3.0T (v.16) scanner. 

!#######################
What needs to be installed on the MRI computer:

"Dimon" (from AFNI)
Install on the follwing folder:
/export/home/sdc/bin/

On the following folder:
   /export/home/sdc/
put the script
   RTFMRI.sh
You'll need to start this script on the terminal every time you run an fMRI scan. Make sure you start it only after the localizer scan has been performed  

create the follwoing folder:
  /export/home/sdc/RTshells
Inside this folder, put the following file
  RTcommands.txt

in the folder:
/export
put the following files:
  output.txt  resultado.txt  sendFMRI.sh

!##########################################
!##########################################
What you'll need to install on the computer that will be recieving the images and controling for head motion. 
0) Install Linux (we recommend Ubuntu - well that's what we are using)

1) Download AFNI
  http://afni.nimh.nih.gov/afni/download/afni/releases/latest
  #Choose the following release: Linux OpenMP 64bit

2) Change to tcsh shell
 echo $SHELL									#print shell type 
 chsh -s /bin/tcsh							#change to tcsh. Its necessary to logout then login for it to work
 set prompt="%B[%n]: 						#Configure Prompt in .tcshrc file in home folder   			

3) Install Packages
  sudo apt-get install libxp6
  sudo apt-get install python-qt4 r-base

4) Set AFNI path
  set path = ( $path ~/abin ) 				#set on .tcshrc file

Copy the following files to the computer:
1) on the Desktop, copy the following files 
   InstructionsStartRTFMRI.txt 
   rtfmri_setup.sh
   
   For the rtfmri_setup.sh , you'll need to edit it to the username that you are using for your user (for us its "rtfmri")
   
 2) XXXXX


!##################

How to run the realtime fmri (and motion tracking) system







