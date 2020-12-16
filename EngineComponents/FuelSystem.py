
# -*- coding: utf-8 -*-
import random
import numpy

class FuelSystem:
    # Injectors resource capacity in km
    strenght_injectors = 140000

    # Fuel filter resource capacity in km
    strenght_fuel_filter = 16000

    list_issues = [
        'None',
        'Elevated_fuel_consumption',
        'Unstable_engine_operation',
        'Difficult_engine_starting',
        'Drop_in_engine_power',
        'Increase_in_engine_smoke',
        'Appearance_of_oil_emulsion_in_engine_coolant',
        'Increased_engine_noise',
        'When_car_is_running_engine_starts_to_triple',
        'When_engine_speed_rises_dips_occur',
        'Fuel_leak'
    ]

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

        self.list_set = set()
    
    def set_zero(self, value):
        return 0.0 if value < 0.0 else value

    def get_occured_issues(self):
        common_procent_strenght = (self.High_pressure_fuel_pump + self.Fuel_filter + self.Injectors + self.Fuel_priming_pump) / 4

        Elevated_fuel_consumption_distribution = (self.set_zero(100 - ((((self.High_pressure_fuel_pump + self.Fuel_filter + self.Injectors + self.Fuel_priming_pump) / 4) + 51))) / 100)
        Unstable_engine_operation_distribution = (self.set_zero(100 - ((self.High_pressure_fuel_pump + 51))) / 100)
        Difficult_engine_starting_distribution = (self.set_zero(100 - ((((self.High_pressure_fuel_pump + self.Fuel_priming_pump) / 2) + 51))) / 100)
        Drop_in_engine_power_distribution = (self.set_zero(100 - ((((self.High_pressure_fuel_pump + self.Fuel_priming_pump + self.Injectors) / 3) + 51))) / 100)
        Increase_in_engine_smoke_distribution = (self.set_zero(100 - ((((self.High_pressure_fuel_pump + self.Fuel_priming_pump) / 2) + 51))) / 100)
        Appearance_of_oil_emulsion_in_engine_coolant_distribution = (self.set_zero(100 - ((self.High_pressure_fuel_pump + 51))) / 100)
        Increased_engine_noise_distribution = (self.set_zero(100 - ((self.High_pressure_fuel_pump + 51))) / 100)
        
        When_car_is_running_engine_starts_to_triple_distribution = (self.set_zero(100 - ((((self.Fuel_filter + self.Fuel_priming_pump) / 2) + 51))) / 100)
        When_engine_speed_rises_dips_occur_distribution = (self.set_zero(100 - ((self.Fuel_filter + 51))) / 100)
        Fuel_leak_distribution = (self.set_zero(100 - ((self.Fuel_priming_pump + 51))) / 100)


        list_issues_p = [ 
            100.0,
            self.set_zero(Elevated_fuel_consumption_distribution),
            self.set_zero(Unstable_engine_operation_distribution), 
            self.set_zero(Difficult_engine_starting_distribution), 
            self.set_zero(Drop_in_engine_power_distribution), 
            self.set_zero(Increase_in_engine_smoke_distribution),
            self.set_zero(Appearance_of_oil_emulsion_in_engine_coolant_distribution),
            self.set_zero(Increased_engine_noise_distribution),
            self.set_zero(When_car_is_running_engine_starts_to_triple_distribution),
            self.set_zero(When_engine_speed_rises_dips_occur_distribution),
            self.set_zero(Fuel_leak_distribution)
        ]

        
        list_issues_p = numpy.array(list_issues_p)
        list_issues_p /= list_issues_p.sum()

        self.list_set.add(numpy.random.choice(self.list_issues, len(self.list_issues), 4, p=list_issues_p)[0])
        
        return self.list_set

    def run(self, increment_value):
        self.High_pressure_fuel_pump -= 0.0000001 * increment_value
        self.Fuel_filter -= 0.00625 * increment_value

        if self.Fuel_filter < 49:
            self.Injectors -= 0.00714 * increment_value
            self.High_pressure_fuel_pump -= 0.001 * (100 - self.Fuel_filter)
            self.Fuel_priming_pump -= 0.001 * (100 - self.Fuel_filter)

        self.Injectors -= 0.00714 * increment_value
        self.Fuel_priming_pump -= 0.0000000001 * increment_value