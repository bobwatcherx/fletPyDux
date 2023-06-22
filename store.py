import pydux

def counter(state, action):
        if state is None:
            state = 0
        if action is None:
            return state
        elif action['type'] == 'INCREMENT':
            return state + 1
            print("tolol")
        elif action['type'] == 'DECREMENT':
            return state - 1
        return state
store = pydux.create_store(counter)
