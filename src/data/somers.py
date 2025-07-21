from data.point_3d import *
from pandas import read_csv
import math


## Berry Locations
class Somers:
    """Somers - Handles somers.csv ."""

    def __init__(self) -> None:
        """Initializes all somers locations after loading CSV data."""
        self.somers_lst = []
        self.load_csv()
        self.populate_somers_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.somers_loc = read_csv("data/1.0/somersloops.csv")

    def populate_somers_locations(self):
        """Creates a variable holding all somers locations (from their respective data)."""

        for i in range(len(self.somers_loc["X"])):
            row = self.somers_loc.iloc[i]
            loc = Point3D(row)
            self.somers_lst += [loc]
