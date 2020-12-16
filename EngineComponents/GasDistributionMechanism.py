# -*- coding: utf-8 -*-
import random
import numpy

class GasDistributionMechanism:
    """
        Class represents gas destribution mechanism which used in Simulation

    constants:
        STRENGTH_VALVE (int): Valve strength value equal around 100 000 kilometers
        STRENGHT_VALVE_DRIVE (int): Valve drive strength value equal around 70 000 kilometers
        STRENGHT_CAMSHAFT (int): Сamshaft strength value equal around 80 000 kilometers

    variables:
        list_issues (string[]): list of issues which possible occures
    """

    STRENGTH_VALVE = 100000
    STRENGHT_VALVE_DRIVE = 70000
    STRENGHT_CAMSHAFT = 80000

    list_issues = [
        'None',
        'When_car_is_running_engine_starts_to_triple', 
        'Drop_in_engine_power',
        'Pops_are_heard_in_exhaust_pipe', 
        'Exhaust_color_gray_black', 
        'Candle_deposits', 
        'Leaks_in_area_of_cylinder_head_gasket',
        'When_engine_speed_rises_dips_occur',
        'Leaking_in_camshaft_oil_seal_area', 
        'Timing_Belt_Problems',
        'Increased_engine_noise'
        ]


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
        strength_valve_wear_pecentage = (Tachometer * 100) / self.STRENGTH_VALVE
        strength_valve_drive_wear_pecentage = (Tachometer * 100) / self.STRENGHT_VALVE_DRIVE
        strength_camshaft_wear_pecentage = (Tachometer * 100) / self.STRENGHT_CAMSHAFT

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

        self.list_set = set()
    
    def set_zero(self, value):
        return 0.0 if value < 0.0 else value
        
    def get_occured_issues(self):
        
        common_procent_strenght = \
            (self.Valve_1 + self.Valve_2 + self.Valve_3 + self.Valve_4 + self.Valve_5 + self.Valve_6 + \
             self.Valve_7 + self.Valve_8 + self.Valve_drive + self.Camshaft + self.Shaft_drive) / 11

        common_procent_valve_strenght = \
            (self.Valve_1 + self.Valve_2 + self.Valve_3 + self.Valve_4 + self.Valve_5 + self.Valve_6 + \
             self.Valve_7 + self.Valve_8) / 8
        
        # print("Occurs common strenght procent ", common_procent_strenght)
        # print("Occurs common valve drive procent ", (common_procent_valve_strenght + self.Valve_drive) / 2)
        
        When_car_is_running_engine_starts_to_triple_distribution = (self.set_zero(100 - \
            (((common_procent_valve_strenght + self.Valve_drive) / 2) + 51)) / 100)
        Drop_in_engine_power_distribution = (self.set_zero(100 - \
            (((common_procent_valve_strenght + self.Valve_drive + self.Camshaft) / 3) + 51)) / 100)
        Pops_are_heard_in_exhaust_pipe_distribution = (self.set_zero(100 - (common_procent_valve_strenght + 50)) / 100)
        
        Exhaust_color_gray_black_distribution = (self.set_zero(100 - \
            (self.Valve_drive + 45)) / 100)
        Candle_deposits_distribution = (self.set_zero(100 - \
            (self.Valve_drive + 45)) / 100)
        Leaks_in_area_of_cylinder_head_gasket_distribution = (self.set_zero(100 - \
            ((self.Valve_drive) + 51)) / 100)
        When_engine_speed_rises_dips_occur_distribution = (self.set_zero(100 - \
            (((self.Valve_drive + self.Camshaft) / 2) + 51)) / 100)
        
        Leaking_in_camshaft_oil_seal_area_distribution = (self.set_zero(100 - \
            ((self.Camshaft) + 51)) / 100)

        Timing_Belt_Problems_distribution = (self.set_zero(100 - \
            ((self.Shaft_drive) + 51)) / 100)
        Increased_engine_noise_distribution = (self.set_zero(100 - \
            ((self.Shaft_drive) + 51)) / 100)

        # print("Occurs common Timing_Belt_Problems_distribution ", Timing_Belt_Problems_distribution)
        # print("Occurs common Timing_Belt_Problems_distribution ", 100 - ((self.Valve_drive) + 51))
        list_issues_p = [ 
            100.0,
            self.set_zero(When_car_is_running_engine_starts_to_triple_distribution), 
            self.set_zero(Drop_in_engine_power_distribution), 
            self.set_zero(Pops_are_heard_in_exhaust_pipe_distribution), 
            self.set_zero(Exhaust_color_gray_black_distribution),
            self.set_zero(Candle_deposits_distribution), 
            self.set_zero(Leaks_in_area_of_cylinder_head_gasket_distribution), 
            self.set_zero(When_engine_speed_rises_dips_occur_distribution), 
            self.set_zero(Leaking_in_camshaft_oil_seal_area_distribution), 
            self.set_zero(Timing_Belt_Problems_distribution),
            self.set_zero(Increased_engine_noise_distribution)
            ]

        list_issues_p = numpy.array(list_issues_p)
        list_issues_p /= list_issues_p.sum()

        self.list_set.add(numpy.random.choice(self.list_issues, len(self.list_issues), 4, p=list_issues_p)[0])


        return self.list_set

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

        if self.Valve_drive < 49:
            self.Valve_1 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_2 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_3 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_4 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_5 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_6 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_7 -= 0.001 * (100 - self.Valve_drive)
            self.Valve_8 -= 0.001 * (100 - self.Valve_drive)
        
        self.Camshaft -= 0.00125 * increment_value

        if self.Camshaft < 50: 
            self.Shaft_drive -= 0.001 * (100 - self.Valve_drive)
        self.Shaft_drive -= 0.00000000000000001 * increment_value