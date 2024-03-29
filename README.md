# InterphaseCellCycleStaging


Code developed to perform interphase cell cycle staging of nuclei stained with DAPI. 
If you are using this code in your research please [cite the paper](#how-to-cite).

## Overview


![](https://github.com/HemaxiN/InterphaseCellCycleStaging/blob/main/img/Picture3.png)


## How to use

To run this code please change the following directories in the file `classifier.py`:

* `img_dir:` directory containing the DAPI images


* `msk_dir:` directory containing the segmentation masks corresponding to the DAPI images in directory `img_dir` (To obtain the segmentation masks for the DAPI images use the code available in https://github.com/HemaxiN/YOLO_UNET.)


* `save_dir:` directory where the results will be saved

To perform cell cycle staging run the file `classifier.py` after changing the `img_dir`, `msk_dir` and `save_dir`. After performing classification nuclei classified as S/G2 will have a green bounding box and nuclei classified as G1 will have a red bounding box in the images present in `save_dir`, as shown in the following figure:


<p align="center">
  <img width="347" height="260" src="img/MAX_24_7IF_Z60_decon1Imag_ALT.png">
</p>

Additionally, a `results.csv` file containing detailed information regarding nuclei classification will be saved in `save_dir`. It has the following structure:

| Image | pred_G1 | pred_S_G2 |
| ----- | ------- | --------- |
| image1.tif | 57 | 27 |
| image2.tif | 49 | 28 |
| ..... | ....... | ......... |

Each row contains the information for each image in `img_dir`. The first, second and third columns represent the image name, number of nuclei classified as G1 and number of nuclei classified as S/G2, respectively.

## Requirements

This implementation requires the packages listed in `requirements.txt`.


## How to cite

```bibtex
@article{narotamo2021machine,
  title={A machine learning approach for single cell interphase cell cycle staging},
  author={Narotamo, Hemaxi and Fernandes, Maria Sofia and Moreira, Ana Margarida and Melo, Soraia and Seruca, Raquel and Silveira, Margarida and Sanches, Jo{\~a}o Miguel},
  journal={Scientific Reports},
  volume={11},
  number={1},
  pages={1--13},
  year={2021},
  publisher={Nature Publishing Group}
}
```
