# coding:utf-8
import cv2

__all__ = ['ImageCropUtils']


class ImageCropUtils(object):

    def __init__(self, device_info):
        self.config = device_info
        self.device_id = device_info.get('device_id')
        self.device_name = device_info.get('device_name')
        self.point1 = None
        self.point2 = None

    def save_coordinate_with_name(self, image_name):
        file_path = './config/' + self.device_name + '.yaml'
        with open(file_path, 'a') as f:
            f.write('  ' + image_name + ':\n')
            f.write('    x1: ' + str(self.point1[0]) + '\n')
            f.write('    y1: ' + str(self.point1[1]) + '\n')
            f.write('    x2: ' + str(self.point2[0]) + '\n')
            f.write('    y2: ' + str(self.point2[1]) + '\n')
            f.write('    threshold: ' + str(1) + '\n')
            f.write('    offset: ' + str(0.5) + '\n')

    def crop_picture(self, image_path, image_name, save_path):
        def on_mouse(event, x, y, flags, param):
            img2 = img.copy()
            if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
                self.point1 = (x, y)
                cv2.circle(img2, self.point1, 10, (0, 255, 0), 5)
                cv2.imshow(image_name, img2)
            elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
                cv2.rectangle(img2, self.point1, (x, y), (255, 0, 0), 5)
                cv2.imshow(image_name, img2)
            elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
                self.point2 = (x, y)
                cv2.rectangle(img2, self.point1, self.point2, (0, 0, 255), 5)
                cv2.imshow(image_name, img2)
                min_x = min(self.point1[0], self.point2[0])
                min_y = min(self.point1[1], self.point2[1])
                width = abs(self.point1[0] - self.point2[0])
                height = abs(self.point1[1] - self.point2[1])
                cut_img = img[min_y: min_y + height, min_x: min_x + width]
                cv2.imwrite(save_path + self.device_name + '_' + image_name + '.jpg', cut_img)

        img = cv2.imread(image_path + self.device_id + '.jpg')
        cv2.namedWindow(image_name)
        cv2.setMouseCallback(image_name, on_mouse)
        cv2.imshow(image_name, img)
        cv2.waitKey(0)
        self.save_coordinate_with_name(image_name)
