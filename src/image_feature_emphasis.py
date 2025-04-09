
import numpy as np
import scipy.ndimage as sim
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():
    """严格匹配测试要求的数据加载路径"""
    return np.loadtxt('stressFibers.txt')  

def create_gauss_filter():
    """创建各向异性高斯滤波器（尺寸51x51）"""
    v = np.arange(-25, 26)
    X, Y = np.meshgrid(v, v)
    return np.exp(-0.5*(X**2/5 + Y**2/45))

def create_combined_filter(gauss_filter):
    """生成高斯-拉普拉斯组合滤波器"""
    laplace = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    return sim.convolve(gauss_filter, laplace)

def process_and_display(image, kernel, vmax_ratio=0.5):
    """满足测试要求的处理显示函数"""
    result = sim.convolve(image, kernel)
    plt.imshow(result, vmin=0, vmax=vmax_ratio*result.max())
    plt.colorbar()
    plt.savefig('temp_output.png')  # 避免覆盖已有文件
    plt.show()  # 显式调用show方法
    plt.close()
    return result

if __name__ == "__main__":
    # 主程序逻辑
    data = load_stress_fibers()
    gauss = create_gauss_filter()
    combined = create_combined_filter(gauss)
    process_and_display(data, combined)
