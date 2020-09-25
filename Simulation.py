# -*- coding: utf-8 -*-

from EngineComponents.CrankMechanism import CrankMechanism
from EngineComponents.GasDistributionMechanism import GasDistributionMechanism
from EngineComponents.CoolingSystem import CoolingSystem
from EngineComponents.EngineLubricationSystem import EngineLubricationSystem
from EngineComponents.FuelSystem import FuelSystem

from prettytable import PrettyTable

import os
import time
import threading


class Engine:
    def __init__(self, CrankMechanism):
        self.CrankMechanism = CrankMechanism

    def getDegreeOfWear():
        pass 

def main():
    def clear(): os.system('cls')

    tachometer = 0
    
    crank = CrankMechanism(100,100,100,100,100,100,100,100,100, tachometer)
    gasDistribution = GasDistributionMechanism(100,100,100,100,100,100,100,100,100,100,100, tachometer)
    coolingSystem = CoolingSystem(100,100,100,100,100,100, tachometer)
    engineLubricationSystem = EngineLubricationSystem(100,100,100,tachometer)
    fuelSystem = FuelSystem(100,100,100,100,tachometer)
    
    prettyTable = PrettyTable()

    prettyTable.field_names = ["Crank mechanism", "Value    ", " ", "Gas Distribution Mechanism", "Value     ", 
                               "  ", "Cooling System", "Value         ", "     ", "Engine Lubrication System", "Value            ", "   ", "Fuel System", "Value             "]
    

    while True:
        prettyTable.add_row(["Pistons 1", crank.Pistons_1, "-", "Valve 1" , gasDistribution.Valve_1, "-", "Cooling fan", coolingSystem.Cooling_fan, "-", "Oil pump", engineLubricationSystem.Oil_pump, "-", "High pressure fuel pump", fuelSystem.High_pressure_fuel_pump])
        prettyTable.add_row(["Pistons 2", crank.Pistons_2, "-", "Valve 2" , gasDistribution.Valve_1, "-", "Coolant pump", coolingSystem.Coolant_pump, "-", "Oil filter", engineLubricationSystem.Oil_filter, "-", "Fuel filter", fuelSystem.Fuel_filter])
        prettyTable.add_row(["Pistons 3", crank.Pistons_3, "-", "Valve 3" , gasDistribution.Valve_1, "-", "Radiator", coolingSystem.Radiator, "-", "Oil", engineLubricationSystem.Oil, "-", "Injectors", fuelSystem.Injectors])
        prettyTable.add_row(["Pistons 4", crank.Pistons_4, "-", "Valve 4" , gasDistribution.Valve_1, "-", "Radiator cap", coolingSystem.Radiator_cap, "-", "-", "-", "-", "Fuel priming pump", fuelSystem.Fuel_priming_pump])
        prettyTable.add_row(["Connecting rod", crank.Connecting_rod, "-", "Valve 5" , gasDistribution.Valve_1, "-", "Expansion tank", coolingSystem.Expansion_tank, "-", "-", "-", "-", "-", "-"])
        prettyTable.add_row(["Crankshaft", crank.Crankshaft, "-", "Valve 6" , gasDistribution.Valve_1, "-", "Thermostat", coolingSystem.Thermostat, "-", "-", "-", "-","-", "-",])
        prettyTable.add_row(["Flywheel", crank.Flywheel, "-", "Valve 7" , gasDistribution.Valve_1, "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        prettyTable.add_row(["Engine block", crank.Engine_block, "-", "Valve 8" , gasDistribution.Valve_1, "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        prettyTable.add_row(["Cylinder head", crank.Cylinder_head, "-", "Valve drive" , gasDistribution.Valve_drive, "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        prettyTable.add_row(["-", "-", "-", "Camshaft" , gasDistribution.Camshaft, "-", "-", "-", "-", "-","-", "-","-", "-"])
        prettyTable.add_row(["-", "-", "-", "Shaft drive" , gasDistribution.Shaft_drive, "-", "-", "-", "-", "-", "-", "-", "-", "-",])

        
        print "tachometer: " + str(tachometer) + " km\n"
        print(prettyTable)


        increment_value = 105
        tachometer += increment_value
        
        crank.run(increment_value)
        gasDistribution.run(increment_value)
        coolingSystem.run(increment_value)
        engineLubricationSystem.run(increment_value)
        fuelSystem.run(increment_value)

        time.sleep(0.1)
        clear()
        prettyTable.clear_rows()

if __name__ == '__main__':
    main()


#E:\Python27\python.exe Simulation.py



        # print "tachometer: " + str(tachometer) + " km\n"
        # print "Crank mechanism"
        # print "   Pistons 1:" + str(crank.Pistons_1)
        # print "   Pistons 2:" + str(crank.Pistons_2)
        # print "   Pistons 3:" + str(crank.Pistons_3)
        # print "   Pistons 4:" + str(crank.Pistons_4)
        # print "   Connecting rod:" + str(crank.Connecting_rod)
        # print "   Crankshaft:" + str(crank.Crankshaft)
        # print "   Flywheel:" + str(crank.Flywheel)
        # print "   Engine block:" + str(crank.Engine_block)
        # print "   Cylinder head:" + str(crank.Cylinder_head)
        # print "-------------------------------------------\n"
        # print "Gas Distribution Mechanism"
        # print "   Valve 1:" + str(gasDistribution.Valve_1)
        # print "   Valve 2:" + str(gasDistribution.Valve_2)
        # print "   Valve 3:" + str(gasDistribution.Valve_3)
        # print "   Valve 4:" + str(gasDistribution.Valve_4)
        # print "   Valve 5:" + str(gasDistribution.Valve_5)
        # print "   Valve 6:" + str(gasDistribution.Valve_6)
        # print "   Valve 7:" + str(gasDistribution.Valve_7)
        # print "   Valve 8:" + str(gasDistribution.Valve_8)
        # print "   Valve drive:" + str(gasDistribution.Valve_drive)
        # print "   Camshaft:" + str(gasDistribution.Camshaft)
        # print "   Shaft_drive:" + str(gasDistribution.Shaft_drive)
        # print "-------------------------------------------\n"
        # print "Cooling System"
        # print "   Cooling fan:" + str(coolingSystem.Cooling_fan)
        # print "   Coolant pump:" + str(coolingSystem.Coolant_pump)
        # print "   Radiator:" + str(coolingSystem.Radiator)
        # print "   Radiator cap:" + str(coolingSystem.Radiator_cap)
        # print "   Expansion tank:" + str(coolingSystem.Expansion_tank)
        # print "   Thermostat:" + str(coolingSystem.Thermostat)