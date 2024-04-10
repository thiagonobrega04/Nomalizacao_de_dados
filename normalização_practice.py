import pandas as pd

planets = pd.DataFrame({
"Planet": ['Mercury', 'Jupiter', 'Saturn', 'Mars'],
"Orbit Speed": [47.87, 13.07, 9.69, 24.07]
})

# Use Min-Max normalization
sp = planets['Orbit Speed']
planets['Orbit Speed'] = (sp - sp.min()) / (sp.max() - sp.min())
print(planets)

df = pd.DataFrame({
    "Planet": ['Mercury', 'Venus', 'Earth', 'Mars'],
    "Orbit Radius": [58, 108, 150, 228],
    "Planet Diameter": [4879, 12104, 12756, 6792]
})
print(f'DataFrame before normalization: \n {df}')

df['Orbit Radius'] = (df['Orbit Radius'] - df['Orbit Radius'].mean()) / df['Orbit Radius'].std()

# Normalize 'Planet Diameter' column here
df['Planet Diameter'] = (df['Planet Diameter'] - df['Planet Diameter'].mean()) / df['Planet Diameter'].std()

print(f'DataFrame after normalization: \n {df}')

# Create a dataset for planets and their mean orbital speeds (in km/s)
df = pd.DataFrame({
    "Planet": ['Mercury', 'Venus', 'Earth', 'Mars'],
    "Orbital Speed": [47.87, 35.02, 29.78, 24.07]
})

# Normalize the data using Min-Max normalization
sp = df['Orbital Speed']
df['Normal Speed'] = (sp - sp.min()) / (sp.max() - sp.min())
print(df)

# Planet distances in Astronomical Units (1 AU is the average Earth-Sun distance)
planets = pd.DataFrame({
    "Planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"],
    "Distance_AU": [0.39, 0.72, 1, 1.52, 5.20, 9.58]
})
print(f'Planets distances before normalization: \n', planets)

dist = planets['Distance_AU']
planets['dist_norm_z_score'] = (dist - dist.mean()) / dist.std()
print(f'Planets after Z-score normalization: \n', planets)

# TODO: Create a new column "dist_norm_min_max" with planet distances normalized using Min-Max method
sp = planets['Distance_AU']
planets['dist_norm_min_max'] = (sp - sp.min()) / (sp.max() - sp.min())

# TODO: Print the dataframe
print(f'Planets after Min-Max normalization: \n', planets)

# TODO: Construct a DataFrame with planets' names and their orbit radius
df = pd.DataFrame({
    "Planet": ['Mercury', 'Venus', 'Earth', 'Mars'],
    "Orbit Radius": [58, 108, 150, 228]
    })
print(f'DataFrame with planets names and their orbit radius: \n', df)

# TODO: Perform Min-Max Normalization on the orbit radius and print the DataFrame
sp = df['Orbit Radius']
df['Orbit_min_max'] = (sp - sp.min()) / (sp.max() - sp.min())
print(f'DataFrame after Min-Max normalization: \n', df)

# TODO: Perform Z-Score Normalization on the orbit radius and print the DataFrame
dist = df['Orbit Radius']
df['Orbit_Zscore'] = (dist - dist.mean()) / dist.std()
print(f'DataFrame after Z-score normalization: \n', df)