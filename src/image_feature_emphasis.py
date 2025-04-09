
import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():
    """加载应力纤维数据"""
    return np.loadtxt('stressFibers.txt') 

def create_gauss_filter():
    """创建各向异性高斯滤波器"""
    v = np.arange(-25, 26)
    X, Y = np.meshgrid(v, v)
    return np.exp(-0.5*(X**2/5 + Y**2/45))  

def create_combined_filter(gauss_filter):
    """创建组合滤波器"""
    laplace_filter = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    return sim.convolve(gauss_filter, laplace_filter)

def plot_filter_surface(filter, title):
    """绘制滤波器3D表面图"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.arange(filter.shape[1]), np.arange(filter.shape[0]))
    ax.plot_surface(X, Y, filter, cmap='viridis')
    plt.title(title)
    plt.show()

def process_and_display(image, filter, vmax_ratio=0.5):
    """处理并显示图像"""
    result = sim.convolve(image, filter)
    plt.imshow(result, vmin=0, vmax=vmax_ratio*result.max())
    plt.colorbar()
    plt.show()
    return result

if __name__ == "__main__":
    # 主程序流程
    stress_fibers = load_stress_fibers()
    
    # 显示原始数据
    plt.imshow(stress_fibers, cmap='gray')
    plt.title("Original Stress Fibers")
    plt.show()

    # 任务(a)
    gauss = create_gauss_filter()
    plt.imshow(gauss)
    plt.title("Gaussian Filter")
    plt.show()
    plot_filter_surface(gauss, "Gaussian Filter Surface")

    # 任务(b)
    combined = create_combined_filter(gauss)
    plt.imshow(combined, origin='lower')
    plt.title("Combined Filter")
    plt.show()
    plot_filter_surface(combined, "Combined Filter Surface")

    # 任务(c)
    process_and_display(stress_fibers, combined)

    # 任务(d)
    rotated_filter = sim.rotate(combined, 90)
    process_and_display(stress_fibers, rotated_filter, 0.4)
