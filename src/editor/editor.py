import cmd 

class MachineEditor(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.automaton_loaded = False  # Attribut pour suivre si un automate est chargé

    def do_import(self, line):
        # Implémentation de l'importation
        self.automaton_loaded = True  # Mettre à jour lorsqu'un automate est importé

    def do_create(self, line):
        # Implémentation de la création
        self.automaton_loaded = True  # Mettre à jour lorsqu'un automate est créé

    def do_modify(self, line):
        if not self.automaton_loaded:
            print("Aucun automate n'est chargé.")
            return
        # Code pour modifier l'automate

    def do_save(self, line):
        if not self.automaton_loaded:
            print("Aucun automate n'est chargé.")
            return
        # Code pour sauvegarder l'automate
