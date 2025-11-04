from calculadora import sumar as su, restar as re

# La notación __ indica que la función de ámbito privado
def __main_function():
    print(su(10,20))
    print(re(10,20))

if __name__=='__main__':
    __main_function()


