def merge(left, right):
    out = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        #         print(left[i])
        #         print(right[j])

        if left[i] <= right[j]:
            out.append(left[i])
            print(out)
            i += 1
        else:
            out.append(right[j])
            j += 1
    print('****')
    print(i)
    print('****')
    while i < len(left):
        out.append(left[i])
    print('****')
    print(j)
    print('****')
    while j < len(right):
        out.append(right[j])
    return out

left= [1,3,4,5,5,5]
right=[0,3,3,7,45]
merge(left,right)
r=0