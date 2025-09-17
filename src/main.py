from config import SetConfig

import cv2
import numpy as np


def make_cv2_window(file_path_name):
    img = cv2.imread(file_path_name)

    cv2.imshow('imshow_test', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
    return




def make_grascal_img(file_path_name, output_file_name):
    # 画像を読み込む
    img = cv2.imread(file_path_name)

    # 画像の高さ、幅を取得する
    height = img.shape[0]
    width = img.shape[1]

    # 出力画像を初期化
    output = np.zeros((height, width, 1), np.uint8)

    # 画像の高さ分ループ
    for y in range(0, height):
        # 画像の幅分ループ
        for x in range(0, width):
            # グレースケール値
            val = 0
            for col in range(0, 3):
                # ピクセルごとに入力画像のRGB値を加算
                val += img[y, x, col]

            # RGB値の平均値を出力画像に設定
            output[y, x] = val / 3

    # 画像を保存する
    cv2.imwrite(output_file_name, img=output)

    return



def main():

    set_config = SetConfig()
    # make_cv2_window(set_config.file_name_path_1)
    make_grascal_img(set_config.file_name_path_1, set_config.save_file_name_1)

    return


if __name__== '__main__':
    main()