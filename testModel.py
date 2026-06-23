from model.model import Model

model = Model()
model.creaGrafo(2010,2016)

nodi, archi = model.getInfo()
print(f'Il grafo contiene {nodi} nodi e {archi} archi')

