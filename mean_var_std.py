import numpy as np

def calculate(list):

  # Raise Error if length of list is not equal to 9
  if (len(list) !=9):
    raise ValueError("List must contain nine numbers.")

  # Set Up Variables
  
  matrix = np.array(list).reshape((3,3))

  mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), np.mean(matrix)]
  var = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), np.var(matrix)]
  std = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), np.std(matrix)]
  my_max = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), np.max(matrix)]
  my_min = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), np.min(matrix)]
  my_sum = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), np.sum(matrix)]

  return {
    "mean": mean,
    "variance": var,
    "standard deviation": std,
    "max": my_max,
    "min": my_min,
    "sum": my_sum
  }
