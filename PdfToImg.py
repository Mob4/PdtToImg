# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:29:22 2017

@author: DL9
"""

from __future__ import print_function
from wand.image import Image


 
with Image(filename='source.pdf',resolution=100) as img:
        print('pages = ', len(img.sequence))
        img.compression_quality = 99
        with img.convert('png') as converted:
            converted.save(filename='result/page_n.png')