import numpy as np

def calculate_distance(point1, point2):
  """
  Calculates the Euclidean distance between two points in a 2D plane using NumPy.

  Args:
    point1: A list or NumPy array representing the coordinates of the first point (e.g., [x1, y1]).
    point2: A list or NumPy array representing the coordinates of the second point (e.g., [x2, y2]).

  Returns:
    The Euclidean distance between the two points.
    Returns None if the input points are not 2-dimensional.
  """
  point1_np = np.array(point1)
  point2_np = np.array(point2)

  if point1_np.shape != (2,) or point2_np.shape != (2,):
    print("Error: Input points must be 2-dimensional (e.g., [x, y]).")
    return None

  distance = np.linalg.norm(point1_np - point2_np)
  return distance

if __name__ == "__main__":
  print("Simple 2D Distance Calculator")
  print("-" * 30)

  # Get input from the user
  try:
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    point1 = [x1, y1]

    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    point2 = [x2, y2]

    # Calculate the distance
    distance = calculate_distance(point1, point2)

    # Display the result
    if distance is not None:
      print(f"\nThe distance between point {point1} and point {point2} is: {distance:.2f}")

  except ValueError:
    print("Error: Please enter valid numerical coordinates.")