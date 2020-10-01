#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# import pybn library
from pybn import *

def get_probabilities_by_component(name):
  """
    Make possible get value of probabilities by system component 
    
    Parameters
    ----------
    name : string
      Name of device which probabilities what want to get.
  """
  return_list = []

  with open ("BayesianDataForEngineComponents\\" + str(name) + ".txt") as myfile:
    for line in myfile:
      for number in line.split(','):
        if number.replace('.','',1).isdigit():
          return_list.append(float(number))
  return return_list

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


  Oil_pump = Node('Oil_pump') # (Масляной насос)
  Oil_pump.addOutcomes(['work','not_work'])

  Oil_filter = Node('Oil_filter') # (Масляной фильтр)
  Oil_filter.addOutcomes(['work','not_work'])

  Engine_oil = Node('Engine_oil') # (Моторное масло)
  Engine_oil.addOutcomes(['work','not_work'])


  Cooling_fan = Node('Cooling_fan') # (Вентилятор радиатора)
  Cooling_fan.addOutcomes(['work','not_work'])

  Coolant_pump = Node('Coolant_pump') # (Насос системы охлаждения)
  Coolant_pump.addOutcomes(['work','not_work'])

  Radiator = Node('Radiator') # (Радиатор)
  Radiator.addOutcomes(['work','not_work'])

  Radiator_cap = Node('Radiator_cap') # (Крышка радиатора)
  Radiator_cap.addOutcomes(['work','not_work'])

  Expansion_tank = Node('Expansion_tank') # (Расширительный бачок)
  Expansion_tank.addOutcomes(['work','not_work'])
  
  Thermostat = Node('Thermostat') # (Термостат)
  Thermostat.addOutcomes(['work','not_work'])
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


  Oil_can_on_dashboard_lights_up = Node('Oil_can_on_dashboard_lights_up') # (Загораеться масленка на приборной панели)
  Oil_can_on_dashboard_lights_up.addOutcomes(['yes','no'])  
  
  Oil_pressure_increase = Node('Oil_pressure_increase') # (Повышенное давление масла)
  Oil_pressure_increase.addOutcomes(['yes','no'])

  Increased_oil_consumption = Node('Increased_oil_consumption') # (Увеличенный расход масла)
  Increased_oil_consumption.addOutcomes(['yes','no'])

  Engine_overheating = Node('Engine_overheating') # (Перегрев двигателя)
  Engine_overheating.addOutcomes(['yes','no'])

  Physical_damage_to_filter = Node('Physical_damage_to_filter') # (Физические повреждения фильтра)
  Physical_damage_to_filter.addOutcomes(['yes','no'])

  Oil_turns_black = Node('Oil_turns_black') # (Масло чернеет)
  Oil_turns_black.addOutcomes(['yes','no'])

  Low_oil_level = Node('Low_oil_level') # (Низкий уровень масла)
  Low_oil_level.addOutcomes(['yes','no'])


  Cooling_fan_does_not_turn_on = Node('Cooling_fan_does_not_turn_on') # (Не включаеться вентилятор радиатора)
  Cooling_fan_does_not_turn_on.addOutcomes(['yes','no'])

  Cooling_fan_does_not_turn_off = Node('Cooling_fan_does_not_turn_off') # (Не выключается вентилятор радиатора)
  Cooling_fan_does_not_turn_off.addOutcomes(['yes','no'])

  Cooling_fan_external_damage = Node('Cooling_fan_external_damage') # (Внешние повреждения вентилятора радиатора)
  Cooling_fan_external_damage.addOutcomes(['yes','no'])

  Cooling_pump_pulley_play = Node('Cooling_pump_pulley_play') # (Насос системы охлаждения)
  Cooling_pump_pulley_play.addOutcomes(['yes','no'])

  Antifreeze_leakage_under_car = Node('Antifreeze_leakage_under_car') # (Появление течи антифриза под автомобилем)
  Antifreeze_leakage_under_car.addOutcomes(['yes','no'])

  Appearance_of_pungent_smell_of_antifreeze_in_car = Node('Appearance_of_pungent_smell_of_antifreeze_in_car') # (Появление в салоне автомобиля резкого запаха антифриза)
  Appearance_of_pungent_smell_of_antifreeze_in_car.addOutcomes(['yes','no'])

  Interior_heating_problems = Node('Interior_heating_problems') # (Проблемы с обогревом салона)
  Interior_heating_problems.addOutcomes(['yes','no'])
  
  Damaged_cylinder_head_gasket = Node('Damaged_cylinder_head_gasket') # (Повреждение прокладки головки блока цилиндров)
  Damaged_cylinder_head_gasket.addOutcomes(['yes','no'])

  Relief_valve_plunger_sticking = Node('Relief_valve_plunger_sticking') # (Плунжер перепускного клапана заедает)
  Relief_valve_plunger_sticking.addOutcomes(['work','not_work'])

  Loose_radiator_cap_spring = Node('Loose_radiator_cap_spring') # (Ослабление пружины крышки радиатора)
  Loose_radiator_cap_spring.addOutcomes(['work','not_work'])
  
  Smoke_from_under_hood = Node('Smoke_from_under_hood') # (Дым из-под капота)
  Smoke_from_under_hood.addOutcomes(['work','not_work'])

  White_steam_from_muffler = Node('White_steam_from_muffler') # (Белый пар из глушителя)
  White_steam_from_muffler.addOutcomes(['work','not_work'])

  Fan_turns_on_ahead_of_time = Node('Fan_turns_on_ahead_of_time') # (Вентилятор охлаждения включается раньше времени)
  Fan_turns_on_ahead_of_time.addOutcomes(['work','not_work'])

  Engine_takes_long_time_to_reach_operating_temperature = Node('Engine_takes_long_time_to_reach_operating_temperature') # (Двигатель долго нагреваеться до робочей температуры)
  Engine_takes_long_time_to_reach_operating_temperature.addOutcomes(['work','not_work'])

  Fluctuations_in_engine_temperature_while_driving = Node('Fluctuations_in_engine_temperature_while_driving') # (Колебания температуры двигателя при движении)
  Fluctuations_in_engine_temperature_while_driving.addOutcomes(['work','not_work'])
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


  # Add arc to Increased_engine_noise
  arc_High_pressure_pump__Increased_engine_noise = Arc(High_pressure_pump, Increased_engine_noise)
  arc_Fuel_filter__Increased_engine_noisee = Arc(Fuel_filter, Increased_engine_noise)
  arc_Injectors__Increased_engine_noise = Arc(Injectors, Increased_engine_noise)
  arc_Fuel_priming_pump__Increased_engine_noise = Arc(Fuel_priming_pump, Increased_engine_noise)
  arc_Engine_oil__Increased_engine_noise = Arc(Engine_oil, Increased_engine_noise)

  # Add arc to When_engine_speed_rises_dips_occur
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



  # Add arc to Oil_can_on_dashboard_lights_up
  arc_Oil_pump__Oil_can_on_dashboard_lights_up = Arc(Oil_pump, Oil_can_on_dashboard_lights_up)
  arc_Oil_filter__Oil_can_on_dashboard_lights_up = Arc(Oil_filter, Oil_can_on_dashboard_lights_up)
  arc_Engine_oil__Oil_can_on_dashboard_lights_up = Arc(Engine_oil, Oil_can_on_dashboard_lights_up)
  
  # Add arc to Oil_pressure_increas
  arc_Oil_pump__Oil_pressure_increase = Arc(Oil_pump, Oil_pressure_increase)
  arc_Oil_filter__Oil_pressure_increase = Arc(Oil_filter, Oil_pressure_increase)
  arc_Engine_oil__Oil_pressure_increase = Arc(Engine_oil, Oil_pressure_increase)

  # Add arc to Increased_oil_consumption
  arc_Oil_pump__Increased_oil_consumption = Arc(Oil_pump, Increased_oil_consumption)
  arc_Oil_filter__Increased_oil_consumption = Arc(Oil_filter, Increased_oil_consumption)
  arc_Engine_oil__Increased_oil_consumption = Arc(Engine_oil, Increased_oil_consumption)

  # Add arc to Engine_overheating
  arc_Oil_filter__Engine_overheating = Arc(Oil_filter, Engine_overheating)
  
  # Add arc to Physical_damage_to_filter
  arc_Oil_pump__Physical_damage_to_filter = Arc(Oil_pump, Physical_damage_to_filter)
  arc_Oil_filter__Physical_damage_to_filter = Arc(Oil_filter, Physical_damage_to_filter)
  arc_Engine_oil__Physical_damage_to_filter = Arc(Engine_oil, Physical_damage_to_filter)

  # Add arc to Oil_turns_black
  arc_Oil_pump__Oil_turns_black = Arc(Oil_pump, Oil_turns_black)
  arc_Oil_filter__Oil_turns_black = Arc(Oil_filter, Oil_turns_black)
  arc_Engine_oil__Oil_turns_black = Arc(Engine_oil, Oil_turns_black)
  
  # Add arc to Low_oil_level
  arc_Oil_pump__Low_oil_level = Arc(Oil_pump, Low_oil_level)
  arc_Oil_filter__Low_oil_level = Arc(Oil_filter, Low_oil_level)
  arc_Engine_oil__Low_oil_level = Arc(Engine_oil, Low_oil_level)



  # Add arc Cooling_fan_does_not_turn_on
  arc_Cooling_fan__Cooling_fan_does_not_turn_on = Arc(Cooling_fan, Cooling_fan_does_not_turn_on)
  arc_Thermostat__Cooling_fan_does_not_turn_on = Arc(Thermostat, Cooling_fan_does_not_turn_on)

  # Add arc Cooling_fan_does_not_turn_off
  arc_Cooling_fan__Cooling_fan_does_not_turn_off = Arc(Cooling_fan, Cooling_fan_does_not_turn_off)
  arc_Thermostat__Cooling_fan_does_not_turn_off = Arc(Thermostat, Cooling_fan_does_not_turn_off)

  # Add arc Cooling_fan_external_damage
  arc_Cooling_fan__Cooling_fan_external_damage = Arc(Cooling_fan, Cooling_fan_external_damage)
  arc_Thermostat__Cooling_fan_external_damage = Arc(Thermostat, Cooling_fan_external_damage)
  
  # Add arc Cooling_pump_pulley_play
  arc_Cooling_fan__Cooling_pump_pulley_play = Arc(Coolant_pump, Cooling_pump_pulley_play)

  # Add arc Antifreeze_leakage_under_car
  arc_Cooling_fan__Antifreeze_leakage_under_car = Arc(Coolant_pump, Antifreeze_leakage_under_car)
  arc_Radiator__Antifreeze_leakage_under_car = Arc(Radiator, Antifreeze_leakage_under_car)

  # Add arc Appearance_of_pungent_smell_of_antifreeze_in_car
  arc_Cooling_fan__Appearance_of_pungent_smell_of_antifreeze_in_car = Arc(Coolant_pump, Appearance_of_pungent_smell_of_antifreeze_in_car)
  
  # Add arc Interior_heating_problems
  arc_Radiator__Interior_heating_problems = Arc(Radiator, Interior_heating_problems)
  
  # Add arc Damaged_cylinder_head_gasket
  arc_Radiator__Damaged_cylinder_head_gasket = Arc(Radiator, Damaged_cylinder_head_gasket)

  # Add arc Relief_valve_plunger_sticking
  arc_Radiator_cap__Relief_valve_plunger_sticking = Arc(Radiator_cap, Relief_valve_plunger_sticking)
  
  # Add arc Relief_valve_plunger_sticking
  arc_Radiator_cap__Loose_radiator_cap_spring = Arc(Radiator_cap, Loose_radiator_cap_spring)
  
  # Add arc Relief_valve_plunger_sticking
  arc_Expansion_tank__Smoke_from_under_hood = Arc(Expansion_tank, Smoke_from_under_hood)

  # Add arc White_steam_from_muffler
  arc_Expansion_tank__White_steam_from_muffler = Arc(Expansion_tank, White_steam_from_muffler)
  
  # Add arc Fan_turns_on_ahead_of_time
  arc_Thermostat__Fan_turns_on_ahead_of_time = Arc(Thermostat, Fan_turns_on_ahead_of_time)

  # Add arc Engine_takes_long_time_to_reach_operating_temperature
  arc_Thermostat__Engine_takes_long_time_to_reach_operating_temperature = Arc(Thermostat, Engine_takes_long_time_to_reach_operating_temperature)
  
  # Add arc Engine_takes_long_time_to_reach_operating_temperature
  arc_Thermostat__Fluctuations_in_engine_temperature_while_driving = Arc(Thermostat, Fluctuations_in_engine_temperature_while_driving)
