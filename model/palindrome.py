from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery
from tires.apollo_tires import ApolloTires

class Palindrome(Car):
    def __init__(self, last_service_date, warning_indicator_on, tire_sensor_data):
        palindrome_engine = SternmanEngine(warning_indicator_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        palindrome_tire = ApolloTires(last_change_mileage, current_mileage)

        super().__init__(palindrome_engine, palindrome_battery, palindrome_tire)

        self.engine = palindrome_engine
        self.battery = palindrome_battery
        self.tire = palindrome_tire
    
    def needs_service(self):
        return super().needs_service()
