#!/usr/bin/env python3
import os
import glob
from PIL import Image

"""search all files start with 'ic', modify and save in other dir"""
for file in glob.glob("ic*"):
  im = Image.open(file).convert('RGB')
  im.rotate(270).resize((128, 128)).save("/opt/icons/" + file, "JPEG")

