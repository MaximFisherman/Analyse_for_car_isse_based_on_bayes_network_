#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# import pybn library
from pybn import *

  # Define a main() function.
def main():

  # Create a Network
  net = Network('CarProblem')

#################################################################################
##################################Agregate####################################
  High_pressure_pump = Node('High_pressure_pump') # (ТНВД)
  High_pressure_pump.addOutcomes(['work','not_work'])

  Fuel_filter = Node('Fuel_filter') # (Топливный фильтр)
  Fuel_filter.addOutcomes(['work','not_work'])

  Injectors = Node('Injectors') # (Форсунки)
  Injectors.addOutcomes(['work','not_work'])

  Fuel_priming_pump = Node('Fuel_priming_pump') # (Топливо подкачивающий насос)
  Fuel_priming_pump.addOutcomes(['work','not_work'])

##################################Simptoms#######################################
  Elevated_fuel_consumption = Node('Elevated_fuel_consumption') # (Повышенный расход топлива)
  Elevated_fuel_consumption.addOutcomes(['yes','no'])

  Unstable_engine_operation = Node('Unstable_engine_operation') # (Нестабильная работа двигателя)
  Unstable_engine_operation.addOutcomes(['yes','no'])

  Difficult_engine_starting = Node('Difficult_engine_starting') # (Затрудненный запуск двигателя)
  Difficult_engine_starting.addOutcomes(['yes','no'])

  Drop_in_engine_power = Node('Drop_in_engine_power') # (Падение мощности двигателя)
  Drop_in_engine_power.addOutcomes(['yes','no'])

  Increase_in_engine_smoke = Node('Increase_in_engine_smoke') # (Увеличение дымности мотора)
  Increase_in_engine_smoke.addOutcomes(['yes','no'])

  Appearance_of_oil_emulsion_in_engine_coolant = Node('Appearance_of_oil_emulsion_in_engine_coolant') # (Появление в охлаждающей жидкости двигателя масляной эмульсии)
  Appearance_of_oil_emulsion_in_engine_coolant.addOutcomes(['yes','no'])

  Increased_engine_noise = Node('Increased_engine_noise') # (Повышение шумности работы движка)
  Increased_engine_noise.addOutcomes(['yes','no']) 
  
  When_engine_speed_rises_dips_occur = Node('When_engine_speed_rises_dips_occur') # (При повышении оборотов в работе двигателя происходят провалы)
  When_engine_speed_rises_dips_occur.addOutcomes(['yes','no'])

  Fuel_leak = Node('Fuel_leak') # (Утечка топлива)
  Fuel_leak.addOutcomes(['yes','no'])

  When_car_is_running_engine_starts_to_triple = Node('When_car_is_running_engine_starts_to_triple') # (При работе автомобиля двигатель начинает троить)
  When_car_is_running_engine_starts_to_triple.addOutcomes(['yes','no'])
