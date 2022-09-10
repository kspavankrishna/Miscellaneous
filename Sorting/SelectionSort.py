# compare two elements and if it is smaller swap

def selection_sort(ulist):
    for i in range(0, len(ulist)):
        min_index = i
        for j in range(i + 1, len(ulist)):
            if ulist[min_index] > ulist[j]:
                min_index = j

        ulist[i], ulist[min_index] = ulist[min_index], ulist[i]
    return ulist


print(selection_sort([9, 1, 5, 2, 0]))

#K S Pavan Krishna