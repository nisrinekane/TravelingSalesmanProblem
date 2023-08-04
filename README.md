# Traveling Salesman Problem Solver Using Genetic Algorithm 

This project implements a genetic algorithm to solve the traveling salesman problem (TSP). Given a list of cities, the objective of the TSP is to find the shortest possible route that visits each city once and returns to the origin city.

![best_route_image](https://github.com/nisrinekane/TravelingSalesmanProblem/blob/main/output/best_route.png)


## Installation

Install Python 3.7 or higher on your system. Install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

Run: the file with the main function

```
python tsp.py
```

The program will output the best route it found and display a visualization of this route.

## How It Works

This implementation uses a genetic algorithm, which is a heuristic that mimics the process of natural selection, to find an efficient solution to the TSP. This process includes mechanisms like selection, crossover (mating) and mutation.

## Project Structure

* `tsp.py`: Contains the implementation of the genetic algorithm including the main evolutionary loop.
* `visualize.py`: Contains function for visualizing the route using matplotlib.
* `cities.csv`: Contains city names and their x and y coordinates, you can customize it using the `cities_generator.py` script.