#########################################Set probabilities################################################
  High_pressure_pump.setProbabilities([0.99,0.01])
  Fuel_filter.setProbabilities([0.99,0.01])
  Injectors.setProbabilities([0.99,0.01])
  Fuel_priming_pump.setProbabilities([0.99,0.01])
  Oil_pump.setProbabilities([0.99,0.01])
  Oil_filter.setProbabilities([0.99,0.01])
  Engine_oil.setProbabilities([0.99,0.01])
  Cooling_fan.setProbabilities([0.99,0.01])
  Coolant_pump.setProbabilities([0.99,0.01])
  Radiator.setProbabilities([0.99,0.01])
  Radiator_cap.setProbabilities([0.99,0.01])
  Expansion_tank.setProbabilities([0.99,0.01])
  Thermostat.setProbabilities([0.99,0.01])
  
  Elevated_fuel_consumption.setProbabilities(
    get_probabilities_by_component("Elevated_fuel_consumption"))

  Unstable_engine_operation.setProbabilities(
    get_probabilities_by_component("Unstable_engine_operation"))

  Difficult_engine_starting.setProbabilities(
    get_probabilities_by_component("Difficult_engine_starting"))

  Drop_in_engine_power.setProbabilities(
    get_probabilities_by_component("Drop_in_engine_power"))

  Increase_in_engine_smoke.setProbabilities(
    get_probabilities_by_component("Increase_in_engine_smoke"))

  Appearance_of_oil_emulsion_in_engine_coolant.setProbabilities(
    get_probabilities_by_component("Appearance_of_oil_emulsion_in_engine_coolant"))

  Increased_engine_noise.setProbabilities(
    get_probabilities_by_component("Increased_engine_noise"))

  When_engine_speed_rises_dips_occur.setProbabilities(
    get_probabilities_by_component("When_engine_speed_rises_dips_occur"))

  Fuel_leak.setProbabilities(
    get_probabilities_by_component("Fuel_leak"))

  When_car_is_running_engine_starts_to_triple.setProbabilities(
    get_probabilities_by_component("When_car_is_running_engine_starts_to_triple"))


  Oil_can_on_dashboard_lights_up.setProbabilities(
    get_probabilities_by_component("Oil_can_on_dashboard_lights_up"))
  
  Oil_pressure_increase.setProbabilities(
    get_probabilities_by_component("Oil_pressure_increase"))

  Increased_oil_consumption.setProbabilities(
    get_probabilities_by_component("Increased_oil_consumption"))

  Engine_overheating.setProbabilities(
    get_probabilities_by_component("Engine_overheating"))

  Physical_damage_to_filter.setProbabilities(
    get_probabilities_by_component("Physical_damage_to_filter"))

  Oil_turns_black.setProbabilities(
    get_probabilities_by_component("Oil_turns_black"))

  Low_oil_level.setProbabilities(
    get_probabilities_by_component("Low_oil_level"))
  
  Cooling_fan_does_not_turn_on.setProbabilities(
    get_probabilities_by_component("Cooling_fan_does_not_turn_on"))

  Cooling_fan_does_not_turn_off.setProbabilities(
    get_probabilities_by_component("Cooling_fan_does_not_turn_off"))

  Cooling_fan_external_damage.setProbabilities(
    get_probabilities_by_component("Cooling_fan_external_damage"))

  Cooling_pump_pulley_play.setProbabilities(
    get_probabilities_by_component("Cooling_pump_pulley_play"))

  Antifreeze_leakage_under_car.setProbabilities(
    get_probabilities_by_component("Antifreeze_leakage_under_car"))

  Appearance_of_pungent_smell_of_antifreeze_in_car.setProbabilities(
    get_probabilities_by_component("Appearance_of_pungent_smell_of_antifreeze_in_car"))

  Interior_heating_problems.setProbabilities(
    get_probabilities_by_component("Interior_heating_problems"))

  Damaged_cylinder_head_gasket.setProbabilities(
    get_probabilities_by_component("Interior_heating_problems"))

  Relief_valve_plunger_sticking.setProbabilities(
    get_probabilities_by_component("Relief_valve_plunger_sticking"))

  Loose_radiator_cap_spring.setProbabilities(
    get_probabilities_by_component("Loose_radiator_cap_spring"))

  Smoke_from_under_hood.setProbabilities(
    get_probabilities_by_component("Smoke_from_under_hood"))

  White_steam_from_muffler.setProbabilities(
    get_probabilities_by_component("White_steam_from_muffler"))

  Fan_turns_on_ahead_of_time.setProbabilities(
    get_probabilities_by_component("Fan_turns_on_ahead_of_time"))

  Engine_takes_long_time_to_reach_operating_temperature.setProbabilities(
    get_probabilities_by_component("Fan_turns_on_ahead_of_time"))

  Fluctuations_in_engine_temperature_while_driving.setProbabilities(
    get_probabilities_by_component("Fluctuations_in_engine_temperature_while_driving"))

  # Changing the nodes spacial and visual attributes:
  High_pressure_pump.setNodePosition(100,10)
  Fuel_filter.setNodePosition(300,10)
  Injectors.setNodePosition(300,150)
  Fuel_priming_pump.setNodePosition(200,150)
  Oil_pump.setNodePosition(350,150)
  Oil_filter.setNodePosition(450,150)
  Engine_oil.setNodePosition(600,150)
  Cooling_fan.setNodePosition(750,150)
  Coolant_pump.setNodePosition(900,150)
  Radiator.setNodePosition(1200,150)
  Radiator_cap.setNodePosition(1350,150)
  Expansion_tank.setNodePosition(1450,150)
  Thermostat.setNodePosition(1600,150)


  Elevated_fuel_consumption.setNodePosition(500,350)
  Unstable_engine_operation.setNodePosition(700,350)
  Difficult_engine_starting.setNodePosition(900,350)
  Drop_in_engine_power.setNodePosition(1000,350)
  Increase_in_engine_smoke.setNodePosition(1150,350)
  Appearance_of_oil_emulsion_in_engine_coolant.setNodePosition(1300,350)
  Increased_engine_noise.setNodePosition(1450,350)
  When_engine_speed_rises_dips_occur.setNodePosition(1600,350)
  Fuel_leak.setNodePosition(1750,350)
  When_car_is_running_engine_starts_to_triple.setNodePosition(1900,350)
  Oil_can_on_dashboard_lights_up.setNodePosition(2050,350)
  Oil_pressure_increase.setNodePosition(2200,350)
  Increased_oil_consumption.setNodePosition(2350,350)
  Engine_overheating.setNodePosition(2500,350)
  Physical_damage_to_filter.setNodePosition(2650,350)
  Oil_turns_black.setNodePosition(2800,350)
  Low_oil_level.setNodePosition(3000,350)
  Cooling_fan_does_not_turn_on.setNodePosition(3150,350)
  Cooling_fan_does_not_turn_off.setNodePosition(3300,350)
  Cooling_fan_external_damage.setNodePosition(3450,350)
  Cooling_pump_pulley_play.setNodePosition(3700,350)
  Antifreeze_leakage_under_car.setNodePosition(3950,350)
  Appearance_of_pungent_smell_of_antifreeze_in_car.setNodePosition(4100,350)
  Interior_heating_problems.setNodePosition(4250,350)
  Damaged_cylinder_head_gasket.setNodePosition(4400,350)
  Relief_valve_plunger_sticking.setNodePosition(4550,350)
  Loose_radiator_cap_spring.setNodePosition(4700,350)
  Smoke_from_under_hood.setNodePosition(4850,350)
  White_steam_from_muffler.setNodePosition(5000,350)
  Fan_turns_on_ahead_of_time.setNodePosition(5150,350)
  Engine_takes_long_time_to_reach_operating_temperature.setNodePosition(5300,350)
  Fluctuations_in_engine_temperature_while_driving.setNodePosition(5450,350)

  # Add notes to network
  net.addNodes([High_pressure_pump, Fuel_filter,
                Injectors, Fuel_priming_pump, Oil_pump, Oil_filter, Engine_oil, Cooling_fan, 
                Coolant_pump, Radiator, Radiator_cap, Expansion_tank, Thermostat,
                Elevated_fuel_consumption, Unstable_engine_operation, 
                Difficult_engine_starting, Drop_in_engine_power, Increase_in_engine_smoke, 
                Appearance_of_oil_emulsion_in_engine_coolant, Increased_engine_noise,
                When_engine_speed_rises_dips_occur, Fuel_leak, When_car_is_running_engine_starts_to_triple, 
                Oil_can_on_dashboard_lights_up, Oil_pressure_increase, Increased_oil_consumption,
                Engine_overheating, Physical_damage_to_filter, Oil_turns_black, Low_oil_level, 
                Cooling_fan_does_not_turn_on, Cooling_fan_does_not_turn_off, Cooling_fan_external_damage,
                Cooling_pump_pulley_play, Antifreeze_leakage_under_car, Appearance_of_pungent_smell_of_antifreeze_in_car,
                Interior_heating_problems, Damaged_cylinder_head_gasket, Relief_valve_plunger_sticking, 
                Loose_radiator_cap_spring, Smoke_from_under_hood, White_steam_from_muffler, Fan_turns_on_ahead_of_time,
                Engine_takes_long_time_to_reach_operating_temperature, Fluctuations_in_engine_temperature_while_driving,
                ])

  # Write file
  net.writeFile('CarProblem.xdsl')

  # Set evidence
  net.setEvidence('Cooling_fan_does_not_turn_on', 1)
  net.setEvidence('Fluctuations_in_engine_temperature_while_driving', 1)
  
  #net.setEvidence('Fuel_filter', 1)

  # Compute the beliefs for the network
  net.computeBeliefs()
    
  # Print the results for each node
  print('High_pressure_pump ', High_pressure_pump.getBeliefs())
  print('Fuel_filter ', Fuel_filter.getBeliefs())
  print('Injectors ', Injectors.getBeliefs())
  print('Fuel_priming_pump ', Fuel_priming_pump.getBeliefs())
  print('\n^^^^^^^^^^^^^Engine Lubrication system^^^^^^^^^^^^^\n')
  print('Oil_pump ', Oil_pump.getBeliefs())
  print('Oil_filter ', Oil_filter.getBeliefs())
  print('Engine_oil ', Engine_oil.getBeliefs())
  print('\n^^^^^^^^^^^^^Cooling system^^^^^^^^^^^^^\n')
  print('Cooling_fan ', Cooling_fan.getBeliefs())
  print('Coolant_pump ', Coolant_pump.getBeliefs())
  print('Radiator ', Radiator.getBeliefs())
  print('Radiator_cap ', Radiator_cap.getBeliefs())
  print('Expansion_tank ', Expansion_tank.getBeliefs())
  print('Thermostat ', Thermostat.getBeliefs())
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
  print('__________________________')
  # print('Oil_can_on_dashboard_lights_up', Oil_can_on_dashboard_lights_up.getBeliefs())
  # print('Oil_pressure_increase', Oil_pressure_increase.getBeliefs())
  # print('Increased_oil_consumption', Increased_oil_consumption.getBeliefs())
  # print('Engine_overheating', Engine_overheating.getBeliefs())
  # print('Physical_damage_to_filter', Physical_damage_to_filter.getBeliefs())
  # print('Oil_turns_black', Oil_turns_black.getBeliefs())
  # print('Low_oil_level', Low_oil_level.getBeliefs())
  print('__________________________')
  print('Cooling_fan_does_not_turn_on', Cooling_fan_does_not_turn_on.getBeliefs())
  print('Cooling_fan_does_not_turn_off', Cooling_fan_does_not_turn_off.getBeliefs())
  print('Cooling_fan_external_damage', Cooling_fan_external_damage.getBeliefs())
  print('Cooling_pump_pulley_play', Cooling_pump_pulley_play.getBeliefs())
  print('Antifreeze_leakage_under_car', Antifreeze_leakage_under_car.getBeliefs())
  print('Appearance_of_pungent_smell_of_antifreeze_in_car', Appearance_of_pungent_smell_of_antifreeze_in_car.getBeliefs())
  print('Interior_heating_problems', Interior_heating_problems.getBeliefs())
  print('Damaged_cylinder_head_gasket', Damaged_cylinder_head_gasket.getBeliefs())
  print('Relief_valve_plunger_sticking', Relief_valve_plunger_sticking.getBeliefs())
  print('Loose_radiator_cap_spring', Loose_radiator_cap_spring.getBeliefs())
  print('Smoke_from_under_hood', Smoke_from_under_hood.getBeliefs())
  print('White_steam_from_muffler', White_steam_from_muffler.getBeliefs())
  print('Fan_turns_on_ahead_of_time', Fan_turns_on_ahead_of_time.getBeliefs())
  print('Engine_takes_long_time_to_reach_operating_temperature', Engine_takes_long_time_to_reach_operating_temperature.getBeliefs())
  print('Fluctuations_in_engine_temperature_while_driving', Fluctuations_in_engine_temperature_while_driving.getBeliefs())
  

  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

# python -W ignore example.py 

