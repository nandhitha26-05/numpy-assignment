import numpy as np
# n = np.random.random((4,4))
# print(n)

# arr = np.random.rand(3,3)
# print(arr)
# result = arr[arr>0.5]
# print(result)

# arr=np.random.randn(20)
# print(arr)
# positive = arr[arr>0]
# negative = arr[arr<0]
# print(positive)
# print(len(positive))
# print(negative)
# print(len(negative))
# arr[arr<0] = 0
# print(arr)

# arr = np.random.randint(1,101,25)
# print(arr)
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))
# even = arr[arr % 2 == 0]
# print(even)

# marks = np.array([35,45,55,65,75,85,95])
# select = np.random.choice(marks,4,replace=False)
# print(marks)
# print(select)

# arr = np.arange(1,21)
# print("before shuffling:")
# print(arr)
# np.random.shuffle(arr)
# print("after shuffle:")
# print(arr)

# arr = np.arange(10,101,10)
# print(arr)
# new_arr=np.random.permutation(arr)
# print(new_arr)
# print(arr)

# marks = np.random.randint(0,101,20)
# print(marks)
# failed = marks[marks<40]
# passed = marks[marks>=40]
# distinction = marks[marks>=75]
# print(failed)
# print(passed)
# print(distinction)

# salary = np.random.randint(20000,100001,15)
# print(salary)
# greater_50000 = salary[salary > 50000]
# print(greater_50000)
# between = salary[(salary >= 30000) & (salary <= 70000)]
# print(between)
# salary[salary<25000] = 25000
# print(salary)

# prices = np.random.randint(100,10001,20)
# print(prices)
# selected =  np.random.choice(prices, 5, replace = False)
# print(selected)
# np.random.shuffle(prices)
# print(prices)
# expensive = prices[prices>5000]
# print(expensive)
# prices[prices>5000]= prices[prices>5000] * 0.90
# print(prices)
# total = np.sum(prices)
# print(total)