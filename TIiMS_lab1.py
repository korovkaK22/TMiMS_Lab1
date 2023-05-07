# ЛАБОРАТОРНА РОБОТА No1. ОПИСОВА СТАТИСТИКА
# Варіант 81
import math
import statistics
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#--------------ФУНКЦІЇ-----------------

#======Середнє значення======
def average (array):
    # знаходимо середнє значення вручну
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return  sum / len(array)

#======Медіана======
def median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        # Якщо кількість елементів парна, повертаємо середнє значення двох серединних елементів
        mid = n // 2
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # Якщо кількість елементів непарна, повертаємо серединний елемент
        return sorted_data[n // 2]

#======Мода========
def mode(arr):
    freq_dict = {}
    for elem in arr:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1

    mode = None
    max_freq = 0
    for key, value in freq_dict.items():
        if value > max_freq:
            max_freq = value
            mode = key

    return mode


#======Дисперсія========
def get_variance(data):
    n = len(data)
    mean = sum(data) / n
    cal_variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return cal_variance

# ======Середньоквадратичне відхилення========
def calculate_sd(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    sd = math.sqrt(variance)
    return sd



#--------------------------КОД---------------------------

#=======Генерація масиву========
mean = 10  # середнє значення
variance = 2.2  # дисперсія
size = 121  # кількість чисел
# генеруємо 121 випадкових чисел з дисперсією 2.2
mainArray = np.random.normal(loc=mean, scale=np.sqrt(variance), size=size)
print("\033[34mВхідний масив\033[0m")
print(str(mainArray))


#=============Бібліотечні розрахунки============
print('\n\n')
print('---Розрахунки за допомогою statistics---')
print("\033[34mСереднє значення: \033[0m" + str(round(statistics.mean(mainArray), 4)))
print("\033[34mМедіана: \033[0m" + str(round(statistics.median(mainArray), 4)))
print("\033[34mМода: \033[0m" + str(round(statistics.mode(mainArray), 4)))
print("\033[34mДисперсія: \033[0m" + str(round(statistics.pvariance(mainArray), 4)))
print("\033[34mСередньоквадратичне відхилення: \033[0m" + str(round(statistics.pstdev(mainArray), 4)))


#=============Розрахунок значень вручну============
print('\n\n')
print('---Розрахунок значень вручну---')
print("\033[34mСереднє значення: \033[0m" + str(round(average(mainArray), 4)))
print("\033[34mМедіана: \033[0m" + str(round(median(mainArray), 4)))
print("\033[34mМода: \033[0m" + str(round(mode(mainArray), 4)))
print("\033[34mДисперсія: \033[0m" + str(round(get_variance(mainArray), 4)))
print("\033[34mСередньоквадратичне відхилення: \033[0m" + str(round(calculate_sd(mainArray), 4)))

#====Гістограма частот=====
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Гістограма частот")
ax.hist(mainArray, edgecolor='black')
fig.show()


#====Полігон частот======

# Обчислення границь інтервалів та частот
bins = np.linspace(np.floor(mainArray.min()), np.ceil(mainArray.max()), num=11)
freq, _ = np.histogram(mainArray, bins=bins)

# Побудова полігону частот
plt.plot(bins[:-1], freq, linestyle='-', marker='o', color='b')
plt.xlabel('Інтервали')
plt.ylabel('Частота')
plt.title('Полігон частот для випадкової вибірки з дисперсією 2.2')
plt.show()



#=====Діаграма розмаху======

plt.title("Діаграма розмаху")
plt.boxplot(mainArray)
plt.show()


#=========Діаграма Парето======

# Сортуємо дані за спаданням
sorted_mainArray = sorted(mainArray, reverse=True)

# Розраховуємо відсотковий внесок кожного значення у загальну суму
cumulative_percentage = 100 * np.cumsum(sorted_mainArray) / sum(sorted_mainArray)

# Побудова діаграми Парето
fig, ax1 = plt.subplots()

# Графік стовпців
ax1.bar(range(len(sorted_mainArray)), sorted_mainArray, color='tab:blue')
ax1.set_xlabel('Значення')
ax1.set_ylabel('Кількість', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Другий графік (вісь y по правій стороні)
ax2 = ax1.twinx()
ax2.plot(range(len(sorted_mainArray)), cumulative_percentage, color='tab:red', marker='o')
ax2.set_ylabel('Відсоток', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Змінюємо мітки на вісі x
ax1.set_xticks(range(len(sorted_mainArray)))
ax1.set_xticklabels(sorted_mainArray)

# Відображаємо діаграму
plt.title('Діаграма Парето')
plt.show()

#==========Кругова діаграма===========

intArray =mainArray.astype(int)
uniqueArray= np.unique(intArray)
countArray= [np.count_nonzero(intArray == x) for x in uniqueArray]

fig4, ax4 = plt.subplots()
plt.pie(countArray, labels=uniqueArray, textprops={'fontsize': 6})


plt.title('Кругова діаграма')
plt.show()