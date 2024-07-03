import time

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._selected_year = None




    def fillDDAnno(self):
        years = self._model._years
        for y in years:
            self._view._DD_anno.options.append(ft.dropdown.Option(data=y, text=y, on_click=self._choice_year))
        self._view.update_page()


    def _choice_year(self, e):
        if e.control.data is None:
            self._selected_year = None
        else:
            self._selected_year = e.control.data

    def handleGrafo(self, e):
        n_giorni = self._view._txtIn_giorni.value
        try:
            int_n_giorni = int(n_giorni)
        except ValueError:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Errore, inserire un valore intero in 'xGiorni'."))
            self._view.update_page()
            return
        self._model._crea_grafo(int_n_giorni, self._selected_year)
        nNodi, nArchi = self._model.get_dettagli_grafo()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato.\n"
                                                       f"Il grafo ha {nNodi} nodi e {nArchi} archi."))
        peso_nodi = self._model.get_peso_adiacenti()
        for p in peso_nodi:
            self._view.txt_result1.controls.append(ft.Text(f"{p[0]}, peso: {p[1]}"))
        self._view.update_page()



