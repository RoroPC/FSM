import unittest
from editor import MachineEditor

class TestMachineEditor(unittest.TestCase):

    def setUp(self):
        self.editor = MachineEditor()

    def test_modify_without_machine(self):
        self.editor.machine_loaded = False
        # Utilisez self.assertIsNone si la méthode ne lève pas d'exception
        self.assertIsNone(self.editor.do_modify(""))

    def test_save_without_machine(self):
        self.editor.machine_loaded = False
        # Utilisez self.assertIsNone si la méthode ne lève pas d'exception
        self.assertIsNone(self.editor.do_save(""))

    # Ajoutez d'autres tests pour les scénarios où machine_loaded est True

if __name__ == '__main__':
    unittest.main()
