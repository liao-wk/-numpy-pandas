import numpy as np

array = np.array([[1, 2, 3],
                  [2, 3, 4]])
print(array)
print("按列求最大值：", np.max(array, axis=0))  # 注意
print("数组的维/行数：", array.ndim)
print("数组的行,列数：", array.shape)
print("数组的大小(行数x列数)：", array.size)
a1 = np.ones((3, 4), dtype=np.int64)
print("a1=", a1)
a2 = np.empty((3, 4))
print("a2=", a2)
a3 = np.arange(10, 20, 2)
print("a3=", a3)
a4 = np.arange(12).reshape((3, 4))
print("a4=", a4)
array2 = np.arange(3)
#  按行合并array和array2 向下合并
array3 = np.vstack((array, array2))  # vertical stack向下合并
print("按行合并array和array2,array3=", array3)
#  按列合并array2 和 array2 向右合并
array4 = np.hstack((array2, array2))  # horizontal stack
print("按列合并array2和array2,array4=", array4)
# 转置
print("array的转置：", array.T)
# 由于行向量.shape=(n,),所以无法转置。可以添加np.newaxis,增加缺少的另一个数。
print("行向量array2的转置：", array2.T, '依然是行向量')  # 注意：行向量的转置依然是行向量
array2_T = array2[:, np.newaxis]  # 将行向量转换为列向量
print("array2_T=", array2_T)
print("同理，array2[np.newaxis, :].T=", array2[np.newaxis, :].T)
#  注意字典，list, array都相当于指针，赋值的时候如果不想影响原来的变化，用.copy()命令。
