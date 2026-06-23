from model.model import Model

model = Model()
model.creaGrafo(2010,2016)

nodi, archi = model.getInfo()
print(f'Il grafo contiene {nodi} nodi e {archi} archi')

compConn = model.getCompConn()
print('Stampa dettagli:')
for c in compConn:
    print(f'{c[0]} - {c[1]}')

