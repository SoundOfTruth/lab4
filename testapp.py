import unittest
from main import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status_code(self):
        response = self.app.post("/")
        assert response.status_code == 200

    def test_file1(self):
        fl = open("test_files\\file1.txt", "rb")
        data = {'file': fl}
        response = self.app.post('/', data=data, follow_redirects=True, content_type='multipart/form-data')
        fl.close()
        assert "word." in response.text

    def test_file2(self):
        fl = open("test_files\\file2.txt", "rb")
        data = {'file': fl}
        response = self.app.post('/', data=data, follow_redirects=True, content_type='multipart/form-data')
        fl.close()
        assert "слово." in response.text

    def test_file3(self):
        fl = open("test_files\\file3.txt", "rb")
        data = {'file': fl}
        response = self.app.post('/', data=data, follow_redirects=True, content_type='multipart/form-data')
        fl.close()
        assert "жилой, дом, адрес, строительный, количество, квартир, шт" in response.text


if __name__ == "__main__":
    unittest.main()
