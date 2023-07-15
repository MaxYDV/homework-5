# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
#
# ■ Суму негативних чисел;
#
# ■ Суму парних чисел;
#
# ■ Суму непарних чисел;
#
# ■ Добуток елементів з кратними індексами 3;
#
# ■ Добуток елементів між мінімальним та максимальним елементом;
#
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
####################################################################################

# ■ Суму негативних чисел;
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# negative_sum = 0
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] < 0:
#         negative_sum += some_list_of_numbers[i]
# print(negative_sum)

# ■ Суму парних чисел;
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# sum_of_paired_numbers = 0
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] % 2 == 0:
#         sum_of_paired_numbers += some_list_of_numbers[i]
# print(sum_of_paired_numbers)

# ■ Суму непарних чисел;
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# sum_of_unpaired_numbers = 0
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] % 2 != 0:
#         sum_of_unpaired_numbers += some_list_of_numbers[i]
# print(sum_of_unpaired_numbers)

# ■ Добуток елементів з кратними індексами 3;
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# product_num = 1
# for i in range(1, len(some_list_of_numbers)):
#     if i % 3 == 0:
#         product_num *= some_list_of_numbers[i]
# print(product_num)

# ■ Добуток елементів між мінімальним та максимальним елементом;
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# start_ind = 0
# end_ind = 0
# product_num = 1
#
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] == min(some_list_of_numbers):
#         start_ind += i + 1
#         break
#
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] == max(some_list_of_numbers):
#         end_ind += i
#         break
#
# for i in range(start_ind, end_ind):
#     product_num += some_list_of_numbers[i]
# print(product_num)

# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# start_ind = 0
# end_ind = 0
# sum_numbers = 1
#
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] > 0:
#         start_ind += i + 1
#         break
#
# for i in range(len(some_list_of_numbers) - 1, -1, -1):
#     if some_list_of_numbers[i] > 0:
#         end_ind += i
#         break
#
# for i in range(start_ind, end_ind):
#     sum_numbers += some_list_of_numbers[i]
# print(sum_numbers)

####################################################################################
# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
#
# На підставі даних цього масиву потрібно:
#
# ■ Створити список цілих, що містить лише парні числа з першого списку;
#
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
#
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
#
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
####################################################################################
# ■ Створити список цілих, що містить лише парні числа з першого списку;
#
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# list_of_paired_numbers = []
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] != 0:
#         if some_list_of_numbers[i] % 2 == 0:
#             list_of_paired_numbers.append(some_list_of_numbers[i])
#             print(list_of_paired_numbers)

# ■ Створити список цілих, що містить лише непарні числа з першого списку;
#
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# list_of_unpaired_numbers = []
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] % 2 != 0:
#         list_of_unpaired_numbers.append(some_list_of_numbers[i])
#         print(list_of_unpaired_numbers)
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
#
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# list_of_negative_numbers = []
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] < 0:
#         list_of_negative_numbers.append(some_list_of_numbers[i])
#         print(list_of_negative_numbers)
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
#
# some_list_of_numbers = [-8, -3, -6, 9, 8, 1, 0, 7, -3, -3, -7, 7, 7, 1, 4, -5, 6]
# list_of_positive_numbers = []
# for i in range(len(some_list_of_numbers)):
#     if some_list_of_numbers[i] > 0:
#         list_of_positive_numbers.append(some_list_of_numbers[i])
#         print(list_of_positive_numbers)
####################################################################################