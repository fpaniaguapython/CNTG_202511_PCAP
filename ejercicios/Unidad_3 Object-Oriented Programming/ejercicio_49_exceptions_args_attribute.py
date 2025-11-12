# El atributo args de una excepción contiene una tupla con todos los
# argumentos que se le pasaron durante su contrucción.
def sumar(x, y):
    if x==0:
        raise ArithmeticError('Uno','Dos','Tres')
    return x+y

try:
    sumar(0,8)
except ArithmeticError as ae:
    print(ae.args) # ('Uno', 'Dos', 'Tres')
