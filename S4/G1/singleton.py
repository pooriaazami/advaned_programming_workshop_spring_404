class RegularClass:
    def __init__(self):
        print('Here')

class Singleton:
    Instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.Instance is None:
            Singleton.Instance = super().__new__(cls)

        return Singleton.Instance

    def __init__(self):
        print('self')

r1 = RegularClass()
r2 = RegularClass()

if r1 is r2:
    print('Theses two instances are the same.')
else:
    print('These two instances are not the same.')

print('=' * 50)

s1 = Singleton()
s2 = Singleton()

if s1 is s2:
    print('Theses two instances are the same.')
else:
    print('These two instances are not the same.')
