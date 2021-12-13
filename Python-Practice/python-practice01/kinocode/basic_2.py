numberList = [ 1, 2, 3, 4, 5, 6]
#  リストを出力
print(numberList)

#  条件分岐  else~if文は「eilf」で書く
age = 4
if age >= 20:
    print('adult')
elif age == 0:
    print('baby')
else:
    print('child')

#  繰り返し処理(Javascriptの繰り返し処理で書く「i++」は書かなくて良い)
for i in range(5):
    print(i)

#  break文(条件に当てはまったら、繰り返し処理を止める)
for i in range(5):
    if i == 3:
        break
    print(i)

#  continue文(条件に当てはまったら、その時の処理をスキップする)
for i in range(5):
    if i == 3:
        continue
    print(i)

#  for文のネスト
for i in range(3):
    for j in range(2):
        print(i, j, sep="_")

#  リスト内の要素を表示したい時の書き方(Javascriptでいうforeachメソッドのような考え方)
list = [2,4,6,8,10]
sum = 0
for i in list:
    print(i)
    sum +=i

print(sum)

