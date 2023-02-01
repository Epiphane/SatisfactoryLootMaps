from data.point_3d import *
from pandas import read_csv
import math

class Spawner:
    """Spawner - handles a single creature spawner"""
    
    def __init__(self, data) -> None:
        """Initializes spawner with data from spawner csv."""
        self.id = data['ID']
        self.species = data['Species']
        self.coords = Point3D(data)
        self.spawn_radius = float(data['Radius'])
        self.min = int(data['Min'])
        self.max = int(data['Max'])

## CreatureSpawners Locations
class CreatureSpawners:
    """CreatureSpawners - Handles creatures.csv ."""

    def __init__(self) -> None:
        """Initializes all spawner locations after loading CSV data."""
        self.spawner_lst = []
        self.load_csv()
        self.populate_spawner_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.spawner_loc = read_csv('../data/U5/creatures.csv')

    def populate_spawner_locations(self):
        """Creates a variable holding all spawner locations (from their respective data)."""
        
        for i in range(len(self.spawner_loc['X'])):
            row = self.spawner_loc.iloc[i]
            loc = Spawner(row)
            self.spawner_lst += [loc]

