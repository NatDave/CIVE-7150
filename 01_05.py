import pandas as pd

# Read the dataset
house_data = pd.read_csv('kc_house_data.csv')

# Drop irrelevant columns
house_data = house_data.drop(['id', 'date', 'zipcode'], axis=1)

# set the response
response = 'price'

# Initialize variables for lowest and highest average and variance
feature_lo_avg = None
feature_hi_avg = None
feature_lo_var = None
feature_hi_var = None

lo_avg = float('inf')
hi_avg = float('-inf')
lo_var = float('inf')
hi_var = float('-inf')

# Display feature names
features = house_data.columns.drop(response)
print("Feature Statistics:")
for feature in features:
    # Compute average, min, max, and variance
    average = house_data[feature].mean()
    min_value = house_data[feature].min()
    max_value = house_data[feature].max()
    variance = house_data[feature].var()

    # Update lowest and highest average
    if average < lo_avg:
      lo_avg = average
      feature_lo_avg = feature
    if average > hi_avg:
      hi_avg = average
      feature_hi_avg = feature

    # Update lowest and highest variance
    if variance < lo_var:
        lo_var = variance
        lowest_var_feature = feature
    if variance > hi_var:
        hi_var = variance
        highest_var_feature = feature

    # Display statistics
    print(f"\nFeature: {feature}")
    print(f"Average: {average:.2f}")
    print(f"Min Value: {min_value}")
    print(f"Max Value: {max_value}")
    print(f"Variance: {variance:.2f}")

# Display features with lowest and highest average
print(f"\nFeature with Lowest Average: {feature_lo_avg} ({lo_avg:.2f})")
print(f"Feature with Highest Average: {feature_hi_avg} ({hi_avg:.2f})")

# Display features with lowest and highest variance
print(f"\nFeature with Lowest Variance: {lowest_var_feature} ({lo_var:.2f})")
print(f"Feature with Highest Variance: {highest_var_feature} ({hi_var:.2f})")

# Compute correlation coefficients
correlation_table = house_data.corr()[[response]].drop(response)
correlation_table.columns = ['Corr. Coeff.']

# Display the correlation table
print("\nCorrelation Coefficient with Response")
print(correlation_table)

# Feature with the highest positive correlation
highest_positive_correlation_feature = correlation_table['Corr. Coeff.'].idxmax()
highest_positive_correlation_value = correlation_table['Corr. Coeff.'].max()
print("\nFeature with Highest Positive Correlation:")
print(f"{highest_positive_correlation_feature} ({highest_positive_correlation_value:.6f})")