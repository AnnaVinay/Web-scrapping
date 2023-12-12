# a = [7,2,15,4,11,6,0,3] # selection sort
# for i in range(1, len(a)): #start from 1 to end
#     key = a[i] # mark index 1 of value as minimum value
#     j = i-1 # index 0
#     while j>= 0 and key < a[j]: #if 
#         a[j+1] = a[j]
#         j -= 1
#     a[j+1] = key
# print(a)
###############################################################
# a = [7,2,5,4,1,6,0,3] #Bubble sorting
# for i in range(len(a)):
#     swapped = True
#     for j in range(0, len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#             swapped = True
#     if not swapped:
#         break
# print(a)
###############################################################
# def binary(arr,target):
#     left,right = 0,len(arr)-1
#     while left<=right:
#         mid = (left+right)//2
#         print(f'mid ; {mid}')
#         if arr[mid] == target:
#             return mid
#         elif arr[mid]>target:
#             right = mid - 1
#         else:
#             left = mid+1
#     return -1
# a = [1,2,3,4,5,6]
# t = 6
# print(binary(a,t))
# ##############################################################
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
    
#     mid = len(arr)//2
#     l_arr = arr[:mid]
#     r_arr = arr[mid:]
#     l_arr=merge_sort(l_arr)
#     r_arr=merge_sort(r_arr)
#     return merge(l_arr,r_arr)
# def merge(left,right):
#     i,j = 0,0
#     new = []
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             new.append(left[i])
#             i +=1
#         else:
#             new.append(right[j])
#             j +=1
#     new.extend(left[i:])
#     new.extend(right[j:])
#     return new
# a = [1,22,31,14,5,6]
# print(merge_sort(a))

###########################################################
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid = len(arr)//2
#     l_arr = arr[:mid]
#     r_arr = arr[mid:]
#     l_arr = merge_sort(l_arr)
#     r_arr = merge_sort(r_arr)
#     return merge(l_arr,r_arr)
# def merge(left,right):
#     i,j = 0,0
#     new = []
#     while i<(len(left)) and j<(len(right)):
#         if left[i]<right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j+=1

#     new.extend(left[i:])
#     new.extend(right[j:])
#     return new
# a= [12,23,13,34,1,2,45,4]
# print(merge_sort(a))
#########################################################
# Selection sort
# a = [7,2,4,5,0,6,1,3]
# for i in range(len(a)):
#     mini = i
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j] = a[j],a[i]
# print(a)

######################################################
# Bubble sort
# a= [7,2,4,5,0,6,1,3]
# for i in range(len(a)):
#     swapped = False
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#             swapped = True
#     print(a)
#     if not swapped:
#         break
# print(a)