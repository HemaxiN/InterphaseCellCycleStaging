''' Cell Cycle Classification '''

#import the packages
from classification_SVM import *
from nuclei_features import *
import numpy as np
import pandas as pd
import os

img_dir = r'C:\Users\hemaxi\Desktop\Nova pasta\deconv_imgs' ##directory where the images are saved
msk_dir = r'C:\Users\hemaxi\Desktop\Nova pasta\masks'  ##directory where the labeled masks are saved
save_dir = r'C:\Users\hemaxi\Desktop\Nova pasta\results' ##directory where the images will be saved
## after performing classification, nuclei classified as S/G2 will have a green bounding box
## and nuclei classified as G1 will have a red bounding box

def cell_cycle_classifier(imgs_dir, msks_dir, save_dir):
	features = obtain_features(imgs_dir, msks_dir, save_dir)
	features = process_dataframe(features)
	df, y_pred_vec = classify(features, save_dir)
	y_pred_vec = np.asarray(y_pred_vec)[0]
	df['pred_S_G2'] = y_pred_vec
	y_pred_vec = 1-y_pred_vec
	df['pred_G1'] = y_pred_vec
	
	final_metrics = df.groupby(["Image"], as_index=False).agg({'pred_G1': np.sum, 'pred_S_G2': np.sum})
	final_metrics.to_csv(os.path.join(save_dir, 'results.csv'), sep=';', index=False)

cell_cycle_classifier(img_dir, msk_dir, save_dir)
