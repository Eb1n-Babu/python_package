from operator import indexOf


selection_list = [34,4,5,56,3,45,6,6,78,8,8,5434,32,3]

z = []
for i in range(len(selection_list)):
    x = min(selection_list)
    y = selection_list.pop(selection_list.index(x))
    z.append(x)
    print(z)


