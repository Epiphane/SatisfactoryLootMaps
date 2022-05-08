from graphics import *
from data import *

"""Variables for sizing / placing images correctly."""
DEF_ZOOM = 0.010
DIST_VAL = (1900/0.003)*DEF_ZOOM
DIST_SCALE = (130/0.003)*DEF_ZOOM

MAP_CONST = [-324400, 425000, -375000, 375000]

def run():
    """Executes graph / figure creation."""

    g = Graphics()
    d = Data()

    g.create_graph()
    g.plot_background("imgs/Biome_Map.png", MAP_CONST)

    for poi in d.poi_lst:
        g.place_poi(poi, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    g.adjust_graph(MAP_CONST)

    # g.showfig()
    g.savefig()

if __name__ == '__main__':
    run()
