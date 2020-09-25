
# -*- coding: utf-8 -*-

class FuelSystem:
    # Injectors resource capacity in km
    strenght_injectors = 140000

    # Fuel filter resource capacity in km
    strenght_fuel_filter = 16000

    def __init__(self, 
                    High_pressure_fuel_pump, # Топливный насос высокого давления 
                    Fuel_filter, # Топливный фильтр
                    Injectors, # Форсунки
                    Fuel_priming_pump, # Топливоподкачивающий насос
                    Tachometer
    ):
        strenght_fuel_filter_wear_pecentage = (Tachometer * 100) / self.strenght_fuel_filter
        strenght_injectors_wear_pecentage = (Tachometer * 100) / self.strenght_injectors

        self.High_pressure_fuel_pump = High_pressure_fuel_pump
        self.Fuel_filter = Fuel_filter - strenght_fuel_filter_wear_pecentage
        self.Injectors = Injectors - strenght_injectors_wear_pecentage
        self.Fuel_priming_pump = Fuel_priming_pump

    def run(self, increment_value):
        self.High_pressure_fuel_pump -= 0.0000001 * increment_value
        self.Fuel_filter -= 0.00625 * increment_value
        self.Injectors -= 0.00714 * increment_value
        self.Fuel_priming_pump -= 0.0000000001 * increment_value