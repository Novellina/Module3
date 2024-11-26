def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
# print_params(a, b, c, d = 1.5) #выдает ошибку, потому что элементов больше, чем параметров
print_params(b = 25)
print_params(c = [1,2,3])
print()
values_list = [3, False, 'my_list']
values_dict = {'a':1, 'b':'строка', 'c':True}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = [3.3, 'can']
print_params(*values_list_2, 42)