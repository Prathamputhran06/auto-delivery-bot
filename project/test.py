import turtle
class Cell:
  def __init__(self, x, y):
    self.x = x
    self.y = y
def draw_grid_with_mapping(screen_width, screen_height, num_divisions_x, num_divisions_y):
  """
  Draws a grid of lines on the turtle screen and maps each cell with its coordinates.

  Args:
      screen_width: Width of the turtle screen.
      screen_height: Height of the turtle screen.
      num_divisions_x: Number of horizontal divisions (including axes).
      num_divisions_y: Number of vertical divisions (including axes).

  Returns:
      A dictionary mapping (x, y) coordinates to a cell object (optional) or None.
  """
  # Get the turtle object (assuming you already have it created)
  t = turtle.Turtle()
  t.penup()
  t.speed(0)  # Set speed to fastest

  # Calculate step size for both horizontal and vertical lines (adjusted for exact coordinates)
  step_x = screen_width / (num_divisions_x)
  step_y = screen_height / (num_divisions_y)

  # Create a dictionary to store cell mappings (optional)
  cell_map = {}

  # Draw vertical lines starting from leftmost coordinate (0, -screen_height/2)
  for i in range(num_divisions_x + 1):
    x = step_x * i - screen_width / 2
    t.goto(x, -screen_height / 2)
    t.pendown()
    t.goto(x, screen_height / 2)
    t.penup()

    # Add cell mapping (optional)
    for j in range(num_divisions_y + 1):
      y = step_y * j - screen_height / 2
      cell_map[(x, y)] = Cell(x, y)  # Replace with your desired cell information

  # Draw horizontal lines starting from bottommost coordinate (-screen_width/2, 0)
  for i in range(num_divisions_y + 1):
    y = step_y * i - screen_height / 2
    t.goto(-screen_width / 2, y)
    t.pendown()
    t.goto(screen_width / 2, y)
    t.penup()

  return cell_map

# Example usage: Assume screen size is 600x400 and want 5x4 grid divisions
screen_width = 600
screen_height = 400
num_divisions_x = 5
num_divisions_y = 4

# Get the turtle screen object (if not already done)
screen = turtle.Screen()
screen.setup(screen_width, screen_height)

# Draw the grid and get cell mapping (optional)
cell_map = draw_grid_with_mapping(screen_width, screen_height, num_divisions_x, num_divisions_y)

# Access cell information using coordinates (optional)
if cell_map:
  cell = cell_map[(step_x * 2 - screen_width / 2, step_y * 3 - screen_height / 2)]
  print(f"Cell at coordinates ({cell.x}, {cell.y})")

# Keep the window open until closed manually
turtle.done()
