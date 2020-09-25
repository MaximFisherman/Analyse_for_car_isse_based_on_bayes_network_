# -*- coding: utf-8 -*-

class CoolingSystem:
    # Coolant pump strength value equal around 60 000 kilometers
    strenght_coolant_pump = 60000

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
    
    def run(self, increment_value):
        self.Cooling_fan -= 0.0000001 * increment_value
        self.Coolant_pump -= 0.0017 * increment_value
        self.Radiator -= 0.000000001 * increment_value
        self.Radiator_cap -= 0.00001 * increment_value
        self.Expansion_tank -= 0.0000000001 * increment_value
        self.Thermostat -= 0.00001 * increment_value
