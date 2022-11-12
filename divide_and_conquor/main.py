# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


  # Press ⌘F8 to toggle the breakpoint.
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
    while i < len(left):
        out.append(left[i])
    while j < len(right):
        out.append(right[j])
    return out

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    left = [1, 3, 4, 5, 5, 5]
    right = [0, 3, 3, 7, 45]
    merge(left,right)
    print(merge)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
