import cv2
import numpy as np


# 定义最小外接矩形的绘制函数
def draw_min_rect(img, points, color=(0,0,255), thickness=2):
    img_copy = img.copy()
    rect = cv2.minAreaRect(np.array(points))
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img_copy, [box], 0, color, thickness)
    return img_copy

# 定义图片显示函数
def show_image(title, img):
    show_img = cv2.resize(img, (800, 600))
    cv2.imshow(title, show_img)
    cv2.waitKey(0)

# 目标1的标注信息是一个矩形,四个点的坐标顺序：左上角，右上角，右下角，左下角
x0, y0, x1, y1, x2, y2, x3, y3 = 508, 154, 876, 154, 876, 222, 508, 222
origin_points = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]

image = cv2.imread('src.jpg')
# 原始图片标注矩形绘制
image_draw = draw_min_rect(image, origin_points)
show_image('orgin image', image_draw)

# 原始图片以中心为原点旋转10度
angle = 10
h, w = image.shape[:2]
M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
image_rot = cv2.warpAffine(image, M, (w, h))

# 显示旋转后的图片
show_image('rotate image', image_rot)

# 此时，我们想要跟踪标注的点在新图中的位置
