import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define file paths
data_file = '/home/ubuntu/project_data_balancing/data.csv'
output_txt = '/home/ubuntu/project_data_balancing/class_distribution.txt'
output_png = '/home/ubuntu/project_data_balancing/class_distribution.png'

# Load the dataset
# The dataset uses ';' as a separator
df = pd.read_csv(data_file, sep=';')

# Identify the target column (last column)
target_column = df.columns[-1]
print(f"Target column identified as: {target_column}")

# Analyze class distribution
class_counts = df[target_column].value_counts()
print("\nClass Distribution:")
print(class_counts)

# Save class distribution to a text file
with open(output_txt, 'w') as f:
    f.write(f"Target column: {target_column}\n\n")
    f.write("Class Distribution:\n")
    f.write(class_counts.to_string())
print(f"\nClass distribution saved to {output_txt}")

# Visualize class distribution
plt.figure(figsize=(8, 6))
sns.countplot(x=target_column, data=df, palette='viridis', order=class_counts.index)
plt.title('Class Distribution of Student Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Number of Students')

# Add counts on top of bars
for index, value in enumerate(class_counts):
    plt.text(index, value + 10, str(value), ha='center') # Add 10 for spacing

plt.tight_layout()
plt.savefig(output_png)
print(f"Class distribution visualization saved to {output_png}")

print("\nAnalysis complete.")

