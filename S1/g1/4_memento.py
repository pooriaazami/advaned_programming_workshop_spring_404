class Memeoto:
    def __init__(self, state):
        self.state = state

class History:
    def __init__(self):
        self.history = []

    def push(self, state):
        self.history.append(state)

    def pop(self):
        if len(self.history) == 0:
            print('There is no history yet!')
            return 

        return self.history.pop()    

class Board:
    def __init__(self):
        self.plane = []
    
    def draw(self, obj):
        self.plane.append(obj)

    def show(self):
        for obj in self.plane:
            print(obj)

    def create_state(self):
        return Memeoto(self.plane.copy())

    def restore(self, state):
        self.plane = state.state

board = Board()
history = History()

board.draw('Line 1')
board.draw('Line 2')
state1 = board.create_state()
history.push(state1)

print('First State:')
board.show()

board.draw('Line 3')
state2 = board.create_state()
history.push(state2)

print('Second State')
board.show()

board.draw('Line 4')
board.show()

board.restore(history.pop())
print('Last State:')
board.show()

board.restore(history.pop())
print('Last State:')
board.show()

