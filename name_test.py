import unittest
from name import get_full_name
class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name=get_full_name('sabohat','qayumova')
        self.assertEqual(name,"Sabohat Qayumova")
    def test_otasining_ismi(self):
        name=get_full_name('sabohat','qayumova','abduvaliyevna')
        self.assertEqual(name,"Sabohat Abduvaliyevna Qayumova")
unittest.main()