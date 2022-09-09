from data.point_3d import *
from pandas import read_csv
import math

## Berry Locations
class Berries:
    """Berries - Handles berries.csv ."""

    def __init__(self) -> None:
        """Initializes all berry locations after loading CSV data."""
        self.berry_lst = []
        self.load_csv()
        self.populate_berry_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.berry_loc = read_csv('../data/berries.csv')

    def populate_berry_locations(self):
        """Creates a variable holding all berry locations (from their respective data)."""
        
        for i in range(len(self.berry_loc['X'])):
            row = self.berry_loc.iloc[i]
            loc = Point3D(row)
            self.berry_lst += [loc]

