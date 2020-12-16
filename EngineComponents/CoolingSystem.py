# -*- coding: utf-8 -*-
import random
import numpy

class CoolingSystem:
    # Coolant pump strength value equal around 60 000 kilometers
    strenght_coolant_pump = 60000

    list_issues = [
        'None',
        'Cooling_fan_does_not_turn_on',
        'Cooling_fan_does_not_turn_off',
        'Cooling_fan_external_damage',
        'Cooling_pump_pulley_play',
        'Engine_overheating',
        'Antifreeze_leakage_under_car',
        'Appearance_of_pungent_smell_of_antifreeze_in_car',
        'Interior_heating_problems',
        'Damaged_cylinder_head_gasket',
        'Relief_valve_plunger_sticking',
        'Loose_radiator_cap_spring',
        'Smoke_from_under_hood',
        'White_steam_from_muffler',
        'Fan_turns_on_ahead_of_time',
        'Engine_takes_long_time_to_reach_operating_temperature',
        'Fluctuations_in_engine_temperature_while_driving'
    ]

    def __init__(self, 
                    Cooling_fan, # Вентилятор радиатора
                    Coolant_pump, # Насос системы охлаждения
                    Radiator, 
                    Radiator_cap, # Крышка радиатора
                    Expansion_tank, # Расширительный бачок
                    Thermostat,
                    Tachometer
    ):
        strength_coolant_pump_wear_pecentage = (Tachometer * 100) / self.strenght_coolant_pump

        self.Cooling_fan = Cooling_fan
        self.Coolant_pump = Coolant_pump - strength_coolant_pump_wear_pecentage
        self.Radiator = Radiator
        self.Radiator_cap = Radiator_cap
        self.Expansion_tank = Expansion_tank
        self.Thermostat = Thermostat

        self.list_set = set()

    def set_zero(self, value):
        return 0.0 if value < 0.0 else value
        
    def get_occured_issues(self):
        common_procent_strenght = (self.Cooling_fan + self.Coolant_pump + self.Radiator + self.Radiator_cap + \
                                   self.Expansion_tank + self.Thermostat) / 6 
        
        # print("Common strenght: ", common_procent_strenght)

        Cooling_fan_does_not_turn_on_distribution = (self.set_zero(100 - (((self.Cooling_fan + self.Thermostat) / 2 + 51))) / 100)
        Cooling_fan_does_not_turn_off_distribution = (self.set_zero(100 - (((self.Cooling_fan + self.Thermostat) / 2 + 51))) / 100)
        Cooling_fan_external_damage_distribution = (self.set_zero(100 - (((self.Cooling_fan) + 51))) / 100)

        Cooling_pump_pulley_play_distribution = (self.set_zero(100 - (((self.Coolant_pump) + 51))) / 100)
        Antifreeze_leakage_under_car_distribution = (self.set_zero(100 - (((self.Coolant_pump) + 51))) / 100)
        Appearance_of_pungent_smell_of_antifreeze_in_car_distribution = (self.set_zero(100 - (((self.Coolant_pump) + 51))) / 100)

        Interior_heating_problems_distribution =  (self.set_zero(100 - (((self.Radiator) + 51))) / 100)
        Damaged_cylinder_head_gasket_distribution =  (self.set_zero(100 - (((self.Radiator) + 51))) / 100)

        Relief_valve_plunger_sticking_distribution =  (self.set_zero(100 - (((self.Radiator_cap) + 51))) / 100)
        Loose_radiator_cap_spring_distribution =  (self.set_zero(100 - (((self.Radiator_cap) + 51))) / 100)

        White_steam_from_muffler_distribution = (self.set_zero(100 - (((self.Expansion_tank) + 51))) / 100)

        Fan_turns_on_ahead_of_time_distribution = (self.set_zero(100 - (((self.Thermostat) + 51))) / 100)
        Engine_takes_long_time_to_reach_operating_temperature_distribution = (self.set_zero(100 - (((self.Thermostat) + 51))) / 100)
        Fluctuations_in_engine_temperature_while_driving_distribution = (self.set_zero(100 - (((self.Thermostat) + 51))) / 100)

        Engine_overheating_distribution = (self.set_zero(100 - (((self.Coolant_pump + self.Radiator) / 2 + 51))) / 100)
        Smoke_from_under_hood_distribution = (self.set_zero(100 - (((self.Expansion_tank) + 51))) / 100)

        list_issues_p = [ 
            100.0,
            self.set_zero(Cooling_fan_does_not_turn_on_distribution),
            self.set_zero(Cooling_fan_does_not_turn_off_distribution), 
            self.set_zero(Cooling_fan_external_damage_distribution), 
            self.set_zero(Cooling_pump_pulley_play_distribution), 
            self.set_zero(Engine_overheating_distribution),
            self.set_zero(Antifreeze_leakage_under_car_distribution),
            self.set_zero(Appearance_of_pungent_smell_of_antifreeze_in_car_distribution),
            self.set_zero(Interior_heating_problems_distribution),
            self.set_zero(Damaged_cylinder_head_gasket_distribution),
            self.set_zero(Relief_valve_plunger_sticking_distribution), 
            self.set_zero(Loose_radiator_cap_spring_distribution), 
            self.set_zero(Smoke_from_under_hood_distribution), 
            self.set_zero(White_steam_from_muffler_distribution),
            self.set_zero(Fan_turns_on_ahead_of_time_distribution),
            self.set_zero(Engine_takes_long_time_to_reach_operating_temperature_distribution),
            self.set_zero(Fluctuations_in_engine_temperature_while_driving_distribution)
            ]

        
        list_issues_p = numpy.array(list_issues_p)
        list_issues_p /= list_issues_p.sum()

        self.list_set.add(numpy.random.choice(self.list_issues, len(self.list_issues), 4, p=list_issues_p)[0])
        
        return self.list_set

    def run(self, increment_value):
        self.Cooling_fan -= 0.0000001 * increment_value
        self.Coolant_pump -= 0.0017 * increment_value

        if self.Cooling_fan < 49:
            self.Radiator -= 0.0001 * increment_value

        if self.Coolant_pump < 49:
            self.Radiator -= 0.0001 * increment_value

        self.Radiator -= 0.000000001 * increment_value
        self.Radiator_cap -= 0.00001 * increment_value
        
        if self.Radiator < 50:
           self.Expansion_tank -= 0.00001 * increment_value 
           
        self.Expansion_tank -= 0.0000000001 * increment_value
        self.Thermostat -= 0.00001 * increment_value
