from model.modelStudant import studanteModel
from view.pag_form_studant import formStudante
class studanteControl():
    def __init__(self):
        self.model = studanteModel()
        self.view = formStudante()
    def saveDataGetStudante(self):
        nome,idade,peso = self.view.getDataStudant()
        self.model.saveStudant()
        self.view.ShowMessegem("AMEM,VAI DA CERTO!")     