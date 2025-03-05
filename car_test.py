import unittest
from cars import Car
class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        make="gm"
        model="malibu"
        year=2020
        self.price=40000
        self.km=10000
        self.avto1=Car(make,model,year)
        self.avto2=Car(make,model,year,km=self.km,price=self.price)
    def test_create(self):
        #Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        #Qiymatlar mavjud emasligini AssertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.avto1.price)
        #Qiymatlar tengligini assertEquels metodi bilan tekshiramiz
        self.assertEqual(0,self.avto1.get_km())
        self.assertEqual(self.price,self.avto2.price)
        self.assertEqual(self.km,self.avto2.get_km())

    def test_set_price(self):
        new_price=45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price,self.avto2.price)
    
    def test_add_km(self):
        #1 Musbat qiymat berib ko'ramiz.
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        #2 Manfiy qiymat berib ko'ramiz.
        km=-5000
        try:
            self.avto1.add_km(km)
        except ValueError as error:
            self.assertEqual(type(error),ValueError)
    def test_get_info(self):
        avto1_info="GM Malibu 2020 - yil, 0 km yurgan."
        self.assertEqual(avto1_info,self.avto1.get_info())
        self.avto1.set_price(25000)
        self.avto1.add_km(1000)
        avto1_info="GM Malibu 2020 - yil, 1000 km yurgan.Narxi: 25000"
        self.assertEqual(avto1_info,self.avto1.get_info())
unittest.main()
