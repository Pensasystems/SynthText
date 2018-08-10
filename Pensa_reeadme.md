#Author: Haindavi
#Date : June 21, 2018

SynthText creates synthetic data set to train and test text extraction models from images.
Modifications have been made to include CPG names in the creation of synthetic data set. 
Different fonts have also been added.

Changes made from the original SynthText repo:
    1. Added new fonts
    2. Added our own text source of CPG names
    3. Modified to take input from images, depth and segmentation given seperately (originally in h5 format)

1. To add new fonts :
Add the model file of the new font to data/fonts
Add the file name to data/fonts/fontlist.txt
run invert_font_size.py to generate the new font_px2pt.cp and overwrite the old file

2.To add more CPG names: 
The Synthtext model samples the words from data/newsgroup/newsgroup.txt
More CPG names can be added to this txt file.