###################################################################################################
  # Add arc to 'Elevated_fuel_consumption'
  arc_High_pressure_pump__Elevated_fuel_consumption = Arc(High_pressure_pump, Elevated_fuel_consumption)
  arc_Fuel_filter__Elevated_fuel_consumption = Arc(Fuel_filter, Elevated_fuel_consumption)
  arc_Injectors__Elevated_fuel_consumption = Arc(Injectors, Elevated_fuel_consumption)
  arc_Fuel_priming_pump__Elevated_fuel_consumption = Arc(Fuel_priming_pump, Elevated_fuel_consumption)

  
  # Add arc to Unstable_engine_operation
  arc_High_pressure_pump__Unstable_engine_operation = Arc(High_pressure_pump, Unstable_engine_operation)
  arc_Fuel_filter__Unstable_engine_operation = Arc(Fuel_filter, Unstable_engine_operation)
  arc_Injectors__Unstable_engine_operation = Arc(Injectors, Unstable_engine_operation)
  arc_Fuel_priming_pump__Unstable_engine_operation = Arc(Fuel_priming_pump, Unstable_engine_operation)
  
  
  # Add arc to Drop_in_engine_power
  arc_High_pressure_pump__Drop_in_engine_power = Arc(High_pressure_pump, Drop_in_engine_power)
  arc_Fuel_filter__Drop_in_engine_power = Arc(Fuel_filter, Drop_in_engine_power)
  arc_Injectors__Drop_in_engine_power = Arc(Injectors, Drop_in_engine_power)
  arc_Fuel_priming_pump__Drop_in_engine_power = Arc(Fuel_priming_pump, Drop_in_engine_power)


  # Add arc to Difficult_engine_starting
  arc_High_pressure_pump__Difficult_engine_starting = Arc(High_pressure_pump, Difficult_engine_starting)
  arc_Fuel_filter__Difficult_engine_starting = Arc(Fuel_filter, Difficult_engine_starting)
  arc_Injectors__Difficult_engine_starting = Arc(Injectors, Difficult_engine_starting)
  arc_Fuel_priming_pump__Difficult_engine_starting = Arc(Fuel_priming_pump, Difficult_engine_starting)


  # Add arc to Increase_in_engine_smoke
  arc_High_pressure_pump__Increase_in_engine_smoke = Arc(High_pressure_pump, Increase_in_engine_smoke)
  arc_Fuel_filter__Increase_in_engine_smoke = Arc(Fuel_filter, Increase_in_engine_smoke)
  arc_Injectors__Increase_in_engine_smoke = Arc(Injectors, Increase_in_engine_smoke)
  arc_Fuel_priming_pump__Increase_in_engine_smoke = Arc(Fuel_priming_pump, Increase_in_engine_smoke)


  # Add arc to Appearance_of_oil_emulsion_in_engine_coolant
  arc_High_pressure_pump__Appearance_of_oil_emulsion_in_engine_coolant = Arc(High_pressure_pump, Appearance_of_oil_emulsion_in_engine_coolant)
  arc_Fuel_filter__Appearance_of_oil_emulsion_in_engine_coolant = Arc(Fuel_filter, Appearance_of_oil_emulsion_in_engine_coolant)
  arc_Injectors__Appearance_of_oil_emulsion_in_engine_coolant = Arc(Injectors, Appearance_of_oil_emulsion_in_engine_coolant)
  arc_Fuel_priming_pump__Appearance_of_oil_emulsion_in_engine_coolant = Arc(Fuel_priming_pump, Appearance_of_oil_emulsion_in_engine_coolant)


  # Add arc to Increase_in_engine_smoke
  arc_High_pressure_pump__Increased_engine_noise = Arc(High_pressure_pump, Increased_engine_noise)
  arc_Fuel_filter__Increased_engine_noisee = Arc(Fuel_filter, Increased_engine_noise)
  arc_Injectors__Increased_engine_noise = Arc(Injectors, Increased_engine_noise)
  arc_Fuel_priming_pump__Increased_engine_noise = Arc(Fuel_priming_pump, Increased_engine_noise)


  # Add arc to Increase_in_engine_smoke
  arc_High_pressure_pump__When_engine_speed_rises_dips_occur = Arc(High_pressure_pump, When_engine_speed_rises_dips_occur)
  arc_Fuel_filter__When_engine_speed_rises_dips_occur = Arc(Fuel_filter, When_engine_speed_rises_dips_occur)
  arc_Injectors__When_engine_speed_rises_dips_occur = Arc(Injectors, When_engine_speed_rises_dips_occur)
  arc_Fuel_priming_pump__When_engine_speed_rises_dips_occur = Arc(Fuel_priming_pump, When_engine_speed_rises_dips_occur)


  # Add arc to Increase_in_engine_smoke
  arc_High_pressure_pump__Fuel_leak = Arc(High_pressure_pump, Fuel_leak)
  arc_Fuel_filter__Fuel_leak = Arc(Fuel_filter, Fuel_leak)
  arc_Injectors__Fuel_leak = Arc(Injectors, Fuel_leak)
  arc_Fuel_priming_pump__Fuel_leak = Arc(Fuel_priming_pump, Fuel_leak)


  # Add arc to Increase_in_engine_smoke
  arc_High_pressure_pump__When_car_is_running_engine_starts_to_triple = Arc(High_pressure_pump, When_car_is_running_engine_starts_to_triple)
  arc_Fuel_filter__When_car_is_running_engine_starts_to_triple = Arc(Fuel_filter, When_car_is_running_engine_starts_to_triple)
  arc_Injectors__When_car_is_running_engine_starts_to_triple = Arc(Injectors, When_car_is_running_engine_starts_to_triple)
  arc_Fuel_priming_pump__When_car_is_running_engine_starts_to_triple = Arc(Fuel_priming_pump, When_car_is_running_engine_starts_to_triple)
