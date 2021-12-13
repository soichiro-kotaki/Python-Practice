class Student:


    #  コンストラクタ（初期化メソッド）の書き方
    def __init__(self, name):
        self.name = name
    #  クラスのメソッドには、必ず引数の記述が必要。渡したい引数が無いときは「self」を書く。（渡したい引数がある場合も、第一引数には、 「self」を書き、第二引数に渡したい引数の名称を書く。
    def avg(self, math, english):
        print((math + english) / 2)

#  クラスのインスタンス化
a001 = Student('Sato')
a001.avg(80, 40)
print(a001.name)

a002 = Student('Tanaka')
print(a002.name)


