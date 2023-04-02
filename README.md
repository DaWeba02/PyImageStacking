# PyImageStacking 

PyImageStacking is a simple python script for stacking images above each other to get one stacked resized image. 
Made for e.g. CTF tasks regarding image processing. 

## Installation

Download main branch an run .py script in IDE of your choice!

## Usage

```python
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

# Resize to your liking!
resized_img = cv2.resize(stacked_img, (1920, 1080))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
