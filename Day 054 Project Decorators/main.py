import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def get_time():
        first_time = time.time()
        function()
        second_time = time.time()
        print(f'{function.__name__} run speed: {second_time - first_time}s')
    return get_time


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
