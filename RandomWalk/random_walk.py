from random import choice


class Randomwalk:
    """A class to generate random walk."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taling steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

    def get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice(range(1, 500))
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice(range(1, 500))
        y_step = y_direction * y_distance

        # Calculate the new position.
        x = self.x_values[-1] + x_step
        y = self.y_values[-1] + y_step

        self.x_values.append(x)
        self.y_values.append(y)

        return x_step, y_step
