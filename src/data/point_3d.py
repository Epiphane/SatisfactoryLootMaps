
class Point3D:
    """Point3D - Parent Class managing a 3d coordinate"""

    def __init__(self, data) -> None:
        """Initializes Point3D with given data."""
        self.x = float(data['X'])
        self.y = float(data['Y'])
        self.z = float(data['Z'])

