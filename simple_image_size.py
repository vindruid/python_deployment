
# coding: utf-8

# In[ ]:

## init : import libraries

import sys
import subprocess
import gc
import pandas as pd
import psycopg2
import csv
from datetime import datetime,timedelta
import datetime as dt
import os

# for keys
import re

# image 
import cv2
import urllib
import numpy as np
from scipy.signal import convolve2d

# paralelism
import multiprocessing
from multiprocessing import Pool

import warnings
warnings.filterwarnings('ignore')


# image_name = input('image name here: ')
image_name = '334569952.jpg'
img = cv2.imread(image_name)

print(img.size)

