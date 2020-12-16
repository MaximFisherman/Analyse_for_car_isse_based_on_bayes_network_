# -*- coding: utf-8 -*-

from EngineComponents.CrankMechanism import CrankMechanism
from EngineComponents.GasDistributionMechanism import GasDistributionMechanism
from EngineComponents.CoolingSystem import CoolingSystem
from EngineComponents.EngineLubricationSystem import EngineLubricationSystem
from EngineComponents.FuelSystem import FuelSystem

from Libraries.Object_maker import Object_maker

from prettytable import PrettyTable

import os
import sys
import time
import socket
import threading 

class Engine:
    def __init__(self, CrankMechanism):
        self.CrankMechanism = CrankMechanism

    def getDegreeOfWear():
        pass 

def main():
    def clear(): os.system('cls')

    tachometer = 53000
    periodic_sender_counter = 10
    iteration_counter = 0

    crank = CrankMechanism(100,100,100,100,100,100,100,100,100, tachometer)
    gasDistribution = GasDistributionMechanism(100,100,100,100,100,100,100,100,100,100,100, tachometer)
    coolingSystem = CoolingSystem(100,100,100,100,100,100, tachometer)
    engineLubricationSystem = EngineLubricationSystem(100,100,100,tachometer)
    fuelSystem = FuelSystem(100,100,100,100,tachometer)
    
    prettyTable = PrettyTable()

    prettyTable.field_names = ["Crank mechanism", "Value    ", " ", "Gas Distribution Mechanism", "Value     ", 
                               "  ", "Cooling System", "Value         ", "     ", "Engine Lubrication System", "Value            ", "   ", "Fuel System", "Value             "]
    
    list_issues = set()


    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('Connecting to {} port {}'.format(server_address[0], server_address[1]), file=sys.stderr) 
    sock.connect(server_address)


    try:
        while True:
            prettyTable.add_row(["Pistons 1", round(crank.Pistons_1, 2), "-", "Valve 1" , round(gasDistribution.Valve_1, 2), "-", "Cooling fan", round(coolingSystem.Cooling_fan, 2), "-", "Oil pump", round(engineLubricationSystem.Oil_pump, 2), "-", "High pressure fuel pump", round(fuelSystem.High_pressure_fuel_pump, 2)])
            prettyTable.add_row(["Pistons 2", round(crank.Pistons_2, 2), "-", "Valve 2" , round(gasDistribution.Valve_1, 2), "-", "Coolant pump", round(coolingSystem.Coolant_pump, 2), "-", "Oil filter", round(engineLubricationSystem.Oil_filter, 2), "-", "Fuel filter", round(fuelSystem.Fuel_filter, 2)])
            prettyTable.add_row(["Pistons 3", round(crank.Pistons_3, 2), "-", "Valve 3" , round(gasDistribution.Valve_1, 2), "-", "Radiator", round(coolingSystem.Radiator, 2), "-", "Oil", round(engineLubricationSystem.Oil, 2), "-", "Injectors", round(fuelSystem.Injectors, 2)])
            prettyTable.add_row(["Pistons 4", round(crank.Pistons_4, 2), "-", "Valve 4" , round(gasDistribution.Valve_1, 2), "-", "Radiator cap", round(coolingSystem.Radiator_cap, 2), "-", "-", "-", "-", "Fuel priming pump", round(fuelSystem.Fuel_priming_pump, 2)])
            prettyTable.add_row(["Connecting rod", round(crank.Connecting_rod, 2), "-", "Valve 5" , round(gasDistribution.Valve_1, 2), "-", "Expansion tank", round(coolingSystem.Expansion_tank, 2), "-", "-", "-", "-", "-", "-"])
            prettyTable.add_row(["Crankshaft", round(crank.Crankshaft, 2), "-", "Valve 6" , round(gasDistribution.Valve_1, 2), "-", "Thermostat", round(coolingSystem.Thermostat, 2), "-", "-", "-", "-","-", "-",])
            prettyTable.add_row(["Flywheel", round(crank.Flywheel, 2), "-", "Valve 7" , round(gasDistribution.Valve_1, 2), "-", "-", "-", "-", "-", "-", "-", "-", "-"])
            prettyTable.add_row(["Engine block", round(crank.Engine_block, 2), "-", "Valve 8" , round(gasDistribution.Valve_1, 2), "-", "-", "-", "-", "-", "-", "-", "-", "-"])
            prettyTable.add_row(["Cylinder head", round(crank.Cylinder_head, 2), "-", "Valve drive" , round(gasDistribution.Valve_drive, 2), "-", "-", "-", "-", "-", "-", "-", "-", "-"])
            prettyTable.add_row(["-", "-", "-", "Camshaft" , round(gasDistribution.Camshaft, 2), "-", "-", "-", "-", "-","-", "-","-", "-"])
            prettyTable.add_row(["-", "-", "-", "Shaft drive" , round(gasDistribution.Shaft_drive, 2), "-", "-", "-", "-", "-", "-", "-", "-", "-",])

            
            print("tachometer: " + str(tachometer) + " km\n")
            print(prettyTable)
            
            # print(gasDistribution.get_occured_issues())
            # print(crank.get_occured_issues())
            # print(coolingSystem.get_occured_issues())
            # print(engineLubricationSystem.get_occured_issues())
            # print(fuelSystem.get_occured_issues())

            list_issues.update(gasDistribution.get_occured_issues())
            list_issues.update(crank.get_occured_issues())
            list_issues.update(coolingSystem.get_occured_issues())
            list_issues.update(engineLubricationSystem.get_occured_issues())
            list_issues.update(fuelSystem.get_occured_issues())

            print(list_issues)


            ################################################################
            ###################Send data to Bayes network###################
            if iteration_counter > periodic_sender_counter:
                # Send data
                obj = Object_maker(list_issues) 

                message = obj.format()
                print('Sending "{}"'.format(message),file=sys.stderr)
                sock.sendall(message)

                # Look for the response
                amount_received = 0
                amount_expected = len(message)
                
                # For syhronic sending message to Host
                while amount_received < amount_expected:
                    data = sock.recv(4096)
                    amount_received += len(data)
                    print('Received "{}"'.format(data),file=sys.stderr)
                
                iteration_counter = 0
            ################################################################
            ################################################################

            increment_value = 1
            tachometer += increment_value
            
            crank.run(increment_value)
            gasDistribution.run(increment_value)
            coolingSystem.run(increment_value)
            engineLubricationSystem.run(increment_value)
            fuelSystem.run(increment_value)

            time.sleep(0.1)
            clear()
            prettyTable.clear_rows()
            iteration_counter += 1
    finally:
        print('Closing socket', file=sys.stderr)
        sock.close()
        
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