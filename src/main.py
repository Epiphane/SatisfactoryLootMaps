from data.creature_spawners import *
from data.crash_sites import *
from data.deposits import *
from data.berries import *
from data.spawns import *
from graphics import *
import sys

"""Variables for sizing / placing images correctly."""
DEF_ZOOM = 0.010
DIST_VAL = (1900/0.003)*DEF_ZOOM
DIST_SCALE = (130/0.003)*DEF_ZOOM

MAP_CONST = [-324400, 425000, -375000, 375000]

def run(output_name):
    """Executes graph / figure creation."""

    g = Graphics()

    sites = CrashSites()
    spawns = SpawnLocations()
    spawners = CreatureSpawners()
    deposits = Deposits()
    berries = Berries()

    g.create_graph()
    g.plot_background("../imgs/Biome_Map.png", MAP_CONST)

    # for poi in sites.poi_lst:
    #     g.place_poi(poi, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    for s in spawns.spawn_lst:
        g.place_spawn(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for d in deposits.depo_lst:
    #     g.place_deposit(d.coords, d.value, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    for b in berries.berry_lst:
        g.place_berry(b, DEF_ZOOM, DIST_VAL, DIST_SCALE)
    
    for s in spawners.spawner_lst:
        g.place_spawner(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    g.adjust_graph(MAP_CONST)

    # g.showfig()
    g.savefig(output_name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        run('output.png')
    else:
        run(sys.argv[1])
