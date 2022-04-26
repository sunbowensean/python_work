from unicodedata import name


class Dog():
    """模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化name,age属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        