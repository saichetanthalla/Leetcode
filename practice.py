# matrix, given a, b find fibnocci. and for new row, add 1 to first 2 values and continue fibnocci]

# a,b=0,1
# coll,rows=10,15
# out=[]
# for i in range(rows):
#     col=[0+i,1+i]
#     a=0+i
#     b=1+i
#     for j in range(2,coll):
#         c=a+b
#         col.append(c)
#         a=b
#         b=c
#     out.append(col)
# print(out)

#----------------------------------------------------------------------------------------------------------------------
#given_array_in_inc_order_find_if_a_number _is_present_or_not, if yes, print those two numbers

# def array_sum(arr,s):
#     for i in range(len(arr)):
#         if arr[i]>=s:
#             arr=arr[:i+1]
#             break
#     remaining=[]
#     rem=[]
#     for i,j in enumerate(arr):
#         temp=s-j
#         s=temp
#         if j<temp:
#             pass
#         else:
#             remaining.append(j)
#
#     print(remaining)
# arr=[0,1,2,3,4,5,7,9,10,11]
# s=9
# array_sum(arr,s)

arr=[0,1,2,3,3,4,5]
i=0
j=1
n=9
while i<=j:
    if arr[i]+arr[j]==n:
        print(arr[i],arr[j])
        break
    elif arr[i]+arr[j]<n:
        i=i+1
    else:
        j= j+1
print('o')






