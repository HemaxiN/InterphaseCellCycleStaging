# InterphaseCellCycleStaging


Code developed to perform interphase cell cycle staging of nuclei stained with DAPI. 

## How to use

To run this code please change the following directories in the file `classifier.py`:

* `img_dir:` directory containing the DAPI images


* `msk_dir:` directory containing the segmentation masks corresponding to the DAPI images in directory img_dir (To obtain the segmentation masks for the DAPI images use the code available in https://github.com/HemaxiN/YOLO_UNET.)


* `save_dir:` directory where the results will be saved

To perform cell cycle staging run the file `classifier.py` after changing the `img_dir`, `msk_dir` and `save_dir`. After performing classification nuclei classified as S/G2 will have a green bounding box and nuclei classified as G1 will have a red bounding box in the images present in the "save_dir", as shown in the following figure:


<p float="center">
<img width="347" height="260" src="img/MAX_24_7IF_Z60_decon1Imag_ALT.png"/>
</p>

Additionally, a .csv file containing detailed information regarding nuclei classification will be saved in the `save_dir`.

## How to cite
