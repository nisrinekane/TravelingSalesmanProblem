import matplotlib.pyplot as plt
import numpy as np

def plot_route(best_route, cities):
    route = cities[best_route]
    route = np.append(route, route[0]).reshape(-1, 2)

    plt.figure(figsize=(8, 8))
    plt.scatter(cities[:, 0], cities[:, 1], color='red')
    plt.plot(route[:, 0], route[:, 1], color='blue', linewidth=1, linestyle='-', marker='o')
    plt.title('Best Route')
    plt.show()
