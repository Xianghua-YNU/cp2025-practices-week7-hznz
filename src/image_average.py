import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt

def create_small_filter():
    """
    创建3×3平均滤波器
    
    返回:
        numpy.ndarray: 3×3的滤波器矩阵，每个元素值为1/9。每个元素的值为1/9是为了保证滤波器的权重总和为1，
                      从而在卷积过程中不会改变图像的整体亮度。
    """
    # 创建3x3的全1矩阵，并除以9进行归一化
    return np.ones((3, 3)) / 9

def create_large_filter():
    """
    创建15×15平均滤波器
    
    返回:
        numpy.ndarray: 15×15的滤波器矩阵，每个元素值为1/225。归一化系数为15×15=225，
                       保证滤波器权重总和为1。
    """
    # 创建15x15的全1矩阵，并除以225进行归一化
    return np.ones((15, 15)) / 225

def process_image(input_file):
    """
    处理图像并显示原始图像和滤波后的结果
    
    参数:
        input_file (str): 输入图像文件路径
        
    功能:
        1. 读取输入图像
        2. 创建3×3和15×15平均滤波器
        3. 对图像应用两种滤波器
        4. 显示原始图像和两种滤波结果对比
    """
    # 1. 读取图像，使用灰度模式读取以确保单通道
    img = plt.imread(input_file)
    
    # 2. 创建滤波器
    small_filter = create_small_filter()
    large_filter = create_large_filter()
    
    # 3. 应用卷积，使用默认边界处理模式
    small_result = sim.convolve(img, small_filter, mode='constant')
    large_result = sim.convolve(img, large_filter, mode='constant')
    
    # 4. 显示结果
    plt.figure(figsize=(15, 5))
    
    # 原始图像
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')  # 使用灰度色图显示
    plt.axis('off')              # 关闭坐标轴
    plt.title('Original Image')
    
    # 3×3滤波结果
    plt.subplot(1, 3, 2)
    plt.imshow(small_result, cmap='gray')
    plt.axis('off')
    plt.title('3×3 Filter Result')
    
    # 15×15滤波结果
    plt.subplot(1, 3, 3)
    plt.imshow(large_result, cmap='gray')
    plt.axis('off')
    plt.title('15×15 Filter Result')
    
    plt.tight_layout()  # 调整子图间距
    plt.show()

if __name__ == "__main__":
    # 主程序入口，确保bwCat.tif存在
    process_image('bwCat.tif')
