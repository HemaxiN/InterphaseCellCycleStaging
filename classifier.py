''' Cell Cycle Classification '''

#import the packages
from classification_SVM import *
from nuclei_features import *
import numpy as np
import pandas as pd

img_dir = r'C:\Users\hemaxi\Desktop\cell_cycle\imgs' ##directory where the images are saved
msk_dir = r'C:\Users\hemaxi\Desktop\cell_cycle\label'  ##directory where the labeled masks are saved
save_dir = r'C:\Users\hemaxi\Desktop\cell_cycle\class' ##directory where the images are saved,
## after performing classification, nuclei classified as S/G2 will have a green bounding box
## and nuclei classified as G1 will have a red bounding box

def cell_cycle_classifier(imgs_dir, msks_dir, save_dir):
	features = obtain_features(imgs_dir, msks_dir)
	features = process_dataframe(features)
	classify(features, save_dir)

cell_cycle_classifier(img_dir, msk_dir, save_dir)