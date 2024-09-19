"""Main file for running the program."""

import sys
from data.creature_spawners import CreatureSpawners
from data.resource_nodes import ResourceNodes
from data.large_rocks import LargeRocks
from data.crash_sites import CrashSites
from data.spawns import SpawnLocations
from data.deposits import Deposits
from data.berries import Berries
from data.mercers import Mercers
from data.somers import Somers
from graphics import Graphics
from data.slugs import Slugs

DEF_ZOOM = 0.010
DIST_VAL = (1900 / 0.003) * DEF_ZOOM
DIST_SCALE = (130 / 0.003) * DEF_ZOOM

MAP_CONST = [-324400, 425000, -375000, 375000]


def run(output_name):
    """Executes graph / figure creation."""

    g = Graphics()

    sites = CrashSites()
    spawns = SpawnLocations()
    spawners = CreatureSpawners()
    somers = Somers()
    mercers = Mercers()
    slugs = Slugs()
    deposits = Deposits()
    berries = Berries()
    nodes = ResourceNodes()
    rocks = LargeRocks()

    g.create_graph()
    g.plot_background("../imgs/Biome_MapU7.png", MAP_CONST)

    # for s in slugs.blue_lst:
    #     g.place_blue_slug(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for s in slugs.yellow_lst:
    #     g.place_yellow_slug(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    for s in slugs.purple_lst:
        g.place_purple_slug(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    for poi in sites.poi_lst:
        g.place_poi(poi, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    for m in mercers.mercer_lst:
        g.place_mercer(m, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    for s in somers.somers_lst:
        g.place_somer(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for s in spawns.spawn_lst:
    #     g.place_spawn(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for n in nodes.res_node_lst:
    #     g.place_res_node(n, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for r in rocks.rock_lst:
    #     g.place_rock(r, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for d in deposits.depo_lst:
    #     g.place_static_deposit(d.coords, d.value, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for d in deposits.depo_lst:
    #     g.place_deposit(d.coords, d.value, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for b in berries.berry_lst:
    #     g.place_berry(b, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    # for s in spawners.spawner_lst:
    #     g.place_spawner(s, DEF_ZOOM, DIST_VAL, DIST_SCALE)

    g.adjust_graph(MAP_CONST)

    g.savefig(output_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        run("output.png")
    else:
        run(sys.argv[1])
