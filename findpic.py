#coding：utf-8
import cv2
import os
import time
import cv2 as cv
import Constant_MI5 as constant
import numpy as np
import numpy as np


def save_screen_cap_with_minicap(pic_name, path):
    screencap = 'adb -s '+ constant.device_id + ' shell \"LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P ' + constant.size + '@'+ constant.size  + '/0 -s > /mnt/sdcard/yys/' + pic_name + '.jpg\" '
    save_picture = 'adb -s ' + constant.device_id + ' pull /mnt/sdcard/yys/'+ pic_name +'.jpg ' + path + ' > /dev/null'
    os.system(screencap)
    os.system(save_picture)
    image = cv.imread(path + pic_name+'.jpg')
    return image

def mathc_img(image,Target,value):
    import cv2
    import numpy as np
    img_rgb = image
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = Target
    w, h = template.shape[::-1]
    print(w, h)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    print(res)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        print(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':

    # 加载原始RGB图像
    img_rgb = save_screen_cap_with_minicap(constant.device_id, './yys_temp/')
    # 创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    Target = cv2.imread('./yys_mark/Mi5_team_change_c84e662d.jpg',0)
    value = 0.9
    mathc_img(img_rgb, Target, value)
