class Persona:
    """
    Questa classe rappresenta una persona caratterizzata da un etica per stabilire che ispira valori
    """
    def __init__(self, nome, cognome, etica=None,valori=None,opinioni=None,motivazioni=None):
        self.nome = nome
        self.cognome = cognome
        self.etica = etica
        self.valori = valori
        self.opinioni = opinioni
        self.motivazioni = motivazioni

    def __repr__(self):
        return f"{self.nome} {self.cognome}"

    def profilo_personale(self):
        profilo_p = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Etica: {self.etica}
        Valori: {self.valori}
        Opinioni: {self.opinioni}
        Motivazioni: {self.motivazioni}
        """
        return profilo_p
