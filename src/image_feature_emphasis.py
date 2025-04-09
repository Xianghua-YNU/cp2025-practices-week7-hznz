import os
import numpy as np
import scipy.ndimage as sim
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, './stressFibers.txt')
    return np.loadtxt(data_path)

def create_gauss_filter():
    v = np.arange(-25, 26)
    X, Y = np.meshgrid(v, v)
    return np.exp(-0.5*(X**2/5 + Y**2/45))

def create_combined_filter(gauss_filter):
    laplace = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    return sim.convolve(gauss_filter, laplace)

def process_and_display(image, kernel, scale=0.5):
    result = sim.convolve(image, kernel)
    plt.imshow(result, vmin=0, vmax=scale*result.max())
    plt.colorbar()
    plt.savefig('processed_output.png') 
    return result


def _plot_filter_3d(filter_matrix, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(np.arange(filter_matrix.shape[1]), 
                      np.arange(filter_matrix.shape[0]))
    ax.plot_surface(x, y, filter_matrix, cmap='viridis')
    plt.title(title)
    plt.savefig(f'{title}.png')
    plt.close()

# --------------------------
# 主程序流程
# --------------------------

if __name__ == "__main__":
    # 初始化数据
    fibers = load_stress_fibers()
    
    # 显示原始数据
    plt.imshow(fibers, cmap='gray')
    plt.title("Original Stress Fibers")
    plt.savefig("original_image.png")
    plt.close()

    # 生成滤波器
    gauss_kernel = create_gauss_filter()
    combined_kernel = create_combined_filter(gauss_kernel)
    
    # 滤波器可视化
    _plot_filter_3d(gauss_kernel, "Gaussian_Filter_3D")
    _plot_filter_3d(combined_kernel, "Combined_Filter_3D")

    # 执行特征强调
    process_and_display(fibers, combined_kernel)  # 垂直方向
    process_and_display(fibers, sim.rotate(combined_kernel, 90), 0.4)  # 水平方向
