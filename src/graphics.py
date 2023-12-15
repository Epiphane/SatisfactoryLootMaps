from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
import numpy as np
import math


class Graphics:
    """Graphics Class - Handles all the drawing."""

    def __init__(self):
        """Initializes correlation between Sheet Value and Function."""
        self.offset = 1250
        self.item_draw = {
            "A": self.a_actual_loc,
            "B": self.b_circle_unique_doggo,
            "C": self.c_circle_unique_doggo_points,
            "D": self.d_circle_unique_reqs,
            "E": self.e_circle_unique_points,
            "F": self.f_circle_items_doggo,
            "G": self.g_circle_items_doggo_points,
            "H": self.h_circle_items_reqs,
            "I": self.i_circle_items_points,
            "J": self.j_circle_unique_doggo_points_noid,
            "K": self.k_circle_unique_points_noid,
            "L": self.l_circle_unique_reqs_noid,
            "M": self.m_circle_items_points_noid,
            "N": self.n_circle_items_reqs_noid,
            "O": self.o_circle_items_doggo_points_noid,
        }

    def create_graph(self):
        """Obtains subplots."""
        self.fig, self.ax = plt.subplots()
        plt.axis("off")

    def plot_background(self, img_path: str, const: list[int, int, int, int]):
        """Plots the background on self.ax given extent {const}."""
        img = plt.imread(img_path)
        self.ax.imshow(img, extent=const, origin="lower")

    def savefig(self, filename="output.png", dpi=1600):
        plt.savefig("../final/" + filename, dpi=dpi, bbox_inches="tight", pad_inches=0)

    def showfig(self):
        plt.show()

    def adjust_graph(self, const: list[int, int, int, int]):
        """Flips graph and set limits for Axes."""
        self.ax = plt.gca()
        self.ax.set_ylim(self.ax.get_ylim()[::-1])

        x_ticks = np.arange(const[0], const[1], 100000)
        plt.xticks(x_ticks, fontsize=5)

        y_ticks = np.arange(const[2], const[3], 100000)
        plt.yticks(y_ticks, fontsize=5)

    def get_image(self, path, zoom_val):
        return OffsetImage(plt.imread(path), zoom=zoom_val)

    def draw_img(self, path, zoom_val, x, y):
        """Draws image with given zoom value at (x, y)."""
        ab = AnnotationBbox(self.get_image(path, zoom_val), (x, y), frameon=False)
        self.ax.add_artist(ab)

    def draw_circle(self, x, y, radius, color="black", fill=False):
        """Draws a circle at (x, y) with given radius."""
        circle = plt.Circle((x, y), radius, linewidth=0.2, color=color, fill=fill)
        self.ax.add_artist(circle)

    def draw_txt(self, x, y, txt, rot=-20, size=0.28):
        """Draws text {txt} centered at (x, y) with given rotation."""
        props = {"ha": "center", "va": "center"}
        txt = plt.text(
            x, y, txt, props, size=size, color="black", rotation=rot, zorder=10
        )
        txt.set_path_effects([PathEffects.withStroke(linewidth=0.2, foreground="w")])

    #########################################
    #   CUSTOM FUNCTIONS FOR DATA DRAWING   #
    #########################################

    def place_poi(self, poi, zoom, dist, scale):
        zoom_val = zoom if poi.img == "HardDrive" else zoom / 2
        poi_path = "../imgs/" + poi.img + ".png"

        self.draw_img(poi_path, zoom_val, poi.x, poi.y)

        self.item_draw[poi.type](poi, zoom, dist, scale)

    def place_spawn(self, coords, zoom, dist, scale):
        self.draw_img("../imgs/BG.png", zoom / 4.3, coords.x, coords.y)
        self.draw_img("../imgs/loc.png", zoom / 3, coords.x, coords.y)

    def place_deposit(self, coords, value, zoom, dist, scale):
        zoom_val = zoom / 3 if int(value) == 21 else zoom * 0.9
        poi_path = "../imgs/" + str(int(value)) + ".png"
        self.draw_img(poi_path, zoom_val, coords.x, coords.y)

    def place_static_deposit(self, coords, value, zoom, dist, scale):
        if int(value) != 21:
            zoom_val = zoom / 4.5
            poi_path = "../imgs/chisel.png"
            self.draw_img(poi_path, zoom_val, coords.x, coords.y)

    def place_res_node(self, node, zoom, dist, scale):
        colors = {"Inpure": "red", "Normal": "darkorange", "Pure": "green"}
        ores = {
            "Desc_OreCopper_C": 2,
            "Desc_SAM_C": 8,
            "Desc_Stone_C": 0,
            "Desc_LiquidOil_C": 10,
            "Desc_OreIron_C": 1,
            "Desc_Coal_C": 3,
            "Desc_Sulfur_C": 5,
            "Desc_OreGold_C": 4,
            "Desc_RawQuartz_C": 6,
            "Desc_OreBauxite_C": 7,
            "Desc_OreUranium_C": 9,
        }
        coords = node.coords
        self.draw_circle(coords.x, coords.y, 2000, color=colors[node.purity], fill=True)
        self.draw_img(f"../imgs/{ores[node.type]}.png", zoom * 0.66, coords.x, coords.y)

    def place_rock(self, coords, zoom, dist, scale):
        self.draw_img("../imgs/rock.png", zoom / 4.9, coords.x, coords.y)

    def place_berry(self, coords, zoom, dist, scale):
        self.draw_img("../imgs/berry.png", zoom / 4.3, coords.x, coords.y)

    def place_spawner(self, spawner, zoom, dist, scale):
        drawable = ["Char_SpaceRabbit_C"]

        if spawner.species not in drawable:
            return

        species_dict = {
            "Char_SpaceGiraffe_C": ("SpaceGiraffe", 0.5),
            "Char_EliteCaveStinger_C": ("EliteCaveStinger", 1),
            "Char_CaveStinger_C": ("Stinger", 1),
            "Char_CaveStinger_Child_C": ("Stinger", 0.6),
            "Char_Stinger_C": ("Stinger", 1),
            "Char_Stinger_Child_C": ("Stinger", 0.6),
            "Char_SpaceRabbit_C": ("LizardDoggo", 0.45),
            "Char_Hog_C": ("Hog", 0.8),
            "Char_AlphaHog_C": ("AlphaHog", 1),
            "Char_Spitter_C": ("Spitter", 1),
            "Char_Spitter_Alternative_C": ("BlueSpitter", 1),
            "Char_Spitter_Small_C": ("Spitter", 0.7),
            "Char_NonFlyingBird_C": ("NonFlyingBird", 0.6),
            "Char_CrabHatcher_C": ("CrabHatcher", 1),
        }

        data = species_dict[spawner.species]
        zoom_val = zoom * data[1]
        spawner_path = f"../imgs/{data[0]}.png"

        self.draw_circle(spawner.coords.x, spawner.coords.y, spawner.spawn_radius)
        self.draw_img(spawner_path, zoom_val, spawner.coords.x, spawner.coords.y)

        txt = ""
        if spawner.max != 1:
            txt = f"{spawner.min}"
            if spawner.min != spawner.max:
                txt += f" - {spawner.max}"

        self.draw_txt(spawner.coords.x, spawner.coords.y - 50, txt, size=0.4)

    ####################################
    #   CUSTOM FUNCTIONS FOR DRAWING   #
    ####################################

    def circle_plot_items(self, poi, zoom, dist, scale, poi_x, poi_y):
        """Draws a circle and all items corresponding to crash site (in a circle - multiple stacks of same item)."""
        self.draw_circle(poi_x, poi_y, zoom * 1300000)

        item_ct = poi.total_items
        curr_item = 0

        for item_type in poi.items:
            item_data = poi.items[item_type]
            item_img = "../imgs/" + item_type + ".png"

            for stack_num in range(item_data[0]):
                x = poi_x + (dist + scale * item_ct) * math.cos(
                    (math.pi * curr_item) / (float(item_ct) / 2.0)
                )
                y = poi_y + (dist + scale * item_ct) * math.sin(
                    (math.pi * curr_item) / (float(item_ct) / 2.0)
                )

                self.draw_img(item_img, zoom, x, y)
                curr_item += 1

    def circle_plot_unique(self, poi, zoom, dist, scale, poi_x, poi_y):
        """
        Draws a circle and one of each type of item corresponding to crash site (in a circle).
        Writes total number of each item type.
        """
        self.draw_circle(poi_x, poi_y, zoom * 1300000)

        item_ct = len(poi.items)
        curr_item = 0

        for item_type in poi.items:
            item_data = poi.items[item_type]
            item_img = "../imgs/" + item_type + ".png"

            x = poi_x + (dist + scale * item_ct) * math.cos(
                (math.pi * curr_item) / (float(item_ct) / 2.0)
            )
            y = poi_y + (dist + scale * item_ct) * math.sin(
                (math.pi * curr_item) / (float(item_ct) / 2.0)
            )

            self.draw_img(item_img, zoom, x, y)
            self.draw_txt(x, y, item_data[1])
            curr_item += 1

    def doggo_draw(self, poi, zoom, dist, scale):
        self.draw_img(
            "../imgs/" + poi.img + ".png",
            zoom / 2,
            poi.x + poi.x_off,
            poi.y + poi.y_off,
        )
        self.draw_txt(poi.x, poi.y, poi.id)

    def a_actual_loc(self, poi, zoom, dist, scale):
        """Draws all items at actual coordinates."""
        for item in poi.item_lst:
            item_img = "../imgs/" + item[0] + ".png"

            self.draw_img(item_img, zoom, item[2], item[3])

    def b_circle_unique_doggo(self, poi, zoom, dist, scale):
        """Draws unique items in a circle for a Doggo."""
        self.circle_plot_unique(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(poi.x + poi.x_off, poi.y + poi.y_off, poi.id)
        self.doggo_draw(poi, zoom, dist, scale)

    def c_circle_unique_doggo_points(self, poi, zoom, dist, scale):
        """Draws unique items in a circle for doggo, along with Loot Points Estimate."""
        self.circle_plot_unique(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(poi.x + poi.x_off, poi.y + poi.y_off - self.offset, poi.id)
        self.draw_txt(
            poi.x + poi.x_off,
            poi.y + poi.y_off + self.offset,
            str(poi.points // 1000) + "k",
        )
        self.doggo_draw(poi, zoom, dist, scale)

    def d_circle_unique_reqs(self, poi, zoom, dist, scale):
        """Draws unique items in a circle. Writes HD ID and Requirements."""
        self.circle_plot_unique(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y - self.offset, poi.id)
        self.draw_txt(poi.x, poi.y + self.offset, poi.req)

    def e_circle_unique_points(self, poi, zoom, dist, scale):
        """Draws unique items in a circle. Writes HD ID and Loot Points Estimate."""
        self.circle_plot_unique(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y - self.offset, poi.id)
        self.draw_txt(poi.x, poi.y + self.offset, str(poi.points // 1000) + "k")

    def f_circle_items_doggo(self, poi, zoom, dist, scale):
        """Draws item entities in a circle for doggo."""
        self.circle_plot_items(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(poi.x + poi.x_off, poi.y + poi.y_off, poi.id)
        self.doggo_draw(poi, zoom, dist, scale)

    def g_circle_items_doggo_points(self, poi, zoom, dist, scale):
        """Draws unique items in a circle for doggo. Also writes Loot Points Estimate."""
        self.circle_plot_items(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(poi.x + poi.x_off, poi.y + poi.y_off - self.offset, poi.id)
        self.draw_txt(poi.x + poi.x_off, poi.y + poi.y_off + self.offset, poi.points)
        self.doggo_draw(poi, zoom, dist, scale)

    def h_circle_items_reqs(self, poi, zoom, dist, scale):
        """Draws unique items in a circle. Writes HD ID and Requirements."""
        self.circle_plot_items(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y - self.offset, poi.id)
        self.draw_txt(poi.x, poi.y + self.offset, poi.req)

    def i_circle_items_points(self, poi, zoom, dist, scale):
        """Draws unique items in a circle. Writes HD ID and Loot Points Estimate."""
        self.circle_plot_items(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y - self.offset, poi.id)
        self.draw_txt(poi.x, poi.y + self.offset, poi.points)

    def j_circle_unique_doggo_points_noid(self, poi, zoom, dist, scale):
        """Draws unique items in a circle for doggo, along with Loot Points Estimate (no ID)."""
        self.circle_plot_unique(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(
            poi.x + poi.x_off, poi.y + poi.y_off, str(poi.points // 1000) + "k"
        )
        self.doggo_draw(poi, zoom, dist, scale)

    def k_circle_unique_points_noid(self, poi, zoom, dist, scale):
        """Draws unique items in a circle. Writes HD Loot Points Estimate (no ID)."""
        self.circle_plot_unique(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y, str(poi.points // 1000) + "k")

    def l_circle_unique_reqs_noid(self, poi, zoom, dist, scale):
        """Draws unique items in a circle. Writes HD Requirements (no ID)"""
        self.circle_plot_unique(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(poi.x, poi.y, poi.req)

    def m_circle_items_points_noid(self, poi, zoom, dist, scale):
        """Draws all items in a circle. Writes HD Loot Points Estimate (no ID)."""
        self.circle_plot_items(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y, str(poi.points // 1000) + "k")

    def n_circle_items_reqs_noid(self, poi, zoom, dist, scale):
        """Draws all items in a circle. Writes HD Requirements (no ID)"""
        self.circle_plot_items(poi, zoom, dist, scale, poi.x, poi.y)
        self.draw_txt(poi.x, poi.y, poi.req)

    def o_circle_items_doggo_points_noid(self, poi, zoom, dist, scale):
        """Draws all items in a circle for doggo, along with Loot Points Estimate (no ID)."""
        self.circle_plot_items(
            poi, zoom, dist, scale, poi.x + poi.x_off, poi.y + poi.y_off
        )
        self.draw_txt(
            poi.x + poi.x_off, poi.y + poi.y_off, str(poi.points // 1000) + "k"
        )
        self.doggo_draw(poi, zoom, dist, scale)
