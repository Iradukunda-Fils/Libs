import numpy as np

# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = np.add(y, x)

# print(z)

# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])

# newarr = np.subtract(arr2, arr1)

# print(newarr)

# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([20, 21, 22, 23, 24, 25])

# newarr = np.multiply(arr1, arr2)

# print(newarr)


# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 5, 10, 8, 2, 33])

# newarr = np.divide(arr1, arr2)


# print(newarr)

# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 5, 6, 8, 2, 33])

# newarr = np.power(arr1, arr2)

# print(newarr)


# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.mod(arr1, arr2)

# print(newarr)


# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.remainder(arr1, arr2)

# print(newarr)


# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.divmod(arr1, arr2)

# print(newarr)


# arr = np.array([-1, -2, 1, 2, 3, -4])

# newarr = np.absolute(arr)

# print(newarr)

# arr = np.trunc([-3.1666, 3.4232])

# print(np.absolute(arr) @ np.array([2, 4]))

# print(abs(-3) * 2 + 3 * 4)


# arr = np.array([233, 343, "hello", "world"], dtype="O")

# print(arr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# arr = np.array([1, 2, 3, 4], dtype=np.int8)

# print(arr)

# narr = arr.astype("S30")
# narr[2] = "930239"

s = (sum(len(bin(i)) for i in list(len(bin(ord(i))[2:]) for i in "Worlde"))) / 8

print(s)

# print(arr.dtype)
# print(narr.dtype)


d = np.array(["hello", "Worlde"])

print(d.dtype)

# print(np.random.rand(5))
# print(np.random.randint(105232, size=(2, 5)))


# def myadd(x, y):
#   return x+y

# myadd = np.frompyfunc(myadd, , 1)

# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# arr1 = np.array([10, 20, 30, 40, 50, 60])
# arr2 = np.array([3, 7, 9, 8, 2, 33])

# newarr = np.divmod(arr1, arr2)

# print(newarr)



# arr = np.array([-1, -2, 1, 2, 3, 255])

# newarr = np.absolute(arr)

# newarr = arr = np.ceil([-3.6666, 3.1])

# print(newarr)


# arr = np.array([np.timedelta64(3, 'h')])

# from datetime import datetime

# today = datetime(2025, 6, 26)
# trip = datetime(2025, 7, 1)

# delta = trip - today

# print(delta)

# d1 = np.datetime64("2024-02-10")
# d2 = np.datetime64("2025-05-15")


# d = d2 - d1

# print(d)


# delta1 = np.timedelta64(5, 'D')   # 5 days
# delta2 = np.timedelta64(2, 'h')   # 2 hours

# print(delta1, "\n\n", delta2)