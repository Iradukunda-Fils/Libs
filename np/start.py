import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5, 6])
# c = np.array([[1, 2, 3], [4, 5, 6]])


# d = np.array([
#     [[1, 2, 3], [4, 5, 6]]
#     , [[1, 2, 3], [4, 5, 6]]
#     ])

# print(a.ndim)
# print(b.ndim)
# print(b.shape)
# print(c.ndim)
# print(d.ndim)
# print(d.shape, end="\n\n")


# print(np.array([
#   [[1, 2, 3], [4, 5, 6]],  # first "block" (like a page)
#   [[1, 2, 3], [4, 5, 6]]   # second "block"
# ]
# ).ndim)


# a = np.array([
#     [
#         [[1, 2], [3, 4]],
#         [[5, 6], [7, 8]]
#     ],
#     [
#         [[9, 10], [11, 12]],
#         [[13, 14], [15, 16]]
#     ]
# ])

# print(a.shape)
# print(a.ndim)

# print([[2,3, 43, 43],4] * 4)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)


# arr = np.array([
#     [1,2,3,4,5], 
#     [6,7,8,9,10]
#     ])

# print('2nd element on 1st row: ', arr[0, -2])


# arr = np.array([[[1, 2, 3, 4], [4, 5, 6, 7], [4, 5, 6, 7]], 
#                 [[7, 8, 9, 10], [10, 11, 12, 13], [4, 5, 6, 7]]])

# print(arr[:, 1:, -3:])
# # print(arr[1, 1, len(arr[1, 1]) // 2])

# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 6])

# print(arr[-4::-1])


# arr = np.array(["1.1f", "2.1", "3.1"])

# # newarr = arr.astype('i')

# print(arr)
# print(arr.dtype)


# print(bin(-255)[3:])
# print(len(str(bin(-255)[3:])))

# data = np.array([-128 ,127], dtype=np.int8)

# print(data.dtype)

# data = np.array([255], dtype=np.uint8)

# print(data.dtype)

# data = np.array([-128, 127], dtype="int8")

# print(abs(np.int16(data[0])) + data[1])

# print(np.int8(127).dtype)


# arr0 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print(arr)

# new = arr.view()
# new = arr.copy()
# new[7] = 90

# print(arr)
# print(new)

# newarr = arr0.view().reshape(4, 3)

# print(*newarr[2,1:])

# newarr[1,0:] = (91,94,74)

# print(newarr)

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate([arr1, arr2])

# print(arr)


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.concatenate([arr1, arr2, newarr[3]])

# print(arr)


# import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(arr[*x])
# print(arr[*np.where(arr % 2 == 0)])
# print(arr[*np.where(arr // 2 > 1)])


# arr = np.array([4, 24, 535, 4232, 54, 6, 3, 7, 52, 12, 7, 8, 9])

# sor = np.sort(arr)

# x = np.searchsorted(sor, (6,3,7))

# print(sor)

# print(*(x // 2 > 1 for x in arr))
# print(x)

# arr = np.array(['banana', 'cherry', 'apple'])

# print(np.sort(arr))

# arr = np.array([41, 42, 43, 44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)


# arr = np.array([41, 42, 43, 44])

# # Create an empty list
# filter_arr = [True if element > 42 else False for element in arr]
# filter_arr = arr > 42 
# # filter_arr = []

# # go through each element in arr
# for element in arr:
#   # if the element is higher than 42, set the value to True, otherwise False:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# filter_arr = arr // 2 > 1

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)





