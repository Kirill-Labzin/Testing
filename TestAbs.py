import test_abs1
import test_abs2

class TestAbs(test_abs1.TestCase):
    
    def test_abs1(self):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_abs2(self):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
