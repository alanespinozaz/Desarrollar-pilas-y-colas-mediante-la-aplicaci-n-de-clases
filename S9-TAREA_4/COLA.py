class Cola:
    def __init__(self,tamaño=10):
        self.cola=[]
        self.tope=0
        self.size=tamaño

    def empty(self):
        return self.tope == 0

    def push(self,dato):                #encolar
        self.cola += [dato]
        self.tope += 1

    def pop(self):               #desencolar
        if self.empty():
            return "La cola esta vacia"
        else:
            return self.cola.pop(0)

    def show(self):           #mostrar
        if self.empty():
            print("Cola vacia")
        else:
            for ele in self.cola:
                print("[{}]".format(ele))

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.cola):
            if ele == buscado:
                enc=True
                break
        if enc ==True:
            return pos
        else:
            return -1

    def longitud(self):
        return self.tope

cola1 = Cola(10)
cola1.push("4")
cola1.push("5")
cola1.push("7")
cola1.push("9")
cola1.pop()
print(cola1.cola)
# cola1.show()
# print(cola1.buscar("7"))
# print(cola1.longitud())

# 2) pilas
#     1) push
#     2) pop
#     3) show = mostrar
#     4) buscar
#     5) lingitud

# 3) colas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) longitud