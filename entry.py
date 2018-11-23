from torch.utils.data import Dataset
from torchvision import transforms
import numpy as np
import os
from PIL import Image

# 图片路径
image_path = './src'
# label文件路径
label_file = './label.txt'

# 关于 epoch、 iteration和batchsize 可以参见该博客: https://blog.csdn.net/sinat_30071459/article/details/50721565
# 批大小
BATCH_SIZE = 16
# 训练次数
EPOCH = 10


class MyDataset(Dataset):
    """
    数据集, 继承自 `torch.utils.data.Dataset`
    """

    def __init__(self, image_path, label_file, transform=None):
        self.image_path = image_path
        self.labels = np.loadtxt(label_file)
        """
        [[2. 2. 3. 1.]
         [9. 9. 8. 6.]
         [4. 9. 6. 1.]
         [4. 8. 8. 6.]
         [3. 2. 5. 9.]
         [0. 3. 7. 7.]
         [1. 3. 6. 9.]
         [5. 3. 5. 3.]
         [7. 4. 3. 6.]
         [0. 0. 8. 2.]]
        """
        self.transform = transform

    def __getitem__(self, index):
        # 连接文件夹与文件名, 由于文件名为 `0001.jpg` 因此可以这么获取
        image_name = os.path.join(self.image_path, '%.4d.jpg' % index)
        image = Image.open(image_name)
        label = self.labels[index]
        if self.transform:
            # 转化为 Tensor
            image = self.transform(image)
        return image, label

    def __len__(self):
        """
        np.size vs np.shape 的解释见: https://stackoverflow.com/a/44805136/6354733
        :return: 二阶矩阵的行数
        """
        return self.labels.shape[0]


dataset = MyDataset(image_path, label_file, transform=transforms.ToTensor())
dataset_size = len(dataset)
