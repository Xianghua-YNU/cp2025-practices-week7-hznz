import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_data():
    """加载应力纤维数据"""
    return np.loadtxt('stressFibers.txt')

def generate_gauss_kernel():
    """生成各向异性高斯滤波器，强调垂直方向特征"""
    x = np.arange(-25, 26)  # 生成-25到25的坐标
    X, Y = np.meshgrid(x, x)
    sigma_x = np.sqrt(5)    # X方向标准差
    sigma_y = np.sqrt(45)   # Y方向标准差（更大，强调垂直方向）
    gauss = np.exp(-0.5 * (X**2/(sigma_x**2) + Y**2/(sigma_y**2)))
    return gauss

def create_edge_filter():
    """生成拉普拉斯边缘检测滤波器"""
    return np.array([[0, -1, 0], 
                    [-1, 4, -1], 
                    [0, -1, 0]])

def plot_3d_surface(kernel, title):
    """绘制滤波器3D表面图"""
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(range(kernel.shape[1]), range(kernel.shape[0]))
    ax.plot_surface(x, y, kernel, cmap='coolwarm')
    ax.set_title(title)
    plt.show()

def apply_filter(image, kernel, scale=0.5):
    """应用滤波器并显示结果"""
    filtered = sim.convolve(image, kernel)
    plt.imshow(filtered, vmin=0, vmax=scale*filtered.max())
    plt.colorbar()
    plt.show()
    return filtered

# 主程序流程
if __name__ == "__main__":
    # 加载原始数据
    fiber_data = load_data()
    plt.imshow(fiber_data, cmap='gray')
    plt.title("原始应力纤维图像")
    plt.show()

    # 任务(a): 高斯滤波器
    gauss_kernel = generate_gauss_kernel()
    plt.imshow(gauss_kernel)
    plt.title("高斯滤波器（垂直方向）")
    plt.colorbar()
    plt.show()
    plot_3d_surface(gauss_kernel, "高斯滤波器3D表面图")

    # 任务(b): 组合滤波器
    laplace = create_edge_filter()
    combined_kernel = sim.convolve(gauss_kernel, laplace)
    plt.imshow(combined_kernel, origin='lower')
    plt.title("组合滤波器（高斯+拉普拉斯）")
    plt.colorbar()
    plt.show()
    plot_3d_surface(combined_kernel, "组合滤波器3D表面图")

    # 任务(c): 垂直方向特征增强
    print("垂直方向滤波结果:")
    vertical_result = apply_filter(fiber_data, combined_kernel)

    # 任务(d): 水平方向特征增强
    rotated_kernel = sim.rotate(combined_kernel, 90)
    print("水平方向滤波结果:")
    horizontal_result = apply_filter(fiber_data, rotated_kernel, 0.4)

    # 选做：45度方向
    angles = [45, -45]
    plt.figure(figsize=(10,4))
    for i, angle in enumerate(angles, 1):
        rotated_kernel = sim.rotate(combined_kernel, angle)
        result = sim.convolve(fiber_data, rotated_kernel)
        plt.subplot(1,2,i)
        plt.imshow(result, vmin=0, vmax=0.5*result.max())
        plt.title(f"{angle}度方向滤波")
        plt.colorbar()
    plt.tight_layout()
    plt.show()
