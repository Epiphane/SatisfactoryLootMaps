from pandas import read_csv
import math

## Item Vals
sink_vals = {
    "AluminumPlateReinforced": 2804,
    "Battery": 465,
    "Cable": 24,
    "CircuitBoard": 696,
    "CircuitBoardHighSpeed": 920,
    "Computer": 17260,
    "ComputerSuper": 99576,
    "HighSpeedConnector": 3776,
    "IronPlateReinforced": 120,
    "IronScrew": 2,
    "ModularFrame": 408,
    "ModularFrameHeavy": 11520,
    "ModularFrameLightweight": 32908,
    "Motor": 1520,
    "SteelPlateReinforced": 632,
    "Wire": 6
}

## Hard Drives
make_float = lambda i: float("".join(str(i).split(',')))

class PointOfInterest:
    """Point Of Interest - Holds nearby loot data."""

    def __init__(self, hd_data):
        """Initializes POI with given data from hard drive spreadsheet."""
        self.name = hd_data['Name']
        self.alt = hd_data['Altitude']
        self.x = make_float(hd_data['X'])
        self.y = make_float(hd_data['Y'])
        self.req = hd_data['Req']
        self.id = hd_data['ID']
        self.img = hd_data['IMG']
        self.type = hd_data['Type']
        self.x_off = make_float(hd_data['X_Off'])
        self.y_off = make_float(hd_data['Y_Off'])
        self.total_items = 0
        self.items = dict()
        self.item_lst = []
        self.points = 0

    def add_item(self, item_type, amount, x, z):
        """Adds item data to POI."""
        self.total_items += 1
        self.item_lst += [(item_type, amount, x, z)]
        if item_type in sink_vals:
            self.points += sink_vals[item_type] * amount
        if item_type in self.items:
            self.items[item_type][0] += 1
            self.items[item_type][1] += amount
        else:
            self.items[item_type] = [1, amount]


class Data:
    """Data - Handles hard_drives.csv and loot_points.csv spreadsheets."""

    def __init__(self):
        """Initializes all POI after loading CSV data."""
        self.load_csv()
        self.populate_poi()
        self.populate_poi_with_items()

    def load_csv(self):
        """Loads csv data to variables."""
        self.lp = read_csv('data/loot_points.csv')
        self.hd = read_csv('data/hard_drives.csv')

    def populate_poi(self):
        """Creates a variable holding all populated POI (from their respective data)."""
        self.poi_lst = []
        for i in range(len(self.hd['X'])):
            row = self.hd.iloc[i]
            poi = PointOfInterest(row)
            self.poi_lst += [poi]

    def populate_poi_with_items(self):
        """Populates POI with items based on closest POI to item."""
        for i in range(len(self.lp['X'])):
            row = self.lp.iloc[i]
            lp_x = row['X']
            lp_y = row['Y']
            lp_z = row['Z']
            min_dist = 999999999
            pod_num = -1
            
            # Iterate to find closest drive
            for index, poi in enumerate(self.poi_lst):
                # dst = math.dist([lp_x, lp_y, lp_z], [poi.x, poi.y, poi.alt * 100])
                dst = math.dist([lp_x, lp_y], [poi.x, poi.y])
                if dst < min_dist:
                    min_dist = dst
                    pod_num = index
            
            closest_poi = self.poi_lst[pod_num]
            lp_type = row['Item Type']
            lp_amount = row['Amount']
            lp_x = row['X']
            lp_z = row['Y']
            closest_poi.add_item(lp_type, lp_amount, lp_x, lp_z)
