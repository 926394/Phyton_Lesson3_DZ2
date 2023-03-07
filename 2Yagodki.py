# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.

# ПРИМЕР:
#4 -> 1 2 3 4
#9

n = int (input('Здравствуйте! Введите кол-во грядок:-)--> '))   
colors0 = list()
for i in range(n):
    colors0.append(i+1)

X = int(input('Введите № грядки в приделах: '))
res = 0
for i in range(X):
    if colors0[i] == X:
        res = colors0[-i] + colors0[i] + colors0[+i]
        
print(res)




