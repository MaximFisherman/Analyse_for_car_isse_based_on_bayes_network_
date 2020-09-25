#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# import pybn library
from pybn import *

  # Define a main() function.
def main():

  # Create a Network
  net = Network('CarProblem')

  Fuel = Node('Fuel') # (топливо)
  SparkPlug = Node('Spark_Plug') # (Cвечи зажигания)
  FuelMeterStanding = Node('Fuel_Meter_Standing') # (Датчик топлива)
  Start = Node('Start') # (Заведеться ли машина или нет)
  Engine = Node('Engine_Start') # (Движок)

  Fuel.addOutcomes(['yes','no']) 
  SparkPlug.addOutcomes(['yes','no'])
  FuelMeterStanding.addOutcomes(['full','half','empty'])
  Start.addOutcomes(['yes','no'])


  # Setting number (and name) of outcomes
  Engine.addOutcomes(['yes','no'])

  # Add arc from 'Fuel' to 'Fuel Meter Standing'
  arc_Fu_FM = Arc(Fuel,FuelMeterStanding)

  # Add arc from 'Fuel' to 'Start'
  arc_Fu_St = Arc(Fuel,Start)

  # Add arc from 'Engine' to 'Start'
  arc_EN_St = Arc(Engine,Start)

  # Add arc from 'Clean Spark Plugs' to 'Start'
  arc_SP_St = Arc(SparkPlug,Start)


  # Shows the size of the probability matrix 'Start'
  # print FuelMeterStanding.getTableSize()

  # Conditional distribution for node 'Fuel'
  Fuel.setProbabilities([0.98,0.02])

  # Conditional distribution for node 'Clean Spark Plugs'
  SparkPlug.setProbabilities([0.96,0.04])

  # Conditional distribution for node 'Fuel Meter Standing'
  FuelMeterStanding.setProbabilities([0.39, 0.60, 0.01, 0.001, 0.001, 0.998])

  # Conditional distribution for node 'Engine'
  Engine.setProbabilities([0.95,0.05])

  # Conditional distribution for node 'Start'
  Start.setProbabilities([
    0.99, 0.01, 0.01, 0.99, 0.0, 1.0, 0.0, 1.0, 
    0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 
    ])


  # Changing the nodes spacial and visual attributes:
  Fuel.setNodePosition(100,10)

  SparkPlug.setNodePosition(300,10)

  FuelMeterStanding.setNodePosition(0,150)
  FuelMeterStanding.setInteriorColor('cc99ff')

  Engine.setNodePosition(300,150)
  Engine.setInteriorColor('ff0011')

  Start.setNodePosition(200,150)
  Start.setInteriorColor('ff0000')

  # Add notes to network
  net.addNodes([Fuel,SparkPlug,FuelMeterStanding,Engine,Start])

  # Write file
  net.writeFile('CarProblem.xdsl')

  # Set evidence
  #net.setEvidence('Fuel',1)
  #net.setEvidence('Engine',1)
  net.setEvidence('Start',2)

  # Compute the beliefs for the network
  net.computeBeliefs()

  # Print the results for each node
  print('Fuel', Fuel.getBeliefs())
  print('Spark_Plug', SparkPlug.getBeliefs())
  print('Fuel_Meter_Standing', FuelMeterStanding.getBeliefs())
  print('Engine', Engine.getBeliefs())
  print('Start', Start.getBeliefs())

  # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

# python -W ignore example.py 

