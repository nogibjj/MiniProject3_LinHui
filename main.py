import polars as pl
import matplotlib.pyplot as plt

# Read data into a Polars DataFrame
df = pl.read_csv('AAPL.csv')

# print(df.head())

# Calculate summary statistics
summary_stats = df.describe()
print(summary_stats)

# Add median row to the summary statistics
median = df.median()

print(summary_stats, median)

# Create a line plot of Open prices
plt.plot(df['Open'])
plt.xticks(rotation=20)
plt.xlabel('Number of days')
plt.ylabel('Open Price')
plt.title('Open price for AAPL in the past year')
plt.savefig('Open price figure with Polars.png')
plt.show()






