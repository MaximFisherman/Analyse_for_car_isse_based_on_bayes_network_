# -*- coding: utf-8 -*-
import random
import numpy

class CrankMechanism:
    # Pistols strength value equal around 120 000 kilometers
    strength_pistons = 120000

    # First problem with Cylinder head (gasket)
    cylinder_head = 200000

    list_issues = [
        'None',
        'Drop_in_engine_power', 
        'Elevated_fuel_consumption',
        'Increased_oil_consumption', 
        'Increase_in_engine_smoke',
        'Reduced_compression_in_cylinders', 
        'Metallic_knock_is_heard_when_engine_is_running',
        'Difficult_engine_starting',
        'No_idling',
        'When_engine_speed_rises_dips_occur', 
        'Gear_shift_stiffness',
        'Vibration_when_pressing_clutch_pedal',
        'Creaking_and_grinding_noise_at_startup',
        'Physical_deformation_of_engine_block',
        'Breakage_of_thread_of_fastening_cylinder_head',
        'Leaks_in_area_of_cylinder_head_gasket',
        'Smoke_from_under_hood',
        'Antifreeze_traces_in_exhaust_system'
        ]

    def __init__(self, 
                    Pistons_1, # Поршень
                    Pistons_2,
                    Pistons_3,
                    Pistons_4,
                    Connecting_rod, # Шатун
                    Crankshaft, # Коленвал
                    Flywheel, # Маховик
                    Engine_block, # Блок
                    Cylinder_head, # Головка блока цилиндров
                    Tachometer
    ):
        # Cylinder wear percentage as indicated by the tachometer
        strength_pistons_wear_pecentage = (Tachometer * 100) / self.strength_pistons
        cylinder_head_wear_pecentage = (Tachometer * 100) / self.cylinder_head

        self.Pistons_1 = Pistons_1 - strength_pistons_wear_pecentage
        self.Pistons_2 = Pistons_2 - strength_pistons_wear_pecentage
        self.Pistons_3 = Pistons_3 - strength_pistons_wear_pecentage
        self.Pistons_4 = Pistons_4 - strength_pistons_wear_pecentage
        self.Connecting_rod = Connecting_rod
        self.Crankshaft = Crankshaft
        self.Flywheel = Flywheel
        self.Engine_block = Engine_block
        self.Cylinder_head = Cylinder_head - cylinder_head_wear_pecentage

        self.list_set = set()

    def set_zero(self, value):
        return 0.0 if value < 0.0 else value

    def get_occured_issues(self):
        common_procent_strenght = \
            (self.Pistons_1 + self.Pistons_2 + self.Pistons_3 + self.Pistons_4 + self.Connecting_rod + self.Crankshaft + \
             self.Flywheel + self.Engine_block + self.Cylinder_head) / 9
            
        common_procent_pistons_strenght = (self.Pistons_1 + self.Pistons_2 + self.Pistons_3 + self.Pistons_4) / 4
        
        # print("Common strenght: ", common_procent_strenght)
        # print("Common common_procent_pistons_strenght: ", common_procent_pistons_strenght)

        Drop_in_engine_power_distribution = (self.set_zero(100 - (((common_procent_pistons_strenght + self.Crankshaft + \
                            self.Flywheel) / 3) + 51)) / 70)

        Elevated_fuel_consumption_distribution = (self.set_zero(100 - (((common_procent_pistons_strenght) + 51))) / 70)
        Increased_oil_consumption_distribution = (self.set_zero(100 - (((common_procent_pistons_strenght) + 51))) / 70)
        Increase_in_engine_smoke_distribution = (self.set_zero(100 - (((common_procent_pistons_strenght) + 50))) / 70)
        Reduced_compression_in_cylinders_distribution = (self.set_zero(100 - (((common_procent_pistons_strenght) + 49))) / 70)
        
        Metallic_knock_is_heard_when_engine_is_running_distribution = (self.set_zero(100 - (((self.Connecting_rod) + 51))) / 100)

        Difficult_engine_starting_distribution = (self.set_zero(100 - ((((self.Crankshaft + self.Flywheel) / 2) + 51))) / 100)
        No_idling_distribution = (self.set_zero(100 - ((((self.Crankshaft + self.Flywheel) / 2) + 51))) / 100)
        When_engine_speed_rises_dips_occur_distribution = (self.set_zero(100 - (((self.Crankshaft) + 51))) / 100)

        Gear_shift_stiffness_distribution = (self.set_zero(100 - (((self.Flywheel) + 51))) / 100)
        Vibration_when_pressing_clutch_pedal_distribution = (self.set_zero(100 - (((self.Flywheel) + 51))) / 100)
        Creaking_and_grinding_noise_at_startup_distribution = (self.set_zero(100 - (((self.Flywheel) + 51))) / 100)

        Physical_deformation_of_engine_block_distribution = (self.set_zero(100 - (((self.Engine_block) + 50))) / 100)
        Breakage_of_thread_of_fastening_cylinder_head_distribution = (self.set_zero(100 - (((self.Engine_block) + 50))) / 100)

        Leaks_in_area_of_cylinder_head_gasket_distribution = (self.set_zero(100 - (((self.Cylinder_head) + 50))) / 100)
        Smoke_from_under_hood_distribution = (self.set_zero(100 - (((self.Cylinder_head) + 48))) / 100)
        When_car_is_running_engine_starts_to_triple_distribution = (self.set_zero(100 - (((self.Cylinder_head) + 51))) / 100)
        Antifreeze_traces_in_exhaust_system_distribution = (self.set_zero(100 - (((self.Cylinder_head) + 51))) / 100)
        
        list_issues_p = [ 
            100.0,
            self.set_zero(Drop_in_engine_power_distribution),
            self.set_zero(Elevated_fuel_consumption_distribution), 
            self.set_zero(Increased_oil_consumption_distribution), 
            self.set_zero(Increase_in_engine_smoke_distribution), 
            self.set_zero(Reduced_compression_in_cylinders_distribution),
            self.set_zero(Metallic_knock_is_heard_when_engine_is_running_distribution),
            self.set_zero(Difficult_engine_starting_distribution),
            self.set_zero(No_idling_distribution),
            self.set_zero(When_engine_speed_rises_dips_occur_distribution),
            self.set_zero(Gear_shift_stiffness_distribution), 
            self.set_zero(Vibration_when_pressing_clutch_pedal_distribution), 
            self.set_zero(Creaking_and_grinding_noise_at_startup_distribution), 
            self.set_zero(Physical_deformation_of_engine_block_distribution),
            self.set_zero(Breakage_of_thread_of_fastening_cylinder_head_distribution),
            self.set_zero(Leaks_in_area_of_cylinder_head_gasket_distribution), 
            self.set_zero(Smoke_from_under_hood_distribution),
            self.set_zero(Antifreeze_traces_in_exhaust_system_distribution)
            ]

        
        list_issues_p = numpy.array(list_issues_p)
        list_issues_p /= list_issues_p.sum()

        self.list_set.add(numpy.random.choice(self.list_issues, len(self.list_issues), 4, p=list_issues_p)[0])

        return self.list_set

    def run(self, increment_value):
        self.Pistons_1 -= 0.00083 * increment_value
        self.Pistons_2 -= 0.00083 * increment_value
        self.Pistons_3 -= 0.00083 * increment_value
        self.Pistons_4 -= 0.00083 * increment_value

        if self.Pistons_1 < 30:
            self.Engine_block -= 0.0001 * (100 - self.Pistons_1)
            self.Connecting_rod -= 0.0001 * (100 - self.Pistons_1)
            self.Crankshaft -= 0.000001 * (100 - self.Pistons_1)

        if self.Engine_block < 20:
            self.Flywheel -= 0.000001 * (100 - self.Engine_block)

        self.Connecting_rod -= 0.0000000000000001 * increment_value
        self.Crankshaft -= 0.0000000000000001 * increment_value
        self.Flywheel -= 0.0000000000000001 * increment_value
        self.Engine_block -= 0.0000000000000001 * increment_value
        self.Cylinder_head -= 0.0005 * increment_value

