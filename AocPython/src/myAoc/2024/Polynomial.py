import numpy as np

# Given data
numbers = [
    11, 15, 21, 33, 48, 78, 119, 172, 238, 360, 582, 867, 1314, 1977,
    3000, 4583, 6911, 10519, 15867, 24026, 36851, 55895, 84739, 128449,
    194782, 297298, 450541, 683900, 1040094,1576166
]

# Step 1: Compute differences
diffs = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]

# Step 2: Fit exponential growth model
x = np.arange(len(diffs))
y = np.array(diffs)

# Fit an exponential model: y = c1 * k^x
log_y = np.log(y)  # Take log of y to linearize the exponential equation
coeffs = np.polyfit(x, log_y, 1)  # Linear fit: log(y) = a*x + b
k = np.exp(coeffs[0])  # Base of the exponential (e^a)
c1 = np.exp(coeffs[1])  # Coefficient (e^b)

# Predict value for item 74
n = 74
predicted_value = c1 * (k ** n)
print(f"c1: {c1}")
print(f"k: {k}")

# Print results
print(f"Exponential model: a_n = {c1:.3f} * ({k:.3f})^n")
print(f"Predicted value for item 74: {predicted_value:.2f}")