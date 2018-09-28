import os
import csv
import pandas as pd
import re
import cv2

dir=os.listdir("lab/")

images_dir="/home/dexter/datasets/drones/drone_photos/"
dir2=os.listdir(images_dir)

i=0
"""
for file in dir:
    with open("lab/"+file) as tsvfile,open("lab2/"+file,"a+") as outfile:
        im=cv2.imread(images_dir+file[:-3]+"jpg")
        #print(str(im.shape[1])+" "+str(im.shape[0]))
        reader = csv.reader(tsvfile, delimiter='\t')
        i+=1
        print(i)
        for row in reader:
                
                row=str(row[0])
                print(row)
                row=file[:-3]+"jpg,"+str(im.shape[1])+","+str(im.shape[0])+","+"drone"+row[1:]
                print(row)
                print(outfile)
                outfile.write(row)


for file in dir2:
    img=cv2.imread(images_dir+file)
    strin=file+","+str(img.shape[1])+","+str(img.shape[0])
    print(strin)

"""


