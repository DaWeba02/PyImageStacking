# PyImageStacking  - Simple python script for stacking images above each other to get one stacked resized image. Made for e.g. CTF tasks regarding image processing. 
# Copyright (c) 2023 Markus Weber
# Github: DaWeba02 (https://github.com/DaWeba02)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import cv2
import numpy as np
import os

# $FILE_PATH: Define images path
path = "$FILE_PATH"

# Img namings should be like: FOO_01.foo or FOO01.foo -> The should all have an common name and a running number! All files must be of same type!
# $COMMON_NAME: A common file name all img files share
# Instead .foo -> .jpg, .png, .bmp, ... Or whatever type of files you have
img_list = []
for i in range(70):
    img_name = "$COMMON_NAME" + str(i) + ".foo"
    img_path = os.path.join(path, img_name)
    img = cv2.imread(img_path)
    img_list.append(img)

stacked_img = np.zeros_like(img_list[0], dtype=np.float32)
for img in img_list:
    stacked_img += img.astype(np.float32) / len(img_list)

stacked_img = np.round(stacked_img).astype(np.uint8)

# Resize to your liking!
resized_img = cv2.resize(stacked_img, (1920, 1080))

cv2.imshow('Resized Stacked Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


