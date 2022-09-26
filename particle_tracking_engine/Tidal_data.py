import numpy as np
import pandas as pd
import numpy.matlib as npm
import time

class tidal_data:

    def __init__(self):
        '''
        Import data from files
        '''

        # K1,M4,S2,N2 og O1
        filenum = ['M2','S2','K1','N2','O1','M4'] # array created to indentify and specify filename
        L = 1488; # length of data matrix
        W = 1088; # width of data matrix
        n = 6; # Nr.of different tidal constituents
        self.Inc = np.zeros((L, W, n)) # Incline ??  # make a small explanation of each component
        self.Maj = np.zeros((L, W, n)) # Major ??
        self.Min = np.zeros((L, W, n)) # Minor ??
        #self.Pha = np.zeros((L, W, n)) # Phase ??

        self.inc = {}
        self.maj = {}
        self.min = {}
        self.Pha = {}

    #= == == == == =Inc == == == == == ==
        for idx,con in enumerate(filenum):
            filename = f'tidal_constituents_data/Cur_Inc_{con}.npy'
            A = np.load(filename)

            # Importing data
            A = A * (np.pi / 180) # Converting Dat to radians

            self.Inc[:,:, idx] = A
            self.inc[f'{con}'] = A

            # This is repeated for Major, Minor and Phase
    #= == == == == == = Maj == == == == == == == == == == == == ==
            filename = f'tidal_constituents_data/Cur_Maj_{con}.npy'
            B = np.load(filename)

            self.Maj[:,:, idx] = B
            self.maj[f'{con}'] = B

    #= == == == == == == Min == == == == == == == == =
            filename = f'tidal_constituents_data/Cur_Min_{con}.npy'
            C = np.load(filename)
            self.Min[:,:, idx] = C
            self.min[f'{con}'] = C

    #= == == == == == == Pha == == == == == == == == == == ==
            filename = f'tidal_constituents_data/Cur_Pha_{con}.npy'
            D = np.load(filename)

            D = D * (np.pi / 180) # Converting Dat to radians

            # self.Pha[:,:, g] = D
            self.Pha[f'{con}'] = D


    #= == == == == = residual U == == == == == ==
        self.ResU = np.load('tidal_constituents_data/Residual_Ubar.npy')
    #= == == == == = residual V == == == == == ==
        self.ResV = np.load('tidal_constituents_data/Residual_Vbar.npy')

    #= == == == optimizing the calculation by adding matrixes togeher before the time loop
    #= == == == = M2 == == ==
        self.M_u1 = np.zeros((6, 1488, 1088))
        self.M_u2 = np.zeros((6, 1488, 1088))
        self.M_v1 = np.zeros((6, 1488, 1088))
        self.M_v2 = np.zeros((6, 1488, 1088))
        self.Pha_all = np.zeros((6, 1488, 1088))
        for idx,constuient in enumerate(filenum):
            self.M_u1[idx, :, :] = np.multiply(self.maj[constuient], np.cos(self.inc[constuient]))
            self.M_u2[idx, :, :] = np.multiply(self.min[constuient], np.sin(self.inc[constuient]))
            self.M_v1[idx, :, :] = np.multiply(self.maj[constuient], np.sin(self.inc[constuient]))
            self.M_v2[idx, :, :] = np.multiply(self.min[constuient], np.cos(self.inc[constuient]))
            self.Pha_all[idx, :, :] = np.array(self.Pha[constuient])


        # = == == grid data == == == == =
        self.length = 148800  # m
        self.width = 108800  # m
        self.dz = 100  # m

        self.MajM2 = self.maj['M2']  # for defining land in the matrix

        '''
        # = == == == = land or not land matrix == == == ==
        A = self.MajM2
        self.A = np.where(A > 0, 2, A)

        ##=========Area to observe=========
        minx = min(area[0]).astype(int)
        miny = min(area[1]).astype(int)
        maxx = np.ceil(max(area[0])).astype(int)
        maxy = np.ceil(max(area[1])).astype(int)

        coord = [(area[0][i], area[1][i]) for i in range(len(area[0]))]
        self.area = Polygon(coord)
        xr = np.arange(minx, maxx)
        yr = np.arange(miny, maxy)
        for idx, x in enumerate(xr):
            for ide, y in enumerate(yr):
                if self.area.contains(Point(x, y)):
                    self.A[y, x] = 1

        '''
        # = == == == = data for the period of tidal constituents == == == =
        self.perM2 = 12.4206  # Hour
        self.perS2 = 12  # Hour
        self.perK1 = 23.93
        self.perN2 = 12.66
        self.perO1 = 25.82
        self.perM4 = 6.2103
        self.per = np.array(
            [self.perM2, self.perS2, self.perK1, self.perN2, self.perO1, self.perM4]
        )

