def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first != 1:
        return first
    return len(str_number)

result = get_multiplied_digits(40203)
print(result)

# def summa_list(my_list):
#     # if not my_list:
#     #     return 0
#     # return my_list[0] + summa_list(my_list[1:])
#
# my_list = [1, 2, 3, 4, 5, 6]
# print(summa_list(my_list))


# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
# print(summa(5))


# stack = []
# stack.append(1)
# print('Добавили элемент' , stack )
# stack.append(2)
# print('Добавили элемент' , stack )
# stack.append(3)
# print('Добавили элемент' , stack )
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)