import unittest
from helper import Query
from datetime import date
import os
from pathlib import Path

class TestQuery(unittest.TestCase):
    def test_object(self):
        query1 = Query(False, "abcd123")
        query2 = Query(True, "abc123.txt")
        self.assertNotEqual(query1, query2)
        self.assertFalse(query1.type == "File")
        self.assertTrue(query2.type == "File")
        self.assertEqual(query1.query_date, query2.query_date)

    def test_date_early(self):
        query1 = Query(False, "abcd123")
        self.assertTrue(query1.early_than_start_date(date(2023, 1, 1)))
        self.assertFalse(query1.early_than_start_date(date(2021, 1, 1)))

    def test_date_late(self):
        query1 = Query(False, "abcd123")
        self.assertTrue(query1.late_than_end_date(date(2021, 1, 1)))
        self.assertFalse(query1.late_than_end_date(date(2023, 1, 1)))

    def test_set_date(self):
        query1 = Query(False, "abcd123")
        query2 = Query(True, "abc123.txt")
        self.assertEqual(query1.query_date, query2.query_date)
        query1.set_date("2022-02-02")
        self.assertNotEqual(query1.query_date, query2.query_date)
        self.assertTrue(query1.early_than_start_date(query2.query_date))

    def test_is_file(self):
        query1 = Query(False, "abcd123")
        query2 = Query(True, "abc123.txt")
        self.assertNotEqual(query1.type, query2.type)
        self.assertEqual(query1.type, "String")
        self.assertEqual(query2.type, "File")

    def test_record(self):
        query1 = Query(False, "abcd123")
        query2 = Query(True, "abc123.txt")
        query1.record()
        query2.record()
        queries = [query1, query2]
        file_path = Path(os.getcwd()) / "Data" / "record.csv"
        self.assertTrue(os.path.exists(file_path))
        file = open(file_path, 'r')
        content = file.readlines()
        rows = content[-2: ]
        for i in range(2):
            self.assertEqual(rows[i].split("\n")[0], ",".join([queries[i].type, queries[i].content, queries[i].query_date.strftime("%Y-%m-%d")]) )
        file.close()

if __name__ == "__main__":
    unittest.main()