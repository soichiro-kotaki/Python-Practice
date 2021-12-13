#  関数の基本的書き方
def say_hello(greeting):
    print(greeting)

say_hello('HELLO WORLD')
say_hello('GOOD MORNING')
say_hello('GOOD EVENING')

#  3つの数字の平均を求める関数の書き方
def average(num1, num2, num3,):
    #  戻り値を返したい時はreturn文を書く
    return (num1 + num2 + num3) / 3

result = average(9, 4, 2)
print(result)
