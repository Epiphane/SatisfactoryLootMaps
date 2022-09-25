from data.point_3d import *
from pandas import read_csv
import math

## Large Rocks Locations
class LargeRocks:
    """LargeRocks - Handles destr_rocks.csv ."""

    def __init__(self) -> None:
        """Initializes all large destructible rock locations after loading CSV data."""
        self.rock_lst = []
        self.load_csv()
        self.populate_rock_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.rock_loc = read_csv('../data/destr_rocks.csv')

    def populate_rock_locations(self):
        """Creates a variable holding all rock locations (from their respective data)."""
        
        for i in range(len(self.rock_loc['X'])):
            row = self.rock_loc.iloc[i]
            loc = Point3D(row)
            self.rock_lst += [loc]

