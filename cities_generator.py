import pandas as pd
import random

# Generate random city data
cities = pd.DataFrame({
    'x': [random.randint(0, 100) for _ in range(20)],
    'y': [random.randint(0, 100) for _ in range(20)]
})

# Save to CSV
cities.to_csv('data/cities.csv', index=False)
