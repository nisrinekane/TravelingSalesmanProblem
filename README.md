# Traveling Salesman Problem Solver Using Genetic Algorithm 

This project implements a genetic algorithm to solve the traveling salesman problem (TSP). Given a list of cities, the objective of the TSP is to find the shortest possible route that visits each city once and returns to the origin city.

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

This implementation uses a genetic algorithm, which is a heuristic that mimics the process of natural selection, to find an efficient solution to the TSP. This process includes mechanisms like selection, crossover (or "mating"), and mutation.

## Project Structure

* `main.py`: The main script that runs the genetic algorithm and visualizes the results.
* `genetic_algorithm.py`: Contains the implementation of the genetic algorithm.
* `visualization.py`: Contains functions for visualizing the route.
* `city.py`: A helper class for representing a city.
* `route.py`: A helper class for representing a route between cities.
* `fitness.py`: A helper class for evaluating the fitness of a route.

## Limitations

This implementation does not guarantee finding the optimal solution. Genetic algorithms generally provide good approximations for the TSP, but they do not always find the most efficient route.

---

Regarding whether the project is ready to be pushed, you should first ensure that you have tested the program with various inputs and in different scenarios to confirm that it works as expected. It would also be a good idea to add some comments in the code explaining the logic, especially for complex parts. Lastly, make sure you have removed any unnecessary print statements or debug code.

From a features perspective, if you are satisfied with the functionality of the project (it can solve the TSP with reasonable accuracy and efficiency, and it can visualize the resulting route), then it sounds like it's ready to be pushed. Remember, you can always make improvements and push updates later.