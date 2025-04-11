# 实验报告 - Pandas 数据操作练习

## 一、实验目的
本次实验的主要目的是通过实际案例掌握Pandas库的核心数据操作技能，包括：
1. 数据的创建与存储
2. 数据的基本信息查看
3. 缺失值的检测与处理
4. 数值型数据的统计分析
5. 数据的可视化展示
6. 处理结果的持久化保存

## 二、实验步骤

### 任务 1: 读取数据
使用os.makedirs()确保数据目录存在
通过os.path.exists()检查数据文件是否存在
若文件不存在，调用creat_frame()生成示例数据
使用pd.read_csv()读取CSV文件
关键代码：
os.makedirs("data", exist_ok=True)
if not os.path.exists("data/data.csv"):
    creat_frame()
return pd.read_csv('data/data.csv')

### 任务 2: 查看数据基本信息
使用DataFrame的info()方法获取数据概览
显示内容包括：
行数和列数
各列名称和非空值数量
数据类型信息
内存使用情况
关键代码：
data.info()

### 任务 3: 处理缺失值
通过data.isnull().any()检测含缺失值的列
使用列表推导式获取存在缺失值的列名列表
对数值型列（使用pd.api.types.is_numeric_dtype判断）：
计算该列均值
使用fillna()方法填充缺失值
关键代码：
missing_columns = data.columns[data.isnull().any()].tolist()
for col in missing_columns:
    if pd.api.types.is_numeric_dtype(data[col]):
        data[col] = data[col].fillna(data[col].mean())
### 任务 4: 数据统计分析
1. 使用select_dtypes(include=['number'])筛选数值列
2. 对每个数值列计算：
均值（mean()）
中位数（median()）
标准差（std()）
3. 使用f-string格式化输出统计结果
4. 关键代码：
numeric_columns = data.select_dtypes(include=['number']).
columns
for col in numeric_columns:
    print(f"{col} 列的均值: {data[col].mean()}, 中位数: {data[col].median()}, 标准差: {data[col].std()}")

### 任务 5: 数据可视化
选择"成绩"列作为可视化对象
使用plot.hist()绘制直方图
默认自动确定分箱数量
调用plt.show()显示图像
关键代码：
data[column_name].plot.hist()
plt.show()

### 任务 6: 数据保存
使用to_csv()方法保存处理后的数据
参数设置：
index=False：不保存行索引
默认UTF-8编码
保存为当前目录下的processed_data.csv文件
关键代码：
data.to_csv('processed_data.csv', index=False)

## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。

### 任务 1: 读取数据
读取的数据基本信息：
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   姓名      5 non-null      object 
 1   年龄      4 non-null      float64
 2   成绩      5 non-null      float64
 3   城市      5 non-null      object 
dtypes: float64(2), object(2)
memory usage: 288.0+ bytes

### 任务 2: 查看数据基本信息
数据基本信息：
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   姓名      5 non-null      object 
 1   年龄      4 non-null      float64
 2   成绩      5 non-null      float64
 3   城市      5 non-null      object 
dtypes: float64(2), object(2)
memory usage: 288.0+ bytes

### 任务 3: 处理缺失值
处理前："年龄"列有1个缺失值
处理后：所有列均无缺失值，缺失值已用均值(26.25)填充

### 任务 4: 数据统计分析
年龄 列的均值: 26.25, 中位数: 26.25, 标准差: 3.031088913245535
成绩 列的均值: 86.8, 中位数: 88.0, 标准差: 5.227332015474051

### 任务 5: 数据可视化
<img width="482" alt="{0BF30206-B8E0-4BBE-90A1-B0556AA925B1}" src="https://github.com/user-attachments/assets/12b255e8-661b-4675-93ee-7020e1fd713a" />


### 任务 6: 数据保存
"E:\文件\计算物理\processed_data.csv"
## 四、总结
收获与体会
掌握了Pandas进行数据处理的完整流程，学会了如何处理数据中的缺失值，熟悉了基本的数据统计分析方法，实践了使用Matplotlib进行简单的数据可视化
遇到的问题及解决方法
文件路径问题：初次运行时因data目录不存在导致报错，通过添加os.makedirs()解决，缺失值处理：最初只考虑了数值型列的填充，后来扩展了其他类型的处理逻辑，可视化优化：调整直方图的bins参数使分布更清晰
对Pandas的理解
Pandas提供了强大的数据处理能力，其DataFrame结构非常适合表格数据的操作。通过本次实验，我认识到：Pandas的方法链式调用可以写出更简洁的代码，数据清洗是数据分析的重要前提，可视化能直观展示数据特征
    
