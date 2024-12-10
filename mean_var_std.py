import numpy as np


def calculate(list):
    # Ensure the list contains exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)

    # Calculate statistics
    mean_val = [matrix.mean(axis=0).tolist(), matrix.mean(
        axis=1).tolist(), matrix.mean().tolist()]
    variance_val = [matrix.var(axis=0).tolist(), matrix.var(
        axis=1).tolist(), matrix.var().tolist()]
    std_val = [matrix.std(axis=0).tolist(), matrix.std(
        axis=1).tolist(), matrix.std().tolist()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(
        axis=1).tolist(), matrix.max().tolist()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(
        axis=1).tolist(), matrix.min().tolist()]
    sum_val = [matrix.sum(axis=0).tolist(), matrix.sum(
        axis=1).tolist(), matrix.sum().tolist()]

    # Return a dictionary with all the calculated statistics
    return {
        'mean': mean_val,
        'variance': variance_val,
        'standard deviation': std_val,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }


result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
