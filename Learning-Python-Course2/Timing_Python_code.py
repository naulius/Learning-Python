def func_one(n):
    return [str(num)for num in range(n)]
print(func_one(10))

def func_two(n):
    return list(map(str,range(n)))
print(func_two(10))

import time
start_time = time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)