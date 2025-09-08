selection_list = [34,4,5,56,3,45,6,6,78,8,8,5434,32,3,7,7]

non_duplicate = []
duplicate = []
count = []

for i in range(len(selection_list)):
    if selection_list[i]  not in non_duplicate:
        non_duplicate.append(selection_list[i])
        x = selection_list.count(selection_list[i])
        count.insert(i, x)
    else:
        duplicate.append(selection_list[i])


print(non_duplicate)
print(duplicate)
print(count)




