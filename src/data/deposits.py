from data.point_3d import *
from pandas import read_csv
import math

class Deposit:
    """Deposit - Holds deposit information."""

    def __init__(self, data) -> None:
        """Initializes deposit with data from deposits csv."""
        self.coords = Point3D(data)
        self.value = data['Val']

## Deposit Locations
class Deposits:
    """Deposits - Handles all_deposits.csv ."""

    def __init__(self) -> None:
        """Initializes all deposits after loading CSV data."""
        self.depo_lst = []
        self.load_csv()
        self.populate_deposits()

    def load_csv(self) -> None:
        """Loads csv data to variables."""
        self.depo_csv = read_csv('../data/all_deposits.csv')

    def populate_deposits(self) -> None:
        """Creates a variable holding all deposits (from their respective data)."""
        
        for i in range(len(self.depo_csv['X'])):
            row = self.depo_csv.iloc[i]
            loc = Deposit(row)
            self.depo_lst += [loc]

