import time

def time_decorator(t):
    def decorator_builder(function):
        def decorator(*args, **kwargs):
            start = time.time()
            function(*args, **kwargs)
            end= time.time()

            if t == 'ms':
                duration = (end - start) * 1000
                print(f'Duration: {duration:.2f} (ms)')
            elif t == 's':
                duration = end - start
                print(f'Duration: {duration:.2f} (s)')

        return decorator
    return decorator_builder

@time_decorator('ms')
def function(name):
    print(f'Hello, {name}')
    print('function() is called.')
    time.sleep(1)
    print('Done')

@time_decorator('s')
def another_function():
    print('another_function() is called.')
    time.sleep(1)
    print('Done')

function('Pooria')
another_function()