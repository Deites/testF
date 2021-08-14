def slice_less(my_list, lesser):
    my_list = [m for m in my_list if m > lesser]
    my_list.sort(reverse=True)
    print(my_list)

list = [1, 5, 10, 15, 3, 6, 9, 0, 2]
number = 6
slice_less(list, number)