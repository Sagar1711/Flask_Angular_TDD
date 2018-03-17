from app import app, db
import unittest

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # def test_database(self):
        

if __name__ == '__main__':
    unittest.main()