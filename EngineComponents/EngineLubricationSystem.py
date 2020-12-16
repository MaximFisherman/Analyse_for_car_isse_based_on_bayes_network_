# -*- coding: utf-8 -*-
import random
import numpy

class EngineLubricationSystem:
    # Oil and Oil filter resource capacity in km
    strenght_oil_filter = 8000
    strenght_oil = 17000
    
    list_issues = [
        'None',
        'Oil_can_on_dashboard_lights_up',
        'Oil_pressure_increase',
        'Increased_oil_consumption',
        'Engine_overheating',
        'Physical_damage_to_filter',
        'Oil_turns_black',
        'Increased_engine_noise',
        'Low_oil_level'
    ]

    def __init__(self, 
                    Oil_pump, # Масляной насос
                    Oil_filter, # Масляной фильтр
                    Oil, # Motor oil
                    Tachometer
    ):
        strength_oil_filter_wear_pecentage = (Tachometer * 100) / self.strenght_oil_filter
        strength_oil_wear_pecentage = (Tachometer * 100) / self.strenght_oil

        self.Oil_pump = Oil_pump
        self.Oil_filter = Oil_filter - strength_oil_filter_wear_pecentage
        self.Oil = Oil - strength_oil_wear_pecentage

        self.list_set = set()

    def set_zero(self, value):
        return 0.0 if value < 0.0 else value

    def get_occured_issues(self):
        common_procent_strenght = (self.Oil_pump + self.Oil_filter + self.Oil) / 3

        # print("Common strenght: ", common_procent_strenght)

        Oil_can_on_dashboard_lights_up_distribution = (self.set_zero(100 - ((((self.Oil_pump + self.Oil_filter + self.Oil) / 3) + 51))) / 100)
        Oil_pressure_increase_distribution = (self.set_zero(100 - (((self.Oil_pump) + 51))) / 100)
        Increased_oil_consumption_distribution = (self.set_zero(100 - (((self.Oil_pump) + 51))) / 100)

        Engine_overheating_distribution = (self.set_zero(100 - (((self.Oil_filter) + 60))) / 100)
        Physical_damage_to_filter_distribution = (self.set_zero(100 - (((self.Oil_filter) + 20))) / 100)
        
        Oil_turns_black_distribution = (self.set_zero(100 - (((self.Oil) + 51))) / 100)
        Increased_engine_noise_distribution = (self.set_zero(100 - (((self.Oil) + 51))) / 100)
        Low_oil_level_distribution = (self.set_zero(100 - (((self.Oil) + 51))) / 100)

        list_issues_p = [ 
            100.0,
            self.set_zero(Oil_can_on_dashboard_lights_up_distribution),
            self.set_zero(Oil_pressure_increase_distribution), 
            self.set_zero(Increased_oil_consumption_distribution), 
            self.set_zero(Engine_overheating_distribution), 
            self.set_zero(Physical_damage_to_filter_distribution),
            self.set_zero(Oil_turns_black_distribution),
            self.set_zero(Increased_engine_noise_distribution),
            self.set_zero(Low_oil_level_distribution)
        ]

        
        list_issues_p = numpy.array(list_issues_p)
        list_issues_p /= list_issues_p.sum()

        self.list_set.add(numpy.random.choice(self.list_issues, len(self.list_issues), 4, p=list_issues_p)[0])
        
        return self.list_set
        

    def run(self, increment_value):
        self.Oil_pump -= 0.0000000001 * increment_value

        if self.Oil_filter < 49 or self.Oil < 30:
            self.Oil_pump -= 0.0001 * (100 - self.Oil_filter)
            
        self.Oil_filter -= 0.0125 * increment_value
        self.Oil -= 0.0058 * increment_value