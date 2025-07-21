from data.point_3d import *
from pandas import read_csv
import math


## Slug Locations
class Slugs:
    """Somers - Handles somers.csv ."""

    def __init__(self) -> None:
        """Initializes all somers locations after loading CSV data."""
        self.blue_lst = []
        self.yellow_lst = []
        self.purple_lst = []
        self.load_csv()
        self.populate_slug_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.slugs_loc = read_csv("data/1.0/slugs.csv")

    def populate_slug_locations(self):
        """Creates a variable holding all slug locations (from their respective data)."""

        for i in range(len(self.slugs_loc["X"])):
            row = self.slugs_loc.iloc[i]
            loc = Point3D(row)
            if row["Item ID"] == "blue":
                self.blue_lst += [loc]
            elif row["Item ID"] == "yellow":
                self.yellow_lst += [loc]
            elif row["Item ID"] == "purple":
                self.purple_lst += [loc]
            else:
                print("Unknown ID - HELP")
