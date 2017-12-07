# Image Style Transfer

使用传统方法和神经网络的方法进行风格转移实验

## [Tradition Method](./tradition_method)
>传统方法

1. 使用reinhard算法迁移图像色彩
2. 使用Laplace金字塔或者是小波变换，将图像分解成高频部分和低频部分两个图像矩阵
3. 将图像的高频和低频部分按照一定的规则融合
4. 逆变换获得风格迁移后的图像

## [NEURAL NETWORK](./neural_network)
神经网络

代码是论文 [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155).
的实现。

代码实现者为 [hzy46/fast-neural-style-tensorflow](https://github.com/hzy46/fast-neural-style-tensorflow/)，使用说明，点入该库查看。
