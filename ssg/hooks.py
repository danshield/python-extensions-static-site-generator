_callbacks = {}

def register(name, order = 0):
    def register_callback(func):
        _callbacks.setdefault(order, []).append(func)

    return register_callback

def event(hook, *args):
    for order in sorted(_callbacks.get(hook, {})):
        func(*args)

def filter(hook, value, *args):
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            value = func(value, *args)

    return value