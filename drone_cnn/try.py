import os
import pandas as pd

train_dir="/home/dexter/Desktop/projects/ml/drone_tf_try2/object_detection/images/train/"

test_dir="/home/dexter/Desktop/projects/ml/drone_tf_try2/object_detection/images/test/"

img_dir="/home/dexter/datasets/drones/images/"


train_di=os.listdir(train_dir)

test_di=os.listdir(test_dir)

img_di=os.listdir(img_dir)
i=0
df_train=pd.read_csv("test.csv")
print(df_train["filename"])

for file in df_train["filename"]:
  print(i)
  os.rename(img_dir+file,test_dir+file)