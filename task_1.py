# Завдання 1
def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


fibonacci_cache = caching_fibonacci()
print(fibonacci_cache(8))
