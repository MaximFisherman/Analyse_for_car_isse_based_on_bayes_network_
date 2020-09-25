# -*- coding: utf-8 -*-

class GasDistributionMechanism:
    # Valve strength value equal around 100 000 kilometers
    strength_valve = 100000

    # Valve drive strength value equal around 70 000 kilometers
    strenght_valve_drive = 70000

    # Сamshaft strength value equal around 80 000 kilometers
    strenght_camshaft = 80000

    def __init__(self, 
                    Valve_1, # Клапана
                    Valve_2,
                    Valve_3,
                    Valve_4,
                    Valve_5,
                    Valve_6,
                    Valve_7,
                    Valve_8,
                    Valve_drive, # Привод клапанов
                    Camshaft, # Распределительный вал
                    Shaft_drive, # Привод вала
                    Tachometer
    ):
        # Valve wear percentage as indicated by the tachometer
        strength_valve_wear_pecentage = (Tachometer * 100) / self.strength_valve
        strength_valve_drive_wear_pecentage = (Tachometer * 100) / self.strenght_valve_drive
        strength_camshaft_wear_pecentage = (Tachometer * 100) / self.strenght_camshaft

        self.Valve_1 = Valve_1 - strength_valve_wear_pecentage
        self.Valve_2 = Valve_2 - strength_valve_wear_pecentage
        self.Valve_3 = Valve_3 - strength_valve_wear_pecentage
        self.Valve_4 = Valve_4 - strength_valve_wear_pecentage
        self.Valve_5 = Valve_5 - strength_valve_wear_pecentage
        self.Valve_6 = Valve_6 - strength_valve_wear_pecentage
        self.Valve_7 = Valve_7 - strength_valve_wear_pecentage
        self.Valve_8 = Valve_8 - strength_valve_wear_pecentage
        self.Valve_drive = Valve_drive - strength_valve_drive_wear_pecentage
        self.Camshaft = Camshaft - strength_camshaft_wear_pecentage
        self.Shaft_drive = Shaft_drive
    
    def run(self, increment_value):
        self.Valve_1 -= 0.001 * increment_value
        self.Valve_2 -= 0.001 * increment_value
        self.Valve_3 -= 0.001 * increment_value
        self.Valve_4 -= 0.001 * increment_value
        self.Valve_5 -= 0.001 * increment_value
        self.Valve_6 -= 0.001 * increment_value
        self.Valve_7 -= 0.001 * increment_value
        self.Valve_8 -= 0.001 * increment_value
        self.Valve_drive -= 0.0014 * increment_value
        self.Camshaft -= 0.00125 * increment_value
        self.Shaft_drive -= 0.00000000000000001 * increment_value