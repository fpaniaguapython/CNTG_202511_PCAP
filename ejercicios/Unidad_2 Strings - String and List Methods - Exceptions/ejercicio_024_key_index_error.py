# LookUpError

# IndexError
lista = [1, 3, 5, 7]
# print(lista[8]) # IndexError (hereda de LookupError, Exception, BaseException)

# KeyError
diccionario = {"Uno":"One", "Dos":"Two", "Tres":"Three"}
# print(diccionario['Cuatro']) # KeyError (heredad de LookupError, Exception, BaseException))

try:
    pass
except LookupError as le: # MAL. IndexError y KeyError son LookupError
    pass
except IndexError as ie:
    pass
except KeyError as ke:
    pass