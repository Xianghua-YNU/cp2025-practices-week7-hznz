"""
SymPy 绘图练习模板

本模板包含三个绘图练习，分别演示：
1. 基本函数绘图
2. 隐函数绘图 
3. 参数曲面绘图

学生需要完成每个函数中的TODO部分来实现相应绘图功能。
"""

import sympy as sp
from sympy.plotting import plot, plot_implicit, plot3d_parametric_surface

def problem1():
    """ 绘制 cos(tan(πx)) 在 [-1, 1] 区间的图像 """
    x = sp.Symbol('x')
    expr = sp.cos(sp.tan(sp.pi * x))
    plot(
        expr, (x, -1, 1),
        xlabel='x', ylabel='y',
        title='image: cos(tan(πx))',
        line_color='blue'
    )

def problem2():
    """ 绘制隐函数 e^y + cos(x)/x + y = 0 (x≠0) """
    x, y = sp.symbols('x y')
    equation = sp.Eq(sp.exp(y) + sp.cos(x)/x + y, 0)
    # 排除x=0并设置绘图范围
    plot_implicit(
        sp.And(equation, x != 0),
        (x, -10, 10), (y, -10, 10),
        xlabel='x', ylabel='y',
        title='image: e^y + cos(x)/x + y = 0 (x≠0)',
        points=500,
        depth=3  # 提高隐式方程求解精度
    )

def problem3():
    """ 绘制三维参数曲面 x=e^{-s}cos(t), y=e^{-s}sin(t), z=t """
    s, t = sp.symbols('s t')
    x = sp.exp(-s) * sp.cos(t)
    y = sp.exp(-s) * sp.sin(t)
    z = t
    plot3d_parametric_surface(
        x, y, z,
        (s, 0, 8), (t, 0, 5*sp.pi),
        xlabel='X', ylabel='Y', zlabel='Z',
        title='image',
        surface_color='goldenrod',
        mesh=True  # 显示网格线增强立体感
    )

if __name__ == "__main__":
    problem1()
    problem2()
    problem3()


if __name__ == "__main__":
    # 依次运行三个问题的绘图函数
    problem1()
    problem2()
    problem3()
