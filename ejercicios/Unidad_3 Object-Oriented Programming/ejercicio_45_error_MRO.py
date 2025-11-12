# CASO DE ERROR EN LA HERENCIA MÚLTIPLE - ¡APRENDER! ¡MEMORIZAR!

class A:
    def hacer_cosas_de_a(self):
        print('Hola, soy A')

# En este ejemplo esta clase no se utiliza
class B(A):
    def hacer_cosas_de_b(self):
        print('Hola, soy B')

class C(A):
    def hacer_cosas_de_c(self):
        print('Hola, soy C')

# class D(C,A):# NO PROVOCA ERROR PERO ES REDUNDANTE
class D(A,C):# PROVOCA UN ERROR TypeError
    def hacer_cosas_de_d(self):
        print('Hola, soy D')

d = D()
d.hacer_cosas_de_a() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C