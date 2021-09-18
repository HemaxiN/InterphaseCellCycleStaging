import numpy as np
import pandas as pd
from joblib import load
import cv2
import os

def classify(df, save_path, imgs_dir):
	clf = load('svm_all.joblib') #load the trained model
	matrix = df.as_matrix(columns = ['norm_area', 'norm_intensity'])
	X_test = matrix.astype(float).reshape(matrix.shape)
	y_pred = clf.predict(X_test)
	i=0
	for index, row in df.iterrows():
	    if (y_pred[i] == 1):  ##nuclei labeled as s/g2
	        img = row['Image']
	        image = cv2.imread(os.path.join(imgs_dir, img))
	        bbox_aux = row['bbox']
	        xmin = bbox_aux[1]
	        ymin = bbox_aux[0]
	        xmax = bbox_aux[3]
	        ymax = bbox_aux[2]
	        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0),10)
	        cv2.imwrite(os.path.join(save_path, img), image)
	        i = i+1
	        
	    else:
	        img = row['Image']
	        image = cv2.imread(os.path.join(imgs_dir, img))
	        bbox_aux = row['bbox']
	        xmin = bbox_aux[1]
	        ymin = bbox_aux[0]
	        xmax = bbox_aux[3]
	        ymax = bbox_aux[2]
	        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 10)
	        cv2.imwrite(os.path.join(save_path, img ), image)
	        i = i+1
