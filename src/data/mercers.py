from data.point_3d import *
from pandas import read_csv
import math


## Mercers Locations
class Mercers:
    """Mercers - Handles Mercers.csv ."""

    def __init__(self) -> None:
        """Initializes all mercers locations after loading CSV data."""
        self.mercer_lst = []
        self.load_csv()
        self.populate_mercer_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.mercer_loc = read_csv("data/1.0/mercers.csv")

    def populate_mercer_locations(self):
        """Creates a variable holding all mercer locations (from their respective data)."""

        for i in range(len(self.mercer_loc["X"])):
            row = self.mercer_loc.iloc[i]
            loc = Point3D(row)
            self.mercer_lst += [loc]
