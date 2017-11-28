# -*- coding: utf-8 -*-

"""
Created by Wang Han on 2017/11/10 16:19.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All Rights Reserved.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Reinhard颜色迁移算法的过程
1. 将参考图片和源图片转换到LAB空间下
2. 得到参考图片和源图片的均值和标准差
3. 对源图片的每一个像素值，减去源图像均值然后乘上参考图片和源图片标准差的比值，再加上参考图像均值
4. 将源图片转换到RGB空间
'''


def reinhard(ref_image, src_image):
  def get_mean_and_std(lab_image):
    L_M_S_mean = np.zeros((3, 1))
    for idx in range(len(L_M_S_mean)):
      L_M_S_mean[idx] = np.mean(lab_image[:, :, idx])
    L_M_S_std = np.zeros((3, 1))
    for idx in range(len(L_M_S_std)):
      L_M_S_std[idx] = np.std(lab_image[:, :, idx])
    return L_M_S_mean, L_M_S_std

  if ref_image.shape[2] != 3 or src_image.shape[2] != 3:
    raise Exception("使用reinhard算法的输入必须是rgb3通道图片")
  ref_image_lab = cv2.cvtColor(ref_image, cv2.COLOR_BGR2LAB)
  src_image_lab = cv2.cvtColor(src_image, cv2.COLOR_BGR2LAB)
  mean1, std1 = get_mean_and_std(ref_image_lab)
  mean2, std2 = get_mean_and_std(src_image_lab)
  res_lab = np.zeros(ref_image.shape)
  for idx in range(3):
    res_lab[:, :, idx] = (src_image_lab[:, :, idx] - mean2[idx]) * (std1[idx] / std2[idx]) + mean1[idx]
    res_lab[:, :, idx][res_lab[:, :, idx] > 255] = 255
    res_lab[:, :, idx][res_lab[:, :, idx] < 0] = 0
  res_rgb = cv2.cvtColor(res_lab.astype('uint8'), cv2.COLOR_LAB2BGR)
  return res_rgb
