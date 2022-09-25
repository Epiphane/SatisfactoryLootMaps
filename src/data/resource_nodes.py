from data.point_3d import *
from pandas import read_csv
import math

class ResourceNode:
    """ResourceNode - handles a single resource node"""
    
    def __init__(self, data) -> None:
        """Initializes resource node with data from resource node csv."""
        self.id = data['ID']
        self.type = data['Type']
        self.purity = data['Purity']
        self.coords = Point3D(data)

## Resource Node Locations
class ResourceNodes:
    """ResourceNodes - Handles resource_nodes.csv ."""

    def __init__(self) -> None:
        """Initializes all resource node locations after loading CSV data."""
        self.res_node_lst = []
        self.load_csv()
        self.populate_node_locations()

    def load_csv(self):
        """Loads csv data to variables."""
        self.node_loc = read_csv('../data/resource_nodes.csv')

    def populate_node_locations(self):
        """Creates a variable holding all resource node locations (from their respective data)."""
        
        for i in range(len(self.node_loc['X'])):
            row = self.node_loc.iloc[i]
            loc = ResourceNode(row)
            self.res_node_lst += [loc]

