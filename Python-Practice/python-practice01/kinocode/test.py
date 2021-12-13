class Student:


    def __init__(self, name):
        self.name = name

    def calc_avg(self, data):
        sum = 0
        for num in data:
            sum += num

        avg =sum / len(data)
        return avg

    def judge(self,avg):
        if (avg >= 60):
            result = 'passed!'
        else:
            result = 'failed!'
        return result


a001 = Student('Sato Kenta')
data = [80, 50, 70, 30, 10]
avg_score = a001.calc_avg(data)
result = a001.judge(avg_score)
print(avg_score, a001.name + ' ' + result)


#  複数インスタンス化
a002 = Student('')
data = [80, 80, 40, 60, 80]
avg_score = a002.calc_avg(data)
result = a002.judge(avg_score)
print(avg_score, a002.name+ '' + result)
