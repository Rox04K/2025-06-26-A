import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._compConn = None

    def fillDDYears(self):
        anni = self._model.getAnni()

        opzioniDD = list(map(lambda x: ft.dropdown.Option(x), anni))
        self._view._ddYear1.options = opzioniDD
        self._view._ddYear2.options = opzioniDD

        self._view.update_page()

    def handleBuildGraph(self, e):
        start = self._view._ddYear1.value
        end = self._view._ddYear2.value

        if start is None or end is None:
            self._view.create_alert('Selezionare un anno di inizio e di fine!')
            return

        if start > end:
            self._view.create_alert('L\'anno di inizio deve essere più piccolo di quello di fine!')
            return

        self._view._txtGraphDetails.controls.clear()
        self._model.creaGrafo(start, end)
        self._view._txtGraphDetails.controls.append(ft.Text(f'Grafo correttamente creato:'))

        nodi, archi = self._model.getInfo()
        self._view._txtGraphDetails.controls.append(ft.Text(f'Numero di nodi: {nodi}'))
        self._view._txtGraphDetails.controls.append(ft.Text(f'Numero di archi: {archi}'))

        self._view.update_page()

    def handlePrintDetails(self, e):
        self._view._txtGraphDetails.controls.clear()

        conn = self._model.getCompConn()
        for c in conn:
            self._view._txtGraphDetails.controls.append(ft.Text(f'{c[0]} - {c[1]}'))

        self._compConn = conn
        self._view.update_page()

    def handleCercaDreamChampionship(self, e):
        if not self._model.hasGraph():
            self._view.create_alert('Devi prima creare il grafo!')
            return

        if self._compConn is None:
            connessa = self._model.getCompConn
        else:
            connessa = self._compConn

        k = self._view._txtInSoglia.value
        m = self._view._txtInNumDiEdizioni.value

        if k is None or m is None:
            self._view.create_alert('Inserisci le soglie!')
            return

        if not k.isdigit() or not m.isdigit():
            self._view.create_alert('Devono essere dei numeri!')
            return

        sottoCampionato, imprMax = self._model.getCampionato(int(k), int(m), connessa)
        self._view._txt_result.controls.append(ft.Text(f'La sottogara migliore ha un\'impredibilità di {imprMax}'))
        for c in sottoCampionato:
            self._view._txt_result.controls.append(c)

