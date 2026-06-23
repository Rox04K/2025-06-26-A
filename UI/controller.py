import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDYears(self):
        anni = self._model.getAnni()

        opzioniDD = list(map(lambda x: ft.dropdown.Option(x), anni))
        self._view._ddYear1.options = opzioniDD
        self._view._ddYear2.options = opzioniDD

        self._view.update_page()

    def handleBuildGraph(self, e):
        pass

    def handlePrintDetails(self, e):
        pass

    def handleCercaDreamChampionship(self, e):
        pass


