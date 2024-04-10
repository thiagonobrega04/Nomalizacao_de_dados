import pandas as pd
df = pd.DataFrame({
    "Space Explorer": ['Spock', 'Kirk', 'McCoy', 'Scotty'],
    "Height": [183, 178, 170, 178]
})

# To normalize using Min-Max in Python, the corresponding code is:

df['Height'] = (df['Height'] - df['Height'].min()) / (df['Height'].max() - df['Height'].min())
print (df['Height'])
# After normalization, df['Height'] is [1, 0.61, 0, 0.61]

# For Z-Score:

df['Height'] = (df['Height'] - df['Height'].mean()) / df['Height'].std()
print(df['Height'])
# After normalization, df['Height'] is [1.07, 0.14, -1.35, 0.14]

# Choosing the Right Scaling Method
# Choosing the right normalization technique can be pivotal in obtaining accurate data analysis results. The right method primarily depends on the nature of your data and the specific requirements of your analyses.

# Use Min-Max Normalization when:
# .Your data is bounded and falls within a specific range.
# .The distribution is not normal, or the standard deviation is very small.
# .You're working with algorithms that require data to be on the same scale, like Neural Networks, or k-Nearest Neighbors.
# Example: Let's take an audio signal that has a minimum and maximum volume. Based on the concept of audio normalization, we want to rescale the signal to fit into a desired range, we would use Min-Max scaling here.

# Use Z-Score Normalization when:
# .The data is influenced by outliers as Z-Score is less sensitive to them.
# .The data is not uniformly distributed and you want to handle skewness.
# .You're dealing with techniques that assume data as centered, like Principal Component Analysis.
# Example: Suppose we have a dataset of student's scores which might contain extreme values (like a score of 100 or 0). To reduce this, we can use Z-Score normalization to identify and handle these score outliers.