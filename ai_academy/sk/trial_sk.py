# import sklearn.datasets

# digits = sklearn.datasets.load_digits()

# print('データの個数=', len(digits.images))
# print('画像データ=', digits.images[0])
# print('何の数字か=', digits.target[0])

import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0], cmap='Greys')
plt.show()