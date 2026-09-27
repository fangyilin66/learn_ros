from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self,name:str,age:int,book:str) -> None:
        print('WriterNode __init__ 方法被调用了')
        super().__init__(name, age)  # 调用父类的__init__方法
        self.book = book


def main():
    node = WriterNode('法外狂徒张三',18,'论快速入狱')
    node.eat('鱼香肉丝')