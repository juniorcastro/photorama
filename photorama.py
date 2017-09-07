#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Photorama - Designit Barcelona Photobooth
#Version: 1.0
#Date: 5 Sep 2017


from picamera import PiCamera
from time import sleep
from os import system
import cups
from InstagramAPI import InstagramAPI

camera = PiCamera()

PhotoPath = "home/pi/photorama/temp" # Change Directory to Folder with Pics that you want to upload
IGUSER = "photorama.barcelona" # Change to your Instagram USERNAME
PASSWD = "barcelona32" # Change to your Instagram Password
IGCaption = "Hi from Barcelona #hola"


print("Taking photo 1")
camera.resolution = (1920,1200)
camera.capture("temp/photo1.jpg")
sleep(1)
print("Done photo 1")

print("Taking photo 2")
camera.resolution = (1920,1200)
camera.capture("temp/photo2.jpg")
sleep(1)
print("Done photo 2")

print("Taking photo 3")
camera.resolution = (1920,1200)
camera.capture("temp/photo3.jpg")
sleep(1)
print("Done photo 3")

print("Taking photo 4")
camera.resolution = (1920,1200)
camera.capture("temp/photo4.jpg")
sleep(1)
print("Done photo 4")



print("Start recordig video 1")
camera.resolution = (525,700)
camera.start_preview()
camera.start_recording("temp/video1.h264")
camera.wait_recording(2)
camera.stop_recording()
camera.stop_preview()
print("Done recording video 1")

print("Converting H264 to MP4")
system("MP4Box -add temp/video1.h264 temp/video1.mp4")
print("Boomerang it!")
system("ffmpeg -i temp/video1.mp4 -filter_complex '[0:v]reverse,fifo[r];[0:v][r] concat=n=2:v=1 [v]' -map '[v]' temp/boomerang1.mp4")
print("Converting MP4 to GIF")
system("ffmpeg -t 5 -i temp/boomerang1.mp4 temp/animation1.gif")



system("convert temp/photo1.jpg -resize x700 -gravity center -crop 525x700+0+0 +repage temp/crop1.jpg")
system("convert temp/photo2.jpg -resize x700 -gravity center -crop 525x700+0+0 +repage temp/crop2.jpg")
system("convert temp/photo3.jpg -resize x700 -gravity center -crop 525x700+0+0 +repage temp/crop3.jpg")
system("convert temp/photo4.jpg -resize x700 -gravity center -crop 525x700+0+0 +repage temp/crop4.jpg")

system("convert temp/crop1.jpg -extent 1200x1800-50-50 temp/photo_strip.jpg")

system("composite -compose atop -geometry +625+50 temp/crop2.jpg temp/photo_strip.jpg temp/photo_strip.jpg")
system("composite -compose atop -geometry +50+800 temp/crop3.jpg temp/photo_strip.jpg temp/photo_strip.jpg")
system("composite -compose atop -geometry +625+800 temp/crop4.jpg temp/photo_strip.jpg temp/photo_strip.jpg")

system("convert -type Grayscale temp/photo_strip.jpg temp/photo_strip_bw.jpg")


##conn = cups.Connection()
##printers = conn.getPrinters()
####default_printer = printers.keys()[0]
##cups.setUser('pi')
##conn.printFile (default_printer, "temp/photo_strip_bw.jpg", "photobooth", {'fit-to-page':'True'})


##igapi = InstagramAPI(IGUSER,PASSWD)

##print("Login to Instagram")
##igapi.login()

##print("Uploading photo to Instagram")
##igapi.uploadPhoto("temp/photo1.jpg",caption=IGCaption,upload_id=None)
