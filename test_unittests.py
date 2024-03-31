import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):
    
    def test_website_loading(self):
        url = "https://atg.world/"
        print("Connecting to ATG.World website...")
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            print("Website loaded successfully!")
        except requests.ConnectionError:
            print("Failed to connect to the website!")
            self.fail("Failed to connect to ATG.World website")

if __name__ == '__main__':
    unittest.main()