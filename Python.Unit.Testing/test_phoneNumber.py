import unittest
import phoneNumber
from phoneNumber import isvalid


class TestPhoneNumber(unittest.TestCase):



    def test_actual(self):#Test if the isvalid function validate a correct phone number
        result = phoneNumber.isvalid("2486195471")
        self.assertTrue(result)

    def test_cuntry_code(self):#Test if the isvalid function validate a correct phone number with correct cuntry code
        result = phoneNumber.isvalid("+12486195471")
        self.assertTrue(result)


    def test_less_degit(self):#Test if the isvalid function validate a wrong phone number 5 digit insted of 10
        result = phoneNumber.isvalid("24861")
        self.assertNotTrue(result)

    def test_prantesis(self):#Test if the isvalid function validate a correct phone number with ()
        result = phoneNumber.isvalid("(248)61954")
        self.assertTrue(result)

    def test_dash(self):#Test if the isvalid function validate a correct phone number with () and -
        result = phoneNumber.isvalid("(248)619-5471")
        self.assertNotTrue(result)

    def test_longer_digit(self):#Test if the isvalid function validate a wrong phone number with more than 10 digits
        result = phoneNumber.isvalid("24861954712345")
        self.assertNotTrue(result)

if __name__ == '__main__':
    unittest.main()
