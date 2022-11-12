import unittest
from helper import Recorder, Query
from datetime import date
import os
from pathlib import Path
import csv

class TestQuery(unittest.TestCase):
    def test_object(self):
        recorder = Recorder()
        self.assertEqual(recorder.csv_path, Path(os.getcwd()) / 'Data' / 'record.csv')
    
    def test_is_exist_csv(self):
        recorder = Recorder()
        if not os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'):
            self.assertFalse(recorder.is_exist_csv())
            open(Path(os.getcwd()) / 'Data' / 'record.csv', "w", newline="").close()
            self.assertTrue(recorder.is_exist_csv())
            os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')
        else:
            self.assertTrue(recorder.is_exist_csv())
            os.rename(Path(os.getcwd()) / 'Data' / 'record.csv', Path(os.getcwd()) / 'Data' / 'record_2.csv')
            self.assertFalse(recorder.is_exist_csv())
            os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')
            os.rename(Path(os.getcwd()) / 'Data' / 'record_2.csv', Path(os.getcwd()) / 'Data' / 'record.csv')
    
    def test_create_csv(self):
        recorder = Recorder()
        if os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'):
            os.rename(Path(os.getcwd()) / 'Data' / 'record.csv', Path(os.getcwd()) / 'Data' / 'record_2.csv')
            recorder.create_csv()
            self.assertTrue(os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'))
            os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')
            os.rename(Path(os.getcwd()) / 'Data' / 'record_2.csv', Path(os.getcwd()) / 'Data' / 'record.csv')
        else:
            recorder.create_csv()
            self.assertTrue(os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'))
            os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')

    def test_write_query(self):
        recorder = Recorder()
        rename = False
        if os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'):
            os.rename(Path(os.getcwd()) / 'Data' / 'record.csv', Path(os.getcwd()) / 'Data' / 'record_2.csv')
            rename = True

        recorder.write_query(True, "test.py")
        recorder.write_query(False, "abcdefg")
        with open(Path(os.getcwd()) / 'Data' / 'record.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            res = []
            for row in reader:
                res.append(row)
  
            self.assertEqual(res[0]['type'], "File")
            self.assertEqual(res[0]['content'], "test.py")
            date_list = res[0]['date'].split("-")
            date_int_list = [int(s) for s in date_list]
            query_date = date(date_int_list[0], date_int_list[1], date_int_list[2])
            self.assertEqual(query_date, date.today())

            self.assertEqual(res[1]['type'], "String")
            self.assertEqual(res[1]['content'], "abcdefg")
            date_list_1 = res[1]['date'].split("-")
            date_int_list_1 = [int(s) for s in date_list_1]
            query_date = date(date_int_list_1[0], date_int_list_1[1], date_int_list_1[2])
            self.assertEqual(query_date, date.today())

        os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')
        if rename:
            os.rename(Path(os.getcwd()) / 'Data' / 'record_2.csv', Path(os.getcwd()) / 'Data' / 'record.csv')

    def test_get_len_csv(self):
        recorder = Recorder()
        q1 = Query(True, "test.py")
        q2 = Query(False, "abcdefg")
        rename = False
        if os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'):
            rename = True
            os.rename(Path(os.getcwd()) / 'Data' / 'record.csv', Path(os.getcwd()) / 'Data' / 'record_2.csv')
        with open(Path(os.getcwd()) / 'Data' / 'record.csv', "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            row = ["type", "content", "date"]
            writer.writerow(row)
            row1 = [q1.type, q1.content, q1.query_date]
            writer.writerow(row1)
            row2 = [q2.type, q2.content, q2.query_date]
            writer.writerow(row2)
        self.assertEqual(recorder.get_len_csv(), 2)
        os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')
        if rename:
            os.rename(Path(os.getcwd()) / 'Data' / 'record_2.csv', Path(os.getcwd()) / 'Data' / 'record.csv')

    def test_get_range_data(self):
        recorder = Recorder()
        q1 = Query(True, "test.py")
        rename = False
        if os.path.exists(Path(os.getcwd()) / 'Data' / 'record.csv'):
            rename = True
            os.rename(Path(os.getcwd()) / 'Data' / 'record.csv', Path(os.getcwd()) / 'Data' / 'record_2.csv')
        with open(Path(os.getcwd()) / 'Data' / 'record.csv', "w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            row = ["type", "content", "date"]
            writer.writerow(row)
            row1 = [q1.type, q1.content, q1.query_date]
            writer.writerow(row1)
        
        with open(Path(os.getcwd()) / 'Data' / 'record.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            res = []
            for row in reader:
                res.append(row)

            startdate = date.today()
            enddate = date.today()
            queries = recorder.get_range_data(startdate, enddate)

            for q in queries:
                date_list = res[0]['date'].split("-")
                date_int_list = [int(s) for s in date_list]
                query_date = date(date_int_list[0], date_int_list[1], date_int_list[2])
                self.assertEqual(query_date, date.today())
        os.remove(Path(os.getcwd()) / 'Data' / 'record.csv')
        if rename:
            os.rename(Path(os.getcwd()) / 'Data' / 'record_2.csv', Path(os.getcwd()) / 'Data' / 'record.csv')


if __name__ == "__main__":
    unittest.main()