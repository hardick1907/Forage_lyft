from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery
from tires.apollo_tires import ApolloTires

class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        thovex_battery = NubbinBattery(last_service_date)
        thovex_tire = ApolloTires(last_change_mileage,current_mileage)

        super().__init__(thovex_engine, thovex_battery, thovex_tire)

        self.engine = thovex_engine
        self.battery = thovex_battery
        self.tire = thovex_tire
    
    def needs_service(self):
        return super().needs_service()
