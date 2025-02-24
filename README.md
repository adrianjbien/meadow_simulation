# Wolf and Sheep Simulation

## Description

This project is a text-based simulation of a wolf chasing a herd of sheep in an infinite two-dimensional meadow. The simulation involves movement mechanics where sheep try to escape while the wolf hunts them down. The simulation runs for a predefined number of rounds or until all sheep have been eaten.

## Features

Object-oriented implementation with Wolf and Sheep classes.

Infinite two-dimensional meadow with Cartesian coordinates.

Randomized initial positions for sheep.

## Movement mechanics:

Sheep move in random directions (N, E, S, W).

Wolf moves towards the closest sheep.

If the wolf catches a sheep, it is removed from the simulation, and wolf takes its place.

## Simulation logs and data saving:

### Outputs simulation details per round.

### Saves animal positions to pos.json.

### Saves the number of alive sheep per round to alive.csv.

### Command-line argument support via argparse.

### Configuration file support using configparser.

### Logging using the logging module.

## Default Settings

Maximum rounds: 50

Number of sheep: 15

Initial position limits for sheep: [-10.0, 10.0]

Sheep movement distance: 0.5

Wolf movement distance: 1.0

## Installation

Run the simulation with default settings:

python simulation.py

Usage

## Run the simulation with optional command-line arguments:

python simulation.py [-c CONFIG] [-l LOG_LEVEL] [-r ROUNDS] [-s SHEEP] [-w]

## Command-Line Arguments

### Arguments Description

-c, --config FILE

Load parameters from a config file

-h, --help

Show help message and exit

-l, --log LEVEL

Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

-r, --rounds NUM

Set maximum number of rounds

-s, --sheep NUM

Set number of sheep

-w, --wait

Pause after each round until key press

## Configuration File Format

### Example INI file:

[Sheep]
InitPosLimit = 10.0
MoveDist = 0.5

[Wolf]
MoveDist = 1.0

### Data Logging

pos.json: Saves positions of all animals per round.

alive.csv: Saves count of alive sheep per round.

chase.log (if logging enabled): Logs simulation events.
