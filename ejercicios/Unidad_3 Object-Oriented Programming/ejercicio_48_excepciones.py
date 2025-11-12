def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print(" |" * (nest - 1), end="")
    if nest > 0:
        print(" +---", end="")
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(ConnectionError)
"""
ConnectionError
 +---BrokenPipeError
 +---ConnectionAbortedError
 +---ConnectionRefusedError
 +---ConnectionResetError
"""

# El método subclass proporciona las clases derivadas de la clase sobre la que se invoca
for subclass in ConnectionError.__subclasses__():
    print(subclass.__name__)
"""
BrokenPipeError
ConnectionAbortedError
ConnectionRefusedError
ConnectionResetError
"""
