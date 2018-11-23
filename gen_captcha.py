#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 19:06:46 2018

@author: lps
@source: https://www.cnblogs.com/king-lps/p/8724361.html
"""
from captcha.image import ImageCaptcha
import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image
import random
import cv2

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

data_path = '.'


def random_captcha_text(char_set=number, captcha_size=4):  # 可以设置只用来生成数字
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text


def gen_capthcha_text_and_image(m):
    image = ImageCaptcha()
    captcha_text = random_captcha_text()  # 生成数字
    captcha_text = ' '.join(captcha_text)  # 生成标签

    captcha = image.generate(captcha_text)

    #    image.write(captcha_text,captcha_text+'.jpg')

    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)

    with open(data_path + "/label.txt", "a") as f:  # 写入标签
        f.write(captcha_text)
        f.writelines("\n")
    # 需要先创建 src 文件夹
    cv2.imwrite(data_path + '/src/' + '%.4d.jpg' % m, captcha_image)  # 保存


#    return captcha_text,captcha_image

if __name__ == '__main__':

    for m in range(0, 5000):
        #          text,image = gen_capthcha_text_and_image()
        gen_capthcha_text_and_image(m)

#    f = plt.figure()
#    ax = f.add_subplot(212)
#    ax.text(0.1,0.1,text,ha='center',va='center',transform=ax.transAxes)
#    plt.imshow(image)
#    plt.show()
#