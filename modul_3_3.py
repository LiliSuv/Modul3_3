def print_params(a = 1, b='Домашнее задание', c = True):
    print(a,b,c)
print_params()
print_params(2,5,9)
print_params('В моем саду расцвели красивые лилии',3, 'штуки')
print_params("Московское время",'23 часа 18 минут')
print_params(b=25)
print_params(c=[1,2,3])
values_list=("Ночь нежна",245.34,True)
values_dict={'a':7,'b':12,'c':74}
print_params(*values_list)
print_params(**values_dict)
values_list_2=(6.7,'Ночь нежна')
print_params(*values_list_2,42)