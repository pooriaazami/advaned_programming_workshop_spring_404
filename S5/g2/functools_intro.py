from functools import partial

def test(some_text):
    print('Inside function test:')
    print(some_text)

hello = partial(test, 'Hello')

hello()