import argparse
from yys.utils.device_config import DeviceConfig
from yys.gui.crop_picture_gui import CropPictureGUI

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MI8')
    args = parser.parse_args()
    d = DeviceConfig(args.p)
    a = CropPictureGUI(d.device_info)
    a.showWindow()
