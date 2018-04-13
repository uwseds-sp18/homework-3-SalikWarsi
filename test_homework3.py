import unittest
import numpy as np
from homework3 import create_dataframe

# Define a class in which the tests will run
class PrimeTest(unittest.TestCase):

    def test_smoke(self):
        create_dataframe("class.db")

    def test_missing(self):
        with self.assertRaises(ValueError):
            create_dataframe("missing.db")
            
    def test_columns(self):
        df = create_dataframe("class.db")
        self.assertTrue(df.columns.size == 3)
        self.assertTrue("video_id" in df.columns)
        self.assertTrue("category_id" in df.columns)
        self.assertTrue("language" in df.columns)
            
    def test_key(self):
        df = create_dataframe("class.db")
        self.assertTrue(df.shape[0] == df[["video_id", "category_id", "language"]].drop_duplicates().shape[0])
        
if __name__ == '__main__':
    unittest.main()
