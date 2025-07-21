from data.point_3d import *
from pandas import read_csv
import math

## Player Spawn Locations
class SpawnLocations:
    """Spawn Locations - Handles sample_spawns.csv ."""

    def __init__(self) -> None:
        """Initializes all SpawnLocation samples after loading CSV data."""
        self.spawn_lst = []
        self.load_csv()
        self.populate_spawn_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.spawn_loc = read_csv('data/U5/sample_spawns.csv')

    def populate_spawn_locations(self):
        """Creates a variable holding all player spawn locations (from their respective data)."""
        
        for i in range(len(self.spawn_loc['X'])):
            row = self.spawn_loc.iloc[i]
            loc = Point3D(row)
            self.spawn_lst += [loc]

