import time
number = 1000


def recursive_fabbonacci(n: int) -> int:
    if n == 0:
        return 0
    
    if n == 1:
        return 1


    return recursive_fabbonacci(n - 1) + recursive_fabbonacci(n - 2)

start_time = time.time()
#print(recursive_fabbonacci(number))
print("--- %s seconds ---" % (time.time() - start_time))


def memoized_fabbonacci(n: int) -> int:
    fabbonacci_list = [0, 1]
    for i in range(2, n + 1):
        fabbonacci_list.append(fabbonacci_list[i - 1] + fabbonacci_list[i - 2])

    return fabbonacci_list[n]

start_time = time.time()
print(memoized_fabbonacci(number))
print("--- %s seconds ---" % (time.time() - start_time))