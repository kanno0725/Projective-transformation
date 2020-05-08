# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:16:53 2020

@author: kanno
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

path = '131128.JPG'
i = cv2.imread(path,1)

#変換前後の対応点を設定
#p_original = np.float32([[292*4,325*4], [350*4,265*4], [373*4,364*4], [422*4,289*4]])
p_original = np.float32([[8*4,270*4], [400*4,68*4], [268*4,551*4], [536*4,69*4]])
#変更後のピクセル
height = 500
width = 1000
p_trans = np.float32([[0,0],[width,0],[0,height],[width,height]])
 
# 変換マトリクスと射影変換
M = cv2.getPerspectiveTransform(p_original, p_trans)
i_trans = cv2.warpPerspective(i, M, (width,height))

# 画像保存
cv2.imwrite('trans'+str(path), i_trans)

# ここからグラフ設定
fig = plt.figure()
ax1 = fig.add_subplot(111)

# 画像をプロット
show = cv2.cvtColor(i_trans, cv2.COLOR_BGR2RGB)
ax1.imshow(show)

fig.tight_layout()
plt.show()
plt.close()
