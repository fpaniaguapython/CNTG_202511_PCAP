class Cosa:
    def __eq__(self, other):
        print('Comparando...')
        return True
    

x = Cosa()
y = Cosa()

print('** ==:', x==y)
print('x is y:', x is y)


    