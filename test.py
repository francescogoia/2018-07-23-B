from model.model import Model

myModel = Model()
myModel._crea_grafo(20, 2014)
print(myModel.get_dettagli_grafo())
peso_adiacenti = myModel.get_peso_adiacenti()
for p in peso_adiacenti:
    print(p)
