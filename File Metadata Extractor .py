#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 01:01:18 2025

@author: nb
"""


from PIL import Image
from PIL.ExifTags import TAGS

image_path = 'test.jpg' # Replace with the path to your image file.
print(f"Extracting metadata from: {image_path}")

try:
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data:
        print("--- EXIF Metadata Found ---")
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            print(f"{tag_name}: {value}")
    else:
        print("No EXIF metadata found in this file.")

except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")