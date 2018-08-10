from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import os.path as osp
import random, os
import cv2
import cPickle as cp
import scipy.signal as ssig
import scipy.stats as sstat
import pygame, pygame.locals
from pygame import freetype
#import Image
from PIL import Image
import math
from common import *
import random,string

for i in range(2000):
	extn = ["","ml","l","oz","lb"]
	index = int(np.random.randint(0, len(extn)))
	flt1 = np.random.uniform(1,10000)
	flt2  = np.random.uniform(1,100)
	text =  str(flt1)[:-5] + extn[index] + " " +str(flt2)[:5] + "$"
	x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
	date = np.random.randint(1,100,3)
	text = text + " " + x + " " + "/".join([str(y) for y in date])
	print(text)
	i += 1
