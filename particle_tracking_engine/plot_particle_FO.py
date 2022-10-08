import numpy as np
from particle_tracking_engine.Tidal_data import tidal_data
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import matplotlib.colors as Cmap
from matplotlib import  dates
import seaborn as sns

class plotting_particles:
    '''Class for plotting particles'''

    def __init__(self, map, area=None):

        # DATA = tidal_data()

        self.FO_map = map
        self.area = area
        if self.area is not None:
            self.mark_A(area)

    def plot_particle(self, x_track, y_track, fig=None, ax=None):

        if self.area == None:
            cmap = Cmap.ListedColormap(['gray', 'white'])
        else:
            cmap = Cmap.ListedColormap(['green', 'white', 'red'])

        if ax is None:
            if fig is None:
                fig, ax = plt.subplots()
            else:
                fig.add_subplot(111)

        Xlims = np.array([115, 595])
        Ylims = np.array([793, 1200])

        ax.set_xlim(Xlims)
        ax.set_ylim(Ylims)
        ax.yaxis.set_visible(False)
        ax.xaxis.set_visible(False)
        # y_land,x_land = np.where(self.FO_map==0)
        # ax.plot(x_land,y_land,'og',markersize=0.1)
        ax.imshow(self.FO_map, cmap=cmap)

        for x, y in zip(x_track, y_track):
            ax.plot(x[0], y[0], '.', markersize=0.2)
            ax.plot(x[0][0], y[0][0], 'rx')
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.05,
                            hspace=0.1)
        # ax[0].legend(loc="upper left", fontsize=15)
        fig.set_size_inches(11.69, 8.27)
        plt.title('Á sjógv kl. 09 tann 07-okt-2022 og 35 tímar fram')
        fig.savefig('Leiting_kl_09_35.png', bbox_inches='tight')

    def plot_particle_tracks(self, x_track, y_track, timestamp=0,color='blue', fig=None, ax=None):

        if ax is None:
            if fig is None:
                fig, ax = plt.subplots()
            else:
                fig.add_subplot(111)

        Xlims = np.array([0, 1088])
        Ylims = np.array([0, 1488])

        ax.set_xlim(Xlims)
        ax.set_ylim(Ylims)

        lines = []

        if len(x_track)!=0:
            lines.extend(ax.plot(x_track.iloc[-1], y_track.iloc[-1], 'o', c=color, markersize=4))
        lines.extend(ax.plot(x_track.iloc[0::50], y_track.iloc[0::50], '-',c=color, markersize=7))
        return lines

       #ax.plot(x[0][0], y[0][0], 'rx')

    def plot_particle_origin(self, x_pos, y_pos):

        cmap = Cmap.ListedColormap(['green', 'white', 'red'])
        fig, ax = plt.subplots()

        Xlims = np.array([0, 1088])
        Ylims = np.array([0, 1488])

        ax.set_xlim(Xlims)
        ax.set_ylim(Ylims)

        ax.imshow(self.FO_map, cmap=cmap)

        for x, y in zip(x_pos, y_pos):
            ax.plot(x, y, 'rx')

    def plot_sea_born_map(self, data,fig=None, ax=None):

        if self.area == None:
            cmap = Cmap.ListedColormap(['gray', 'white'])
        else:
            cmap = Cmap.ListedColormap(['green', 'white', 'red'])

        if ax is None:
            if fig is None:
                fig, ax = plt.subplots()
            else:
                fig.add_subplot(111)

        Xlims = np.array([115, 595])
        Ylims = np.array([793, 1200])

        ax.set_xlim(Xlims)
        ax.set_ylim(Ylims)
        sns.kdeplot(data=data, x='x', y='y', color='r', fill=True,
                    cmap="Reds", thresh=.3, alpha=0.5);

        ax.imshow(self.FO_map, cmap=cmap)

        for x, y in zip(data.x, data.y):
            ax.plot(x, y, 'rx')
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.05,
                            hspace=0.1)
        # ax[0].legend(loc="upper left", fontsize=15)
        fig.set_size_inches(11.69, 8.27)
        plt.title('Á sjógv kl. 09 tann 07-okt-2022 og 35 tímar fram')
        fig.savefig('Leiting_kl_09_35_seaborn.png', bbox_inches='tight')

    def mark_A(self, areas):

        for i, areas in enumerate(areas):
            minx = min(areas[0]).astype(int)
            miny = min(areas[1]).astype(int)
            maxx = np.ceil(max(areas[0])).astype(int)
            maxy = np.ceil(max(areas[1])).astype(int)

            coord = [(areas[0][j], areas[1][j]) for j in range(len(areas[0]))]
            self.area = Polygon(coord)
            xr = np.arange(minx, maxx)
            yr = np.arange(miny, maxy)
            for idx, x in enumerate(xr):
                for ide, y in enumerate(yr):
                    if self.area.contains(Point(x, y)):
                        self.FO_map[y, x] = i + 2
