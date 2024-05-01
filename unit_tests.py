import unittest
from unittest.mock import mock_open, patch, MagicMock
import datetime
from meter_reader import parse_line, parse_file, count_meters, sum_of_invalid_meters, sum_of_valid_meters

class TestMeterReader(unittest.TestCase):
    def test_parse_line_meter(self):
        line_header = "HEADER|"
        line_meter = "METER|1300001188124|"
        line_reading ="READING|20200110000000|4810.1|20210402|V|"

        header_result = parse_line(line_header, 1)
        meter_result = parse_line(line_meter, 2)
        reading_result = parse_line(line_reading, 3)


        self.assertIsNone(header_result)
        self.assertIsNone(meter_result)
        self.assertEqual(reading_result, {'METER_ID': 1300001188124, 'READING_ID': 20200110000000, 'VALUE': 4810.1, 'DATE': datetime.date(2021, 4, 2), 'STATUS': 'V'} )

    def test_sum_of_invalid_meters_test(self):
        list_of_readings = [
            {'METER_ID': 2200019605568, 'READING_ID': 20200110000000, 'VALUE': 4810.1, 'DATE': datetime.date(2021, 4, 2), 'STATUS': 'V'},
            {'METER_ID': 1591024987400, 'READING_ID': 20200315000000, 'VALUE': 29310.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'V'},
            {'METER_ID': 1300001188124, 'READING_ID': 20200329000000, 'VALUE': 11519.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'V'},
            {'METER_ID': 1300001188124, 'READING_ID': 20200329001234, 'VALUE': 115.0, 'DATE': datetime.date(2021, 3, 31), 'STATUS': 'F'},
            {'METER_ID': 1300001188124, 'READING_ID': 2020032904567, 'VALUE': 1144.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'F'},
            {'METER_ID': 1300001188124, 'READING_ID': 2020032904567, 'VALUE': 1144.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'F'}
        ]
        sum = sum_of_invalid_meters(list_of_readings)
        self.assertEqual(sum, 3)

def test_sum_of_valid_meters_test(self):
        list_of_readings = [
            {'METER_ID': 2200019605568, 'READING_ID': 20200110000000, 'VALUE': 4810.1, 'DATE': datetime.date(2021, 4, 2), 'STATUS': 'V'},
            {'METER_ID': 1591024987400, 'READING_ID': 20200315000000, 'VALUE': 29310.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'V'},
            {'METER_ID': 1300001188124, 'READING_ID': 20200329000000, 'VALUE': 11519.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'V'},
            {'METER_ID': 1300001188124, 'READING_ID': 20200329001234, 'VALUE': 115.0, 'DATE': datetime.date(2021, 3, 31), 'STATUS': 'F'},
            {'METER_ID': 1300001188124, 'READING_ID': 2020032904567, 'VALUE': 1144.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'F'},
            {'METER_ID': 1300001188124, 'READING_ID': 2020032904567, 'VALUE': 1144.0, 'DATE': datetime.date(2021, 4, 1), 'STATUS': 'F'}
        ]
        sum = sum_of_valid_meters(list_of_readings)
        self.assertEqual(sum, 3)






if __name__ == '__main__':
    unittest.main()
