"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


# sorted [O(N * logN)] + slice [O(N)]
# Algorithm complexity = max[O(N * logN), O(N)] = O(N * logN)
# the same can be done with dictionary sorted by value
def find_max_gain_list_1(lst_in):
    return (sorted(lst_in, key=lambda gain: gain[1]))[-3:]

# 3 + 3(N + 3 + N + 2) = 18 + 6N
# O(6N)
def find_max_gain_list_2(lst_in):
    max_gain = 0                                    #O(1)
    max_gain_index = 0                              #O(1)
    final_list = []                                 #O(1)
    for j in range(3):                              #O(1) - const. always 3 steps only.
        for i in range(len(lst_in)):                #O(N)
            if max_gain <= lst_in[i][1]:            #O(1)
                max_gain = lst_in[i][1]             #O(1)
                max_gain_index = i                  #O(1)
        final_list.append(lst_in[max_gain_index])   #O(1)
        lst_in.pop(max_gain_index)                  #O(N)
        max_gain_index = 0                          #O(1)
        max_gain = 0                                #O(1)
    return final_list


lst = [
    ["company_1", 1000],
    ["company_2", 12000],
    ["company_3", 104600],
    ["company_4", 10021340],
    ["company_5", 100330],
    ["company_6", 10034312340],
    ["company_7", 10],
    ["company_8", 1012303430],
    ["company_9", 100343425234530],

]
print(sorted(lst, key=lambda gain: gain[1]))
print(find_max_gain_list_1(lst))
print(find_max_gain_list_2(lst))
# find_max_gain_list_1 should be faster then find_max_gain_list_2 till N=10^6 where logN=6 =)))))))