import cv2
import numpy
import matplotlib

image_paths = {
    'top': '../../boards/v1_6/board_1_6_top.png',
    'bottom': '../../boards/v1_6/board_1_6_bottom.png',
}

def load_images(paths):
    #loop through paths and load images
    return { key: cv2.imread(path) for (key, path) in paths }

def main():
    #load images
    images = {}

        'top': cv2.imread(image_paths['top']),
        'bottom': cv2.imread(image_paths['bottom']),
    }


if __name__ == "__main__":
    main()
