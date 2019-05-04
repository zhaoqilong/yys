import argparse
from utils.device_config import DeviceConfig
from gui.crop_picture_gui import CropPictureGUI

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--p', type=str, default='MuMu')
    args = parser.parse_args()
    d = DeviceConfig(args.p)
    a = CropPictureGUI(d.device_info)
    a.showWindow()
