import cv2
import numpy
import matplotlib

image_paths = {
    'via': ['via.png', 0],
    'via2': ['via2.png', 0],
    'via3': ['via3.png', 0],
    'via4': ['via4.png', 0],
    #'sample': ['sample.png']
    'sample': ['../../boards/v1_6/board_1_6_top.png']
}


def load_images(paths):
    #loop through paths and load images
    return {
        key: cv2.bitwise_not(cv2.imread(
            val[0],
            (len(val) > 1) and val[1] or cv2.IMREAD_COLOR
        ))
        for (key, val) in paths.items()
    }

def match_test(tpl, img, color):
    #match
    print('matching')
    threshold = 0.7
    res = cv2.matchTemplate(
        img,
        tpl,
        cv2.TM_CCOEFF_NORMED
    )

    #draw rectangles
    print('drawing rects')
    w, h = tpl.shape[0:2]
    loc = numpy.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        center = (int(pt[0] + (w/2)), int(pt[1] + (h/2)))
        #cv2.rectangle(images['sample'], center, (pt[0]+w, pt[1]+h), color, 2)
        cv2.circle(img, center, int(w/2), color, 1)
    
def show_image(img):
    #resize
    print('resizing & displaying')
    #new = cv2.resize(images['sample'], (1200, 1300), interpolation=cv2.INTER_AREA)

    #show
    new = img
    cv2.namedWindow('result')
    cv2.moveWindow('result', 0,0)
    cv2.imshow('result', new)
    cv2.imwrite('output.png', new)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def main():
    #load images
    images = load_images(image_paths)
    
    #                                  BGR (blue, green, red)
    match_test(images['via'], images['sample'], (0,0,255))
    match_test(images['via2'], images['sample'], (0,255,0))
    match_test(images['via3'], images['sample'], (255,0,0))
    match_test(images['via4'], images['sample'], (255,0,255))
    show_image(images['sample'])


if __name__ == "__main__":
    main()
