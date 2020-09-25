# -*- coding: utf-8 -*-

class EngineLubricationSystem:
    # Oil and Oil filter resource capacity in km
    strenght_oil_filter = 8000
    strenght_oil = 17000

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

    def run(self, increment_value):
        self.Oil_pump -= 0.0000000001 * increment_value
        self.Oil_filter -= 0.0125 * increment_value
        self.Oil -= 0.0058 * increment_value