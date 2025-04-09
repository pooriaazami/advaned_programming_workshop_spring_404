class Memento:
    def __init__(self, state):
        self.state = state

class History:
    def __init__(self):
        self.history = []

    def push(self, state):
        self.history.append(state)

    def pop(self):
        if len(self.history) < 0:
            print('There is no history')
            return
        
        return self.history.pop()

class Board:
    def __init__(self):
        self.content = []

    def draw(self, obj):
        self.content.append(obj)

    def show(self):
        for obj in self.content:
            print(obj)

    def save_state(self):
        # self.history.append(self.content.copy())
        return  Memento(self.content.copy())

    # def undo(self):
    def restore(self, state):
        self.content = state.state


board = Board()
history = History()

board.draw('Line 1')
board.draw('Line 2')
board.draw('Line 3')

print('State 1:')
state1 = board.save_state()
history.push(state1)
board.show()


board.draw('Line 4')

print('State 2:')
state2 = board.save_state()
history.push(state2)
board.show()

board.draw('Line 5')
board.draw('Line 6')
board.draw('Line 7')

print('State 3:')
board.show()


print('=' * 100)
# print(board.history)
# print('=' * 100)

board.restore(history.pop())
board.show()
