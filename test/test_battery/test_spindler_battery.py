import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_true(self):
        current_date = date.fromisoformat("2023-08-06")
        last_service_date = date.fromisoformat("2020-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_false(self):
        current_date = date.fromisoformat("2023-08-06")
        last_service_date = date.fromisoformat("2022-10-15")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
