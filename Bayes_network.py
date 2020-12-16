#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import os
import sys
import time
import msvcrt
import socket

from pybn import *
from msvcrt import getch
          
from Libraries.Object_maker import Object_maker

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



  dict_of_evidence = {}
  
  # Set evidence
  # net.setEvidence('Drop_in_engine_power', 1)
  # net.setEvidence('Candle_deposits', 1)
  # net.setEvidence('Leaking_in_camshaft_oil_seal_area', 1)
  
  # net.setEvidence('Increased_engine_noise', 1)
  # net.setEvidence('Timing_Belt_Problems', 1)
  #net.setEvidence('Unstable_engine_operation', 1)
  
  #net.setEvidence('Fuel_filter', 1)

  # Compute the beliefs for the network
  
  
###################################################################
############## Set Up server for getting simulation value##########  

  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Bind the socket to the port
  server_address = ('localhost', 10000)
  print >>sys.stderr, 'starting up on %s port %s' % server_address
  sock.bind(server_address)

  # Listen for incoming connections
  sock.listen(1)
  while True:
      # Wait for a connection
      print >>sys.stderr, 'waiting for a connection'
      connection, client_address = sock.accept()
      if connection != None: 
          break
      
      

  try:
      def clear(): os.system('cls')
      def disable_not_presented_evidences(map_of_evidence):
        pass
      
      
      
      print >>sys.stderr, 'connection from', client_address
      

      
      # Create a Network
      net = Network('CarProblem')

      while True:
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


          Pistons = Node('Pistons') # (Поршни)
          Pistons.addOutcomes(['work','not_work'])

          Connecting_rod = Node('Connecting_rod') # (Шатун)
          Connecting_rod.addOutcomes(['work','not_work'])

          Crankshaft = Node('Crankshaft') # (Коленвал)
          Crankshaft.addOutcomes(['work','not_work'])

          Flywheel = Node('Flywheel') # (Маховик)
          Flywheel.addOutcomes(['work','not_work'])

          Engine_block = Node('Engine_block') # (Блок двигателя)
          Engine_block.addOutcomes(['work','not_work'])

          Cylinder_head = Node('Cylinder_head') # (Блок двигателя)
          Cylinder_head.addOutcomes(['work','not_work'])


          Valve = Node('Valve') # (Клапана)
          Valve.addOutcomes(['work','not_work'])

          Valve_drive = Node('Valve_drive') # (Привод клапанов)
          Valve_drive.addOutcomes(['work','not_work'])

          Camshaft = Node('Camshaft') # (Распределительный вал)
          Camshaft.addOutcomes(['work','not_work'])

          Shaft_drive = Node('Shaft_drive') # (Привод вала)
          Shaft_drive.addOutcomes(['work','not_work'])
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

          Cooling_pump_pulley_play = Node('Cooling_pump_pulley_play') # (Люфт шкива помпы)
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


          Reduced_compression_in_cylinders = Node('Reduced_compression_in_cylinders') # (Сниженная компресия в цилиндрах)
          Reduced_compression_in_cylinders.addOutcomes(['work','not_work'])

          Metallic_knock_is_heard_when_engine_is_running = Node('Metallic_knock_is_heard_when_engine_is_running') # (Слышен металический стук при работе двигателя)
          Metallic_knock_is_heard_when_engine_is_running.addOutcomes(['work','not_work'])

          No_idling = Node('No_idling') # (Отсутствие холостого хода)
          No_idling.addOutcomes(['work','not_work'])

          Gear_shift_stiffness = Node('Gear_shift_stiffness') # (Жесткость переключения передач)
          Gear_shift_stiffness.addOutcomes(['work','not_work'])

          Vibration_when_pressing_clutch_pedal = Node('Vibration_when_pressing_clutch_pedal') # (Вибрация при нажатии педали сцепления)
          Vibration_when_pressing_clutch_pedal.addOutcomes(['work','not_work'])

          Creaking_and_grinding_noise_at_startup = Node('Creaking_and_grinding_noise_at_startup') # (Скрип и скрежет при запуске)
          Creaking_and_grinding_noise_at_startup.addOutcomes(['work','not_work'])

          Physical_deformation_of_engine_block = Node('Physical_deformation_of_engine_block') # (Физическая деформация головы двигателя)
          Physical_deformation_of_engine_block.addOutcomes(['work','not_work'])

          Breakage_of_thread_of_fastening_cylinder_head = Node('Breakage_of_thread_of_fastening_cylinder_head') # (Срыв резьбы крепления головки блока цилиндров)
          Breakage_of_thread_of_fastening_cylinder_head.addOutcomes(['work','not_work'])

          Leaks_in_area_of_cylinder_head_gasket = Node('Leaks_in_area_of_cylinder_head_gasket') # (Течи в области прокладки ГБЦ)
          Leaks_in_area_of_cylinder_head_gasket.addOutcomes(['work','not_work'])

          Reduced_compression_cylinders_block = Node('Reduced_compression_cylinders_block') # (Сниженная компресия)
          Reduced_compression_cylinders_block.addOutcomes(['work','not_work'])

          Antifreeze_traces_in_exhaust_system = Node('Antifreeze_traces_in_exhaust_system') # (Следы тосола в выхлопной системе)
          Antifreeze_traces_in_exhaust_system.addOutcomes(['work','not_work'])


          Pops_are_heard_in_exhaust_pipe = Node('Pops_are_heard_in_exhaust_pipe') # (Слышны хлопки в выхлопной трубе)
          Pops_are_heard_in_exhaust_pipe.addOutcomes(['work','not_work'])

          Exhaust_color_gray_black = Node('Exhaust_color_gray_black') # (Цвет выхлопа серо-черный)
          Exhaust_color_gray_black.addOutcomes(['work','not_work'])

          Candle_deposits = Node('Candle_deposits') # (Нагар на свечах)
          Candle_deposits.addOutcomes(['work','not_work'])

          Leaking_in_camshaft_oil_seal_area = Node('Leaking_in_camshaft_oil_seal_area') # (Течь в области сальника распредвала)
          Leaking_in_camshaft_oil_seal_area.addOutcomes(['work','not_work'])

          Timing_Belt_Problems = Node('Timing_Belt_Problems') # (Проблемы с ремнем ГРМ)
          Timing_Belt_Problems.addOutcomes(['work','not_work'])
        ###################################################################################################
          # Add arc to 'Elevated_fuel_consumption'
          arc_High_pressure_pump__Elevated_fuel_consumption = Arc(High_pressure_pump, Elevated_fuel_consumption)
          arc_Fuel_filter__Elevated_fuel_consumption = Arc(Fuel_filter, Elevated_fuel_consumption)
          arc_Injectors__Elevated_fuel_consumption = Arc(Injectors, Elevated_fuel_consumption)
          arc_Fuel_priming_pump__Elevated_fuel_consumption = Arc(Fuel_priming_pump, Elevated_fuel_consumption)
          arc_Pistons__Elevated_fuel_consumption = Arc(Pistons, Elevated_fuel_consumption)

          
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
          arc_Pistons__Drop_in_engine_power = Arc(Pistons, Drop_in_engine_power)
          arc_Crankshaft__Drop_in_engine_power = Arc(Crankshaft, Drop_in_engine_power)
          arc_Flywheel__Drop_in_engine_power = Arc(Flywheel, Drop_in_engine_power)
          arc_Valve__Drop_in_engine_power = Arc(Valve, Drop_in_engine_power)
          arc_Valve_drive__Drop_in_engine_power = Arc(Valve_drive, Drop_in_engine_power)
          arc_Camshaft__Drop_in_engine_power = Arc(Camshaft, Drop_in_engine_power)


          # Add arc to Difficult_engine_starting
          arc_High_pressure_pump__Difficult_engine_starting = Arc(High_pressure_pump, Difficult_engine_starting)
          arc_Fuel_priming_pump__Difficult_engine_starting = Arc(Fuel_priming_pump, Difficult_engine_starting)
          arc_Crankshaft__Difficult_engine_starting = Arc(Crankshaft, Difficult_engine_starting)
          arc_Flywheel__Difficult_engine_starting = Arc(Flywheel, Difficult_engine_starting)

          # Add arc to Increase_in_engine_smoke
          arc_High_pressure_pump__Increase_in_engine_smoke = Arc(High_pressure_pump, Increase_in_engine_smoke)
          arc_Injectors__Increase_in_engine_smoke = Arc(Injectors, Increase_in_engine_smoke)
          arc_Fuel_priming_pump__Increase_in_engine_smoke = Arc(Fuel_priming_pump, Increase_in_engine_smoke)
          arc_Pistons__Increase_in_engine_smoke = Arc(Pistons, Increase_in_engine_smoke)

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
          arc_Crankshaft__Increased_engine_noise = Arc(Crankshaft, Increased_engine_noise)

          # Add arc to When_engine_speed_rises_dips_occur
          arc_Fuel_filter__When_engine_speed_rises_dips_occur = Arc(Fuel_filter, When_engine_speed_rises_dips_occur)
          arc_Crankshaft__When_engine_speed_rises_dips_occur = Arc(Crankshaft, When_engine_speed_rises_dips_occur)
          arc_Valve_drive__When_engine_speed_rises_dips_occur = Arc(Valve_drive, When_engine_speed_rises_dips_occur)
          arc_Camshaft__When_engine_speed_rises_dips_occur = Arc(Camshaft, When_engine_speed_rises_dips_occur)

          # Add arc to Increase_in_engine_smoke
          arc_High_pressure_pump__Fuel_leak = Arc(High_pressure_pump, Fuel_leak)
          arc_Fuel_filter__Fuel_leak = Arc(Fuel_filter, Fuel_leak)
          arc_Injectors__Fuel_leak = Arc(Injectors, Fuel_leak)
          arc_Fuel_priming_pump__Fuel_leak = Arc(Fuel_priming_pump, Fuel_leak)


          # Add arc to Increase_in_engine_smoke
          arc_Fuel_filter__When_car_is_running_engine_starts_to_triple = Arc(Fuel_filter, When_car_is_running_engine_starts_to_triple)
          arc_Injectors__When_car_is_running_engine_starts_to_triple = Arc(Injectors, When_car_is_running_engine_starts_to_triple)
          arc_Cylinder_head__When_car_is_running_engine_starts_to_triple = Arc(Cylinder_head, When_car_is_running_engine_starts_to_triple)
          arc_Valve__When_car_is_running_engine_starts_to_triple = Arc(Valve, When_car_is_running_engine_starts_to_triple)
          arc_Valve_drive__When_car_is_running_engine_starts_to_triple = Arc(Valve_drive, When_car_is_running_engine_starts_to_triple)


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
          arc_Pistons__Increased_oil_consumption = Arc(Pistons, Increased_oil_consumption)

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
          arc_Cylinder_head__Smoke_from_under_hood = Arc(Cylinder_head, Smoke_from_under_hood)

          # Add arc White_steam_from_muffler
          arc_Expansion_tank__White_steam_from_muffler = Arc(Expansion_tank, White_steam_from_muffler)
          
          # Add arc Fan_turns_on_ahead_of_time
          arc_Thermostat__Fan_turns_on_ahead_of_time = Arc(Thermostat, Fan_turns_on_ahead_of_time)

          # Add arc Engine_takes_long_time_to_reach_operating_temperature
          arc_Thermostat__Engine_takes_long_time_to_reach_operating_temperature = Arc(Thermostat, Engine_takes_long_time_to_reach_operating_temperature)
          
          # Add arc Engine_takes_long_time_to_reach_operating_temperature
          arc_Thermostat__Fluctuations_in_engine_temperature_while_driving = Arc(Thermostat, Fluctuations_in_engine_temperature_while_driving)


          # Add arc Reduced_compression_in_cylinders
          arc_Pistons__Reduced_compression_in_cylinders = Arc(Pistons, Reduced_compression_in_cylinders)

          # Add arc Metallic_knock_is_heard_when_engine_is_running
          arc_Connecting_rod__Metallic_knock_is_heard_when_engine_is_running = Arc(Connecting_rod, Metallic_knock_is_heard_when_engine_is_running)
          
          # Add arc No_idling
          arc_Crankshaft__No_idling = Arc(Crankshaft, No_idling)
          
          # Add arc Gear_shift_stiffness
          arc_Flywheel__Gear_shift_stiffness = Arc(Flywheel, Gear_shift_stiffness)

          # Add arc Vibration_when_pressing_clutch_pedal
          arc_Flywheel__Vibration_when_pressing_clutch_pedal = Arc(Flywheel, Vibration_when_pressing_clutch_pedal)
          
          # Add arc Creaking_and_grinding_noise_at_startup
          arc_Flywheel__Creaking_and_grinding_noise_at_startup = Arc(Flywheel, Creaking_and_grinding_noise_at_startup)
          
          # Add arc Physical_deformation_of_engine_block
          arc_Engine_block__Physical_deformation_of_engine_block = Arc(Engine_block, Physical_deformation_of_engine_block)
          
          # Add arc Breakage_of_thread_of_fastening_cylinder_head
          arc_Engine_block__Breakage_of_thread_of_fastening_cylinder_head = Arc(Engine_block, Breakage_of_thread_of_fastening_cylinder_head)
          
          # Add arc Leaks_in_area_of_cylinder_head_gasket
          arc_Cylinder_head__Leaks_in_area_of_cylinder_head_gasket = Arc(Cylinder_head, Leaks_in_area_of_cylinder_head_gasket)
          arc_Valve_drive__Leaks_in_area_of_cylinder_head_gasket = Arc(Valve_drive, Leaks_in_area_of_cylinder_head_gasket)
          
          # Add arc Reduced_compression_cylinders_block
          arc_Cylinder_head__Reduced_compression_cylinders_block = Arc(Cylinder_head, Reduced_compression_cylinders_block)

          # Add arc Antifreeze_traces_in_exhaust_system
          arc_Cylinder_head__Antifreeze_traces_in_exhaust_system = Arc(Cylinder_head, Antifreeze_traces_in_exhaust_system)


          # Add arc Pops_are_heard_in_exhaust_pipe
          arc_Valve__Pops_are_heard_in_exhaust_pipe = Arc(Valve, Pops_are_heard_in_exhaust_pipe)

          # Add arc Exhaust_color_gray_black
          arc_Valve_drive__Exhaust_color_gray_black = Arc(Valve_drive, Exhaust_color_gray_black)

          # Add arc Candle_deposits
          arc_Valve_drive__Candle_deposits = Arc(Valve_drive, Candle_deposits)
          
          # Add arc Leaking_in_camshaft_oil_seal_area
          arc_Valve_drive__Leaking_in_camshaft_oil_seal_area = Arc(Valve_drive, Leaking_in_camshaft_oil_seal_area)
          
          # Add arc Timing_Belt_Problems
          arc_Shaft_drive__Timing_Belt_Problems = Arc(Shaft_drive, Timing_Belt_Problems)
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
          Pistons.setProbabilities([0.99,0.01])
          Connecting_rod.setProbabilities([0.99,0.01]) 
          Crankshaft.setProbabilities([0.99,0.01]) 
          Flywheel.setProbabilities([0.99,0.01]) 
          Engine_block.setProbabilities([0.99,0.01]) 
          Cylinder_head.setProbabilities([0.99,0.01]) 
          Valve.setProbabilities([0.99,0.01]) 
          Valve_drive.setProbabilities([0.99,0.01])
          Camshaft.setProbabilities([0.99,0.01])
          Shaft_drive.setProbabilities([0.99,0.01])

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

          Reduced_compression_in_cylinders.setProbabilities(
            get_probabilities_by_component("Reduced_compression_in_cylinders"))
          
          Metallic_knock_is_heard_when_engine_is_running.setProbabilities(
            get_probabilities_by_component("Metallic_knock_is_heard_when_engine_is_running"))

          No_idling.setProbabilities(
            get_probabilities_by_component("No_idling"))
          
          Gear_shift_stiffness.setProbabilities(
            get_probabilities_by_component("Gear_shift_stiffness"))

          Vibration_when_pressing_clutch_pedal.setProbabilities(
            get_probabilities_by_component("Vibration_when_pressing_clutch_pedal"))

          Creaking_and_grinding_noise_at_startup.setProbabilities(
            get_probabilities_by_component("Creaking_and_grinding_noise_at_startup"))

          Physical_deformation_of_engine_block.setProbabilities(
            get_probabilities_by_component("Physical_deformation_of_engine_block"))

          Breakage_of_thread_of_fastening_cylinder_head.setProbabilities(
            get_probabilities_by_component("Physical_deformation_of_engine_block"))

          Leaks_in_area_of_cylinder_head_gasket.setProbabilities(
            get_probabilities_by_component("Leaks_in_area_of_cylinder_head_gasket"))

          Reduced_compression_cylinders_block.setProbabilities(
            get_probabilities_by_component("Reduced_compression_cylinders_block"))

          Antifreeze_traces_in_exhaust_system.setProbabilities(
            get_probabilities_by_component("Antifreeze_traces_in_exhaust_system"))

          Pops_are_heard_in_exhaust_pipe.setProbabilities(
            get_probabilities_by_component("Pops_are_heard_in_exhaust_pipe"))

          Exhaust_color_gray_black.setProbabilities(
            get_probabilities_by_component("Exhaust_color_gray_black"))

          Candle_deposits.setProbabilities(
            get_probabilities_by_component("Candle_deposits"))

          Leaking_in_camshaft_oil_seal_area.setProbabilities(
            get_probabilities_by_component("Leaking_in_camshaft_oil_seal_area"))

          Timing_Belt_Problems.setProbabilities(
            get_probabilities_by_component("Timing_Belt_Problems"))

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
          Pistons.setNodePosition(1750,150)
          Connecting_rod.setNodePosition(2000,150)
          Crankshaft.setNodePosition(2150,150)
          Flywheel.setNodePosition(2300,150)
          Engine_block.setNodePosition(2450,150)

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
          Reduced_compression_in_cylinders.setNodePosition(5700,350)
          Metallic_knock_is_heard_when_engine_is_running.setNodePosition(5850,350)
          No_idling.setNodePosition(6000,350)
          Gear_shift_stiffness.setNodePosition(6150,350)
          Vibration_when_pressing_clutch_pedal.setNodePosition(6300,350)
          Creaking_and_grinding_noise_at_startup.setNodePosition(6450,350)
          Physical_deformation_of_engine_block.setNodePosition(6600,350)
          Breakage_of_thread_of_fastening_cylinder_head.setNodePosition(6750,350)
          Leaks_in_area_of_cylinder_head_gasket.setNodePosition(6900,350)
          Reduced_compression_cylinders_block.setNodePosition(7050,350)
          Antifreeze_traces_in_exhaust_system.setNodePosition(7200,350)
          Pops_are_heard_in_exhaust_pipe.setNodePosition(7350,350)
          Exhaust_color_gray_black.setNodePosition(7500,350)
          Candle_deposits.setNodePosition(7650,350)
          Leaking_in_camshaft_oil_seal_area.setNodePosition(7800,350)
          Timing_Belt_Problems.setNodePosition(8000,350)

          # Add notes to network
          net.addNodes([High_pressure_pump, Fuel_filter,
                        Injectors, Fuel_priming_pump, Oil_pump, Oil_filter, Engine_oil, Cooling_fan, 
                        Coolant_pump, Radiator, Radiator_cap, Expansion_tank, Thermostat, Pistons, Connecting_rod,
                        Crankshaft, Flywheel, Engine_block, Cylinder_head, Valve, Valve_drive, 
                        Camshaft, Shaft_drive, Elevated_fuel_consumption, Unstable_engine_operation, 
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
                        Reduced_compression_in_cylinders, Metallic_knock_is_heard_when_engine_is_running, No_idling,
                        Gear_shift_stiffness, Vibration_when_pressing_clutch_pedal, Creaking_and_grinding_noise_at_startup,
                        Physical_deformation_of_engine_block, Breakage_of_thread_of_fastening_cylinder_head,
                        Leaks_in_area_of_cylinder_head_gasket, Reduced_compression_cylinders_block, Antifreeze_traces_in_exhaust_system,
                        Pops_are_heard_in_exhaust_pipe, Exhaust_color_gray_black, Candle_deposits, Leaking_in_camshaft_oil_seal_area,
                        Timing_Belt_Problems])

          # Write file
          net.writeFile('CarProblem.xdsl')








          data = connection.recv(4096)
          #print >>sys.stderr, 'received "%s"\n' % data
          
          obj = Object_maker(data)

          for evidence in dict_of_evidence:
            evidence = 0 

          for evidence_name in obj.unformat():
            if str(evidence_name) != '' and str(evidence_name) != 'None':
              dict_of_evidence[str(evidence_name)] = 1 
           

          # if(len(dict_of_evidence) > 1):  
          #    for key in dict_of_evidence:
          #       print(str(key) + ": " + str(dict_of_evidence[key]))

          for key in dict_of_evidence:
            net.setEvidence(str(key), dict_of_evidence[str(key)])

          net.computeBeliefs()
          clear()

          # print(dict_of_evidence)
          #Print the results for each node
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
          print('\n^^^^^^^^^^^^^Cooling system^^^^^^^^^^^^^\n')
          print('Pistons ', Pistons.getBeliefs())
          print('Connecting_rod ', Connecting_rod.getBeliefs())
          print('Crankshaft ', Crankshaft.getBeliefs())
          print('Flywheel ', Flywheel.getBeliefs())
          print('Engine_block ', Engine_block.getBeliefs())
          print('Cylinder_head ', Cylinder_head.getBeliefs())
          print('\n^^^^^^^^^^^^^Gas distribution mechanism^^^^^^^^^^^^^\n')
          print('Valve ', Valve.getBeliefs())
          print('Valve_drive ', Valve_drive.getBeliefs())
          print('Crankshaft ', Crankshaft.getBeliefs())
          print('Shaft_drive ', Shaft_drive.getBeliefs())
          print('__________________________')
          # print('Elevated_fuel_consumption ', Elevated_fuel_consumption.getBeliefs())
          # print('Unstable_engine_operation ', Unstable_engine_operation.getBeliefs())
          # print('Difficult_engine_starting ', Difficult_engine_starting.getBeliefs())
          # print('Drop_in_engine_power ', Drop_in_engine_power.getBeliefs())
          # print('Increase_in_engine_smoke ', Increase_in_engine_smoke.getBeliefs())
          # print('Appearance_of_oil_emulsion_in_engine_coolant ', Appearance_of_oil_emulsion_in_engine_coolant.getBeliefs())
          # print('Increased_engine_noise', Increased_engine_noise.getBeliefs())
          # print('When_engine_speed_rises_dips_occur', When_engine_speed_rises_dips_occur.getBeliefs())
          # print('Fuel_leak', Fuel_leak.getBeliefs())
          # print('When_car_is_running_engine_starts_to_triple', When_car_is_running_engine_starts_to_triple.getBeliefs())
          # print('__________________________')
          # print('Oil_can_on_dashboard_lights_up', Oil_can_on_dashboard_lights_up.getBeliefs())
          # print('Oil_pressure_increase', Oil_pressure_increase.getBeliefs())
          # print('Increased_oil_consumption', Increased_oil_consumption.getBeliefs())
          # print('Engine_overheating', Engine_overheating.getBeliefs())
          # print('Physical_damage_to_filter', Physical_damage_to_filter.getBeliefs())
          # print('Oil_turns_black', Oil_turns_black.getBeliefs())
          # print('Low_oil_level', Low_oil_level.getBeliefs())
          # print('__________________________')
          # print('Cooling_fan_does_not_turn_on', Cooling_fan_does_not_turn_on.getBeliefs())
          # print('Cooling_fan_does_not_turn_off', Cooling_fan_does_not_turn_off.getBeliefs())
          # print('Cooling_fan_external_damage', Cooling_fan_external_damage.getBeliefs())
          # print('Cooling_pump_pulley_play', Cooling_pump_pulley_play.getBeliefs())
          # print('Antifreeze_leakage_under_car', Antifreeze_leakage_under_car.getBeliefs())
          # print('Appearance_of_pungent_smell_of_antifreeze_in_car', Appearance_of_pungent_smell_of_antifreeze_in_car.getBeliefs())
          # print('Interior_heating_problems', Interior_heating_problems.getBeliefs())
          # print('Damaged_cylinder_head_gasket', Damaged_cylinder_head_gasket.getBeliefs())
          # print('Relief_valve_plunger_sticking', Relief_valve_plunger_sticking.getBeliefs())
          # print('Loose_radiator_cap_spring', Loose_radiator_cap_spring.getBeliefs())
          # print('Smoke_from_under_hood', Smoke_from_under_hood.getBeliefs())
          # print('White_steam_from_muffler', White_steam_from_muffler.getBeliefs())
          # print('Fan_turns_on_ahead_of_time', Fan_turns_on_ahead_of_time.getBeliefs())
          # print('Engine_takes_long_time_to_reach_operating_temperature', Engine_takes_long_time_to_reach_operating_temperature.getBeliefs())
          # print('Fluctuations_in_engine_temperature_while_driving', Fluctuations_in_engine_temperature_while_driving.getBeliefs())
          # print('__________________________')
          # print('Reduced_compression_in_cylinders', Reduced_compression_in_cylinders.getBeliefs())
          # print('Metallic_knock_is_heard_when_engine_is_running', Metallic_knock_is_heard_when_engine_is_running.getBeliefs())
          # print('No_idling', No_idling.getBeliefs())
          # print('Gear_shift_stiffness', Gear_shift_stiffness.getBeliefs())
          # print('Vibration_when_pressing_clutch_pedal', Vibration_when_pressing_clutch_pedal.getBeliefs())
          # print('Creaking_and_grinding_noise_at_startup', Creaking_and_grinding_noise_at_startup.getBeliefs())
          # print('Physical_deformation_of_engine_block', Physical_deformation_of_engine_block.getBeliefs())
          # print('Breakage_of_thread_of_fastening_cylinder_head', Breakage_of_thread_of_fastening_cylinder_head.getBeliefs())
          # print('Leaks_in_area_of_cylinder_head_gasket', Leaks_in_area_of_cylinder_head_gasket.getBeliefs())
          # print('Reduced_compression_cylinders_block', Reduced_compression_cylinders_block.getBeliefs())
          # print('Antifreeze_traces_in_exhaust_system', Antifreeze_traces_in_exhaust_system.getBeliefs())
          # print('__________________________')
          # print('Pops_are_heard_in_exhaust_pipe', Pops_are_heard_in_exhaust_pipe.getBeliefs())
          # print('Exhaust_color_gray_black', Exhaust_color_gray_black.getBeliefs())
          # print('Candle_deposits', Candle_deposits.getBeliefs())
          # print('Leaking_in_camshaft_oil_seal_area', Leaking_in_camshaft_oil_seal_area.getBeliefs())  
          # print('Timing_Belt_Problems', Timing_Belt_Problems.getBeliefs())  
          
          # print "Choose a number from 1 to 7: "
          # userResponse = ''
          
          # flag = False
          # if (msvcrt.kbhit()):
          #   print "you pressed",msvcrt.getch(),"so now i will quit"
          #   userResponse = msvcrt.getch()
          #   if userResponse == '1':
          #       flag = True
                  
          # if flag:
          #   print("aasdasdasdasdasdasdasdadasd")

          if data:
              #print >>sys.stderr, '\nsending data back to the client'
              connection.sendall(data)
          else:
              print >>sys.stderr, 'no more data from', client_address
              break
          
          time.sleep(.6)
          net.reset()

  finally:
      # Clean up the connection
      connection.close()






  


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

# python -W ignore example.py 

