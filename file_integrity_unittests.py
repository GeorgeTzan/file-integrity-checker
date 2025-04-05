import unittest
import file_integrity as fi
import os

class TestIntegrityChecker(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"
        with open(self.test_file, "w") as f:
            f.write("Hello World")

    def test_sha256(self):
        expected_hash = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e" 
        self.assertEqual(fi.calculate_file_hash(self.test_file), expected_hash)

    def tearDown(self):
        os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()