# -*- coding: utf-8 -*-

class CrankMechanism:
    # Pistols strength value equal around 120 000 kilometers
    strength_pistons = 120000

    # First problem with Cylinder head (gasket)
    cylinder_head = 200000

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


    def get_occured_issues(self):
        return self.list_set

    def run(self, increment_value):
        self.Pistons_1 -= 0.00083 * increment_value
        self.Pistons_2 -= 0.00083 * increment_value
        self.Pistons_3 -= 0.00083 * increment_value
        self.Pistons_4 -= 0.00083 * increment_value
        self.Connecting_rod -= 0.0000000000000001 * increment_value
        self.Crankshaft -= 0.0000000000000001 * increment_value
        self.Flywheel -= 0.0000000000000001 * increment_value
        self.Engine_block -= 0.0000000000000001 * increment_value
        self.Cylinder_head -= 0.0005 * increment_value

