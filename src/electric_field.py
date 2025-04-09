"""
电偶极子电势与电场计算与可视化模板

本模板用于计算和可视化电偶极子的电势分布和电场线。
学生需要完成标有TODO的三个函数实现。
"""

import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k = 8.99e9  # 库仑常数 (N·m²/C²)
q_pos = 1e-9  # 正点电荷量 (C)
q_neg = -1e-9  # 负点电荷量 (C)

# 电荷位置 [x, y] 坐标 (m)
pos_charge_pos = np.array([0.05, 0])  # 正电荷位置
neg_charge_pos = np.array([-0.05, 0])  # 负电荷位置

def calculate_potential(X, Y):
    """
    计算二维空间电势分布
    
    参数:
        X, Y: 二维网格坐标矩阵 (numpy.ndarray)
        
    返回:
        V: 电势值矩阵 (numpy.ndarray)
    """
    # 计算每个点到正电荷的距离
    r_pos = np.sqrt((X - pos_charge_pos[0])**2 + (Y - pos_charge_pos[1])**2)
    # 计算每个点到负电荷的距离
    r_neg = np.sqrt((X - neg_charge_pos[0])**2 + (Y - neg_charge_pos[1])**2)
    
    # 计算电势 (V = k*q/r)
    V_pos = k * q_pos / r_pos
    V_neg = k * q_neg / r_neg
    V = V_pos + V_neg
    
    return V

def calculate_electric_field(V, spacing):
    """
    通过电势梯度计算电场强度
    
    参数:
        V: 电势值矩阵 (numpy.ndarray)
        spacing: 网格间距 (float)
        
    返回:
        Ex, Ey: 电场在x和y方向的分量 (numpy.ndarray, numpy.ndarray)
    """
    # 计算电势梯度 (注意负号)
    Ey, Ex = np.gradient(-V, spacing)
    
    return Ex, Ey

def main():
    """
    主函数: 计算并可视化电势和电场
    """
    # 创建计算网格
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)
    spacing = x[1] - x[0]  # 网格间距

    # 计算电势和电场
    V = calculate_potential(X, Y)
    Ex, Ey = calculate_electric_field(V, spacing)
    
    # 绘制结果
    plt.figure(figsize=(8, 6))
    
    # 绘制电势等高线图
    levels = np.linspace(-1000, 1000, 21)
    contour = plt.contourf(X, Y, V, levels=levels, cmap='jet')
    plt.colorbar(contour, label='Electric Potential (V)')
    
    # 绘制电场线
    plt.streamplot(X, Y, Ex, Ey, color='black', density=1.5, linewidth=1, arrowsize=1)
    
    # 标记电荷位置
    plt.plot(pos_charge_pos[0], pos_charge_pos[1], 'ro', markersize=8, label='Positive Charge')
    plt.plot(neg_charge_pos[0], neg_charge_pos[1], 'bo', markersize=8, label='Negative Charge')
    
    # 添加标签和标题
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Electric Dipole: Potential and Field Lines')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    
    plt.show()

if __name__ == "__main__":
    main()
