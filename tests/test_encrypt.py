import unittest
import modules.encrypt as encoder_model

class EncryptTests(unittest.TestCase):

    def test_mix_of_up_down_cases(self):
        self.assertEqual(encoder_model.encrypt("Hello Word", 3), 'Khoor#Zrug')
        self.assertNotEqual(encoder_model.encrypt("nOtEqUaLToLoWeRcAsE", 5), 'styjvzfqytqtbjwhfxj')

if __name__ == '__main__':
    unittest.main()