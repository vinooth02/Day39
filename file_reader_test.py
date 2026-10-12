import unittest
from file_reader import FileReader


class FileReaderTest(unittest.TestCase):

    def setUp(self):
        self.reader = FileReader()

    def test_read_existing_file(self):

        filename = "sample.txt"

        with open(filename, "w") as file:
            file.write("Hello Python")

        result = self.reader.read_file(filename)

        self.assertEqual(result, "Hello Python")

    def test_missing_file(self):

        result = self.reader.read_file("missing_file_123.txt")

        self.assertEqual(result, "File not found")


if __name__ == "__main__":
    unittest.main()