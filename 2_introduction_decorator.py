import time

def time_decorator(t):
    def decorator_builder(function):
        def decorator(*args, **kwargs):
            start = time.time()
            function(*args, **kwargs)
            end = time.time()

            if t == 'ms':
                duration = (end - start) * 1000
                print(f'duration: {duration:.2f} ms')
            elif t == 's':
                duration = end - start
                print(f'duration: {duration:.2f} s')

        return decorator
    return decorator_builder

@time_decorator('ms')
def function(name):
    print(f'You called function(), Hello {name}')
    time.sleep(1)
    print('function is done!')

@time_decorator('s')
def another_function():
    print('You called another_function()')
    time.sleep(1)
    print('another_function is done!')

function('Pooria')
another_function()
