class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f'Title:{self.title}. Year:{self.year}'
    
    def __repr__(self) -> str:
        # return self.__str__() # Esta línea devolvería la cadena proporcionada por __str__
        return f'T:{self.title}. Y:{self.year}'

it = Movie('It', 2002)
it_2 = Movie('It, Chapter 2', 2008)
the_shinning = Movie('The shinning', 1988)

movies = [it, it_2, the_shinning]

# Python tiene una implementación de __str__ para sus 'cosas'
print(3) # 3
print('Cine') # Cine
print(True) # True
print([3, True, "cinco"]) # [3, True, 'cinco']
print({'title':'The Shinning', 'year':1988}) # {'title': 'The Shinning', 'year': 1988}

# A Python hay que proporcionarle una implementación de __str__ para nuestras 'cosas'
# print(it) # sin __str__ --> <__main__.Movie object at 0x0000022A75484590>
print(it) # con __str__ --> Title:It. Year:2002)

# print(movies) # sin __repr__ --> [<__main__.Movie object at 0x00000217749C4590>, <__main__.Movie object at 0x00000217749B8410>, <__main__.Movie object at 0x00000217749B8550>]
print(movies) # con __repr__ --> [T:It. Y:2002, T:It, Chapter 2. Y:2008, T:The shinning. Y:1988]