#########################################Set probabilities################################################
  High_pressure_pump.setProbabilities([0.99,0.01])
  Fuel_filter.setProbabilities([0.99,0.01])
  Injectors.setProbabilities([0.99,0.01])
  Fuel_priming_pump.setProbabilities([0.99,0.01])

  Elevated_fuel_consumption.setProbabilities([
    0, 1,	
    0.9, 0.1,	
    0.2, 0.8,	
    0.99, 0.01,	
    0.5, 0.5,
    0.99, 0.01,
    0.99, 0.01,	
    0.99,	0.01,	
    0.2, 0.8,	
    0.99,	0.01,
    0.99,	0.01,
    0.99,	0.01,
    0.99,	0.01,
    0.99,	0.01,
    0.99,	0.01,
    0.99,	0.01,
    ])

  Unstable_engine_operation.setProbabilities([
    0.01, 0.99,	
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.99,	0.01,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  Difficult_engine_starting.setProbabilities([
    0.01, 0.99,	
    0.2, 0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.05,	0.95,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  Drop_in_engine_power.setProbabilities([
    0.01, 0.99,	
    0.01, 0.99,
    0.1, 0.9,
    0.01, 0.99,
    0.2, 0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.15,	0.85,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  Increase_in_engine_smoke.setProbabilities([
    0.01, 0.99,	
    0.3, 0.7,
    0.2, 0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.2,	0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  Appearance_of_oil_emulsion_in_engine_coolant.setProbabilities([
    0.01, 0.99,	
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.2,	0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  Increased_engine_noise.setProbabilities([
    0.01, 0.99,	
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.1, 0.9,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  When_engine_speed_rises_dips_occur.setProbabilities([
    0.01, 0.99,	
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.2, 0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  Fuel_leak.setProbabilities([
    0.01, 0.99,	
    0.2, 0.8,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])


  When_car_is_running_engine_starts_to_triple.setProbabilities([
    0.01, 0.99,	
    0.01, 0.99,
    0.2, 0.8,
    0.01, 0.99,
    0.1, 0.9,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    0.01, 0.99,
    ])

  # Changing the nodes spacial and visual attributes:
  High_pressure_pump.setNodePosition(100,10)

  Fuel_filter.setNodePosition(300,10)

  Injectors.setNodePosition(300,150)
  Injectors.setInteriorColor('ff0011')

  Fuel_priming_pump.setNodePosition(200,150)
  Fuel_priming_pump.setInteriorColor('ff0000')


  Elevated_fuel_consumption.setNodePosition(500,150)
  
  Unstable_engine_operation.setNodePosition(700,150)

  Difficult_engine_starting.setNodePosition(900,150)

  Drop_in_engine_power.setNodePosition(1000,150)

  Increase_in_engine_smoke.setNodePosition(1150,150)

  Appearance_of_oil_emulsion_in_engine_coolant.setNodePosition(1300,150)

  Increased_engine_noise.setNodePosition(1450,150)

  When_engine_speed_rises_dips_occur.setNodePosition(1600,150)

  Fuel_leak.setNodePosition(1750,150)

  When_car_is_running_engine_starts_to_triple.setNodePosition(1900,150)

  # Add notes to network
  net.addNodes([High_pressure_pump, Fuel_filter,
                Injectors,Fuel_priming_pump, Elevated_fuel_consumption, Unstable_engine_operation, Difficult_engine_starting,
                Drop_in_engine_power, Increase_in_engine_smoke, Appearance_of_oil_emulsion_in_engine_coolant, Increased_engine_noise,
                When_engine_speed_rises_dips_occur, Fuel_leak, When_car_is_running_engine_starts_to_triple])

  # Write file
  net.writeFile('CarProblem.xdsl')

  # Set evidence
  #net.setEvidence('Increased_engine_noise', 1)
  net.setEvidence('When_car_is_running_engine_starts_to_triple', 1)
  
  #net.setEvidence('Fuel_filter', 1)
  # Compute the beliefs for the network
  net.computeBeliefs()

  # Print the results for each node
  print('High_pressure_pump ', High_pressure_pump.getBeliefs())
  print('Fuel_filter ', Fuel_filter.getBeliefs())
  print('Injectors ', Injectors.getBeliefs())
  print('Fuel_priming_pump ', Fuel_priming_pump.getBeliefs())
  print('__________________________')
  print('Elevated_fuel_consumption ', Elevated_fuel_consumption.getBeliefs())
  print('Unstable_engine_operation ', Unstable_engine_operation.getBeliefs())
  print('Difficult_engine_starting ', Difficult_engine_starting.getBeliefs())
  print('Drop_in_engine_power ', Drop_in_engine_power.getBeliefs())
  print('Increase_in_engine_smoke ', Increase_in_engine_smoke.getBeliefs())
  print('Appearance_of_oil_emulsion_in_engine_coolant ', Appearance_of_oil_emulsion_in_engine_coolant.getBeliefs())
  print('Increased_engine_noise', Increased_engine_noise.getBeliefs())
  print('When_engine_speed_rises_dips_occur', When_engine_speed_rises_dips_occur.getBeliefs())
  print('Fuel_leak', Fuel_leak.getBeliefs())
  print('When_car_is_running_engine_starts_to_triple', When_car_is_running_engine_starts_to_triple.getBeliefs())
  




  # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

# python -W ignore example.py 

