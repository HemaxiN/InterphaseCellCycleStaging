import cv2
import os
import pickle
import pandas as pd
import numpy as np 
from skimage.segmentation import clear_border
from skimage.measure import regionprops, label
import skimage

def obtain_features(images_path, predictions_path):
	#create the dataframe
	features = pd.DataFrame(columns = ["Image", "Area", "Total Intensity", "Mean Intensity", 
									  "Nucleus Patch", "bbox"])
	#for each image and prediction, read the image, load the pickle object
	for img, pred in zip(os.listdir(images_path), os.listdir(predictions_path)):
		#read the image
		image = cv2.imread(os.path.join(images_path, img), cv2.IMREAD_GRAYSCALE)
		#folder containing binary masks 
		masks = cv2.imread(os.path.join(predictions_path, pred), cv2.IMREAD_GRAYSCALE)
		masks = skimage.morphology.remove_small_objects(masks , min_size = 20)        
		masks_labelled = lbl2(masks)	        
		#compute features for each nuclei and add to the features dataframe
		features = compute_props(image, masks_labelled, features, img)
	return features

def lbl2(masks):
	#label the masks and clear the borders 
	#masks = label(masks) --> the output masks from https://github.com/HemaxiN/YOLO_UNET are already labeled
	prediction = clear_border(masks, buffer_size=1)
	return prediction

def compute_props(image, masks_labelled, features, img):
	properties = regionprops(masks_labelled, intensity_image = image)
	#for each nuclei, save the corresponding features 
	for region in properties:
		area = float(region.area)
		total_intensity = float(np.sum(region.intensity_image))
		mean_intensity = region.mean_intensity
		
		bbox_aux = region.bbox        
		
		filled_img = region.filled_image #binary image containing nucleus       

		saving_img = region.intensity_image
		
		xmin = bbox_aux[1]
		ymin = bbox_aux[0]
		xmax = bbox_aux[3]
		ymax = bbox_aux[2]    
		
		res = {"Image": img, "Area": area, "Total Intensity": total_intensity, "Mean Intensity": mean_intensity,
				"Nucleus Patch": saving_img, "bbox": bbox_aux}
		row = len(features)
		features.loc[row] = res
	return features

def create_new_table(pandasfilepath):
	df = pd.DataFrame(columns=["Image", "Area", "Total Intensity", "Mean Intensity", "Nucleus Patch", "bbox"])
	df.to_pickle(pandasfilepath)
	
def save_pd(pandasfilepath, result):
	result.to_pickle(pandasfilepath)    

''' process the dataframe to include the normalized area and normalized total intensity''' 
def process_dataframe(df_aux):
	var = df_aux.groupby(['Image'], as_index = False).var()
	mean = df_aux.groupby(['Image'], as_index = False).mean()

	normalized_area = []
	normalized_total_intensity = []

	for index, row in df_aux.iterrows():
	    #print(row['Area'], row['Total Intensity'])
	    img_name = row['Image']
	    area_mean =  mean[mean['Image'] == img_name]['Area']
	    area_mean = area_mean.as_matrix()[0]
	    area_var = var[var['Image'] == img_name]['Area']
	    area_var = area_var.as_matrix()[0]
	    area = row['Area']
	    n_area = (area - area_mean) / (np.sqrt(area_var))
	    intensity_mean =  mean[mean['Image'] == img_name]['Total Intensity']
	    intensity_mean = intensity_mean.as_matrix()[0]
	    intensity_var = var[var['Image'] == img_name]['Total Intensity']
	    intensity_var = intensity_var.as_matrix()[0]
	    intensity = row['Total Intensity']    
	    n_intensity = (intensity - intensity_mean) / (np.sqrt(intensity_var))
	    normalized_area.append(n_area)
	    normalized_total_intensity.append(n_intensity)
	    
	normalized_area_df = pd.Series( (v for v in normalized_area) ) 
	normalized_total_intensity_df = pd.Series((v for v in normalized_total_intensity))
	 
	df_aux['norm_area'] = normalized_area_df
	df_aux['norm_intensity'] = normalized_total_intensity_df
	    
	return df_aux

