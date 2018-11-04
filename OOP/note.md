#OOP-Python面向对象
- Python的面向对象
- 面向对象编程（抽象、继承、封装、多态）
    - 基础
    - 公有私有
    - 继承
    - 组合、Minxi
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
#1.面向对象概述（ObjectOriented.00）
- OOP思想
    -对于任意任务，首先考虑任务这个世界的构成，由模型
- 几个名词
    - OO：面向对象
    - OOA：面向对象的分析
    - OOD：面向对象的设计
    - OOI：面向对象的实现
    - OOP：面向对象的编程
    - OOA -> OOD -> OOI: 面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物
    - 对象：具象的事物、单个个体
    - 类和对象的关系
        - 一个具象，代表一类事物的
#2.类的基本实现
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员的检查
    
            # dict前后各有两个下划线
            obj.__dict__
    类所有的成员
    
            class.name.__dict__
#3.anaconda基本使用
- anaconda 主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list: 显示anaconda安装的包
- conda env list: 显示anaconda的虚拟环境列表
- conda create -n XXX python=3.6: 创建python版本为3.6的名为XXX的虚拟环境