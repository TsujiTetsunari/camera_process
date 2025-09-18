from config import SetConfig
from utils import (make_cv2_window,
                   make_grascal_img,
                   make_normal_img,
                   check_img_data)


import cv2
import numpy as np



def main():

    set_config = SetConfig()
    # make_cv2_window(set_config.file_name_path_1)
    # make_grascal_img(set_config.file_name_path_1, set_config.save_file_name_gr_1)
    # make_normal_img(set_config.file_name_path_1, set_config.save_file_name_no_1)

    check_img_data(set_config.file_name_path_1, set_config.save_file_name_1)

    return


if __name__== '__main__':
    main()