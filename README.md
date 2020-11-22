# InterphaseCellCycleStaging


Code developed to perform interphase cell cycle staging of nuclei stained with DAPI. To run this code please change the following directories in the file classifier.py:


--> img_dir: directory containing the DAPI images


--> msk_dir: directory containing the segmentation masks corresponding to the DAPI images in directory img_dir (To obtain the segmentation masks for the DAPI images use the code available in https://github.com/HemaxiN/YOLO_UNET.)


--> save_dir: directory containing the DAPI images, after performing classification, nuclei classified as S/G2 will have a green bounding box and nuclei classified as G1 will have a red bounding box in the images present in this directory, as shown in the following figure:


