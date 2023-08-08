import numpy as np
import pandas as pd
from particle_tracking_engine.georak import geo2grid


class particle_data:

    def __init__(self,numpont=10):
        '''
        Generates areas and
        creates agents for locations
        params:
        numpont:  number of agents in each area to the power of 2
        '''
    #= == == == == == == = Aliøkir Føroyar == == == == == ==
    #= == == == == == == == == == == == == == == == == == == == == == == ==
        self.numpont = numpont
        print(f'Number of particles released per wave: {numpont**2}')
    #= == == == == == == == == == == == == == == == == == == == == == == ==
    #= == == == == == == == Sundalagi == == == == == == == == == == =


    #= == == == == == == = Sundalagi sudur == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A81.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A81c = grid

        A81x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A81y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A81x1 = np.zeros((numpont, numpont))
        A81y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A81x1[yy, :] = np.array(np.linspace(A81x[0, yy], A81x[1, yy], numpont))
            A81y1[yy, :] = np.array(np.linspace(A81y[0, yy], A81y[1, yy], numpont))

        self.A81x = A81x1
        self.A81y = A81y1


    #= == == == == == == = Sundalagi norður == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A87.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A87c = grid

        A87x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A87y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A87x1 = np.zeros((numpont, numpont))
        A87y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A87x1[yy, :] = np.array(np.linspace(A87x[0, yy], A87x[1, yy], numpont))
            A87y1[yy, :] = np.array(np.linspace(A87y[0, yy], A87y[1, yy], numpont))

        self.A87x = A87x1
        self.A87y = A87y1


    # = == == == == == == == = Skalafjørðurin == == == == == == == == == ==
        A34x = np.array([np.linspace(670, 670, numpont), np.linspace(675, 675, numpont)])
        A34y = np.array([np.linspace(1005, 1015, numpont), np.linspace(1005, 1015, numpont)])
        A34x1 = np.zeros((numpont, numpont))
        A34y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A34x1[yy, :] = np.array(np.linspace(A34x[0, yy], A34x[1, yy], numpont))
            A34y1[yy, :] = np.array(np.linspace(A34y[0, yy], A34y[1, yy], numpont))

        self.A34x = A34x1
        self.A34y = A34y1


    #= == == == == == == == = Lamba == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A04.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A04c = grid

        A04x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A04y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A04x1 = np.zeros((numpont, numpont))
        A04y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A04x1[yy, :] = np.array(np.linspace(A04x[0, yy], A04x[1, yy], numpont))
            A04y1[yy, :] = np.array(np.linspace(A04y[0, yy], A04y[1, yy], numpont))

        self.A04x = A04x1
        self.A04y = A04y1


    #= == == == == == == == = Gøta == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A25.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A25c = grid

        A25x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A25y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A25x1 = np.zeros((numpont, numpont))
        A25y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A25x1[yy, :] = np.array(np.linspace(A25x[0, yy], A25x[1, yy], numpont))
            A25y1[yy, :] = np.array(np.linspace(A25y[0, yy], A25y[1, yy], numpont))

        self.A25x = A25x1
        self.A25y = A25y1


    #= == == == == == Árnafjørður == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A52.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A52c = grid

        A52x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A52y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A52x1 = np.zeros((numpont, numpont))
        A52y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A52x1[yy, :] = np.array(np.linspace(A52x[0, yy], A52x[1, yy], numpont))
            A52y1[yy, :] = np.array(np.linspace(A52y[0, yy], A52y[1, yy], numpont))

        self.A52x = A52x1
        self.A52y = A52y1


        #= == == == == == Funningsfjørður == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A71.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A71c = grid

        A71x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A71y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A71x1 = np.zeros((numpont, numpont))
        A71y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A71x1[yy, :] = np.array(np.linspace(A71x[0, yy], A71x[1, yy], numpont))
            A71y1[yy, :] = np.array(np.linspace(A71y[0, yy], A71y[1, yy], numpont))

        self.A71x = A71x1
        self.A71y = A71y1


        #= == == == == == Norðoyri == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A13.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A13c = grid

        A13x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A13y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A13x1 = np.zeros((numpont, numpont))
        A13y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A13x1[yy, :] = np.array(np.linspace(A13x[0, yy], A13x[1, yy], numpont))
            A13y1[yy, :] = np.array(np.linspace(A13y[0, yy], A13y[1, yy], numpont))

        self.A13x = A13x1
        self.A13y = A13y1


        #= == == == == == Ánirnar == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A12.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A12c = grid

        A12x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A12y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A12x1 = np.zeros((numpont, numpont))
        A12y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A12x1[yy, :] = np.array(np.linspace(A12x[0, yy], A12x[1, yy], numpont))
            A12y1[yy, :] = np.array(np.linspace(A12y[0, yy], A12y[1, yy], numpont))

        self.A12x = A12x1
        self.A12y = A12y1


        #= == == == == == Haraldsund == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A72.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A72c = grid

        A72x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A72y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A72x1 = np.zeros((numpont, numpont))
        A72y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A72x1[yy, :] = np.array(np.linspace(A72x[0, yy], A72x[1, yy], numpont))
            A72y1[yy, :] = np.array(np.linspace(A72y[0, yy], A72y[1, yy], numpont))

        self.A72x = A72x1
        self.A72y = A72y1


        #= == == == == == Viðareiði == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A73.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A73c = grid

        A73x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A73y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A73x1 = np.zeros((numpont,numpont))
        A73y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A73x1[yy,:]= np.array(np.linspace(A73x[0,yy], A73x[1,yy], numpont))
            A73y1[yy,:]= np.array(np.linspace(A73y[0,yy], A73y[1,yy], numpont))

        self.A73x = A73x1
        self.A73y = A73y1


    #= == == == == == norðdepil == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A11.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A11c = grid

        A11x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A11y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A11x1 = np.zeros((numpont,numpont))
        A11y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A11x1[yy,:]= np.array(np.linspace(A11x[0,yy], A11x[1,yy], numpont))
            A11y1[yy,:]= np.array(np.linspace(A11y[0,yy], A11y[1,yy], numpont))

        self.A11x = A11x1
        self.A11y = A11y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A05.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A05c = grid

        A05x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A05y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A05x1 = np.zeros((numpont, numpont))
        A05y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A05x1[yy, :] = np.array(np.linspace(A05x[0, yy], A05x[1, yy], numpont))
            A05y1[yy, :] = np.array(np.linspace(A05y[0, yy], A05y[1, yy], numpont))

        self.A05x = A05x1
        self.A05y = A05y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == ==
    #= == == == == == == == Kaldbaksfjørður == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A10.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A10c = grid

        A10x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A10y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A10x1 = np.zeros((numpont,numpont))
        A10y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A10x1[yy,:]= np.array(np.linspace(A10x[0,yy], A10x[1,yy], numpont))
            A10y1[yy,:]= np.array(np.linspace(A10y[0,yy], A10y[1,yy], numpont))

        self.A10x = A10x1
        self.A10y = A10y1


        lonlat = np.genfromtxt('Aliøkir/A82.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A82c = grid

        A82x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A82y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A82x1 = np.zeros((numpont,numpont))
        A82y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A82x1[yy,:]= np.array(np.linspace(A82x[0,yy], A82x[1,yy], numpont))
            A82y1[yy,:]= np.array(np.linspace(A82y[0,yy], A82y[1,yy], numpont))

        self.A82x = A82x1
        self.A82y = A82y1


    #= == == = uttanfyri skálafjørð
        lonlat = np.genfromtxt('Aliøkir/A85.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A85c = grid

        A85x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A85y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A85x1 = np.zeros((numpont,numpont))
        A85y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A85x1[yy,:]= np.array(np.linspace(A85x[0,yy], A85x[1,yy], numpont))
            A85y1[yy,:]= np.array(np.linspace(A85y[0,yy], A85y[1,yy], numpont))

        self.A85x = A85x1
        self.A85y = A85y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == ==
    #= == == == == == == == Argir == == == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A06.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A06c = grid

        A06x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A06y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A06x1 = np.zeros((numpont,numpont))
        A06y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A06x1[yy,:]= np.array(np.linspace(A06x[0,yy], A06x[1,yy], numpont))
            A06y1[yy,:]= np.array(np.linspace(A06y[0,yy], A06y[1,yy], numpont))

        self.A06x = A06x1
        self.A06y = A06y1


    #= == == == == == == == Velbastað == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A89.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A89c = grid

        A89x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A89y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A89x1 = np.zeros((numpont,numpont))
        A89y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A89x1[yy,:]= np.array(np.linspace(A89x[0,yy], A89x[1,yy], numpont))
            A89y1[yy,:]= np.array(np.linspace(A89y[0,yy], A89y[1,yy], numpont))

        self.A89x = A89x1
        self.A89y = A89y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == ==
    #= == == == == == == == Vágar == == == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A83.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A83c = grid

        A83x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A83y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A83x1 = np.zeros((numpont, numpont))
        A83y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A83x1[yy, :] = np.array(np.linspace(A83x[0, yy], A83x[1, yy], numpont))
            A83y1[yy, :] = np.array(np.linspace(A83y[0, yy], A83y[1, yy], numpont))

        self.A83x = A83x1
        self.A83y = A83y1


        lonlat = np.genfromtxt('Aliøkir/A27.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A27c = grid

        A27x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A27y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A27x1 = np.zeros((numpont, numpont))
        A27y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A27x1[yy, :] = np.array(np.linspace(A27x[0, yy], A27x[1, yy], numpont))
            A27y1[yy, :] = np.array(np.linspace(A27y[0, yy], A27y[1, yy], numpont))

        self.A27x = A27x1
        self.A27y = A27y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == ==
    #= == == == == == == == Vestmanna == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A88.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A88c = grid

        A88x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A88y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A88x1 = np.zeros((numpont,numpont))
        A88y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A88x1[yy,:]= np.array(np.linspace(A88x[0,yy], A88x[1,yy], numpont))
            A88y1[yy,:]= np.array(np.linspace(A88y[0,yy], A88y[1,yy], numpont))

        self.A88x = A88x1
        self.A88y = A88y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == ==
    #= == == == == == == == Árnafjørður == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A63.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A63c = grid

        A63x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A63y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A63x1 = np.zeros((numpont,numpont))
        A63y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A63x1[yy,:]= np.array(np.linspace(A63x[0,yy], A63x[1,yy], numpont))
            A63y1[yy,:]= np.array(np.linspace(A63y[0,yy], A63y[1,yy], numpont))

        self.A63x = A63x1
        self.A63y = A63y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == =
    #= == == == == == == == Fuglafjørður == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A57.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A57c = grid

        A57x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A57y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A57x1 = np.zeros((numpont, numpont))
        A57y1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            A57x1[yy, :] = np.array(np.linspace(A57x[0, yy], A57x[1, yy], numpont))
            A57y1[yy, :] = np.array(np.linspace(A57y[0, yy], A57y[1, yy], numpont))

        self.A57x = A57x1
        self.A57y = A57y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == =
    #= == == == == == == == Suðuroy == == == == == == == == == == =

    #= == == == == == == == == hov == == == == =
        lonlat = np.genfromtxt('Aliøkir/A18.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A18c = grid

        A18x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A18y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A18x1 = np.zeros((numpont,numpont))
        A18y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A18x1[yy,:]= np.array(np.linspace(A18x[0,yy], A18x[1,yy], numpont))
            A18y1[yy,:]= np.array(np.linspace(A18y[0,yy], A18y[1,yy], numpont))

        self.A18x = A18x1
        self.A18y = A18y1


    #= == == == == == == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A17.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A17c = grid

        A17x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A17y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A17x1 = np.zeros((numpont,numpont))
        A17y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A17x1[yy,:]= np.array(np.linspace(A17x[0,yy], A17x[1,yy], numpont))
            A17y1[yy,:]= np.array(np.linspace(A17y[0,yy], A17y[1,yy], numpont))

        self.A17x = A17x1
        self.A17y = A17y1


    #= == == == == == == == == == Vágur == == == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A92.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A92c = grid

        A92x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A92y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A92x1 = np.zeros((numpont,numpont))
        A92y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A92x1[yy,:]= np.array(np.linspace(A92x[0,yy], A92x[1,yy], numpont))
            A92y1[yy,:]= np.array(np.linspace(A92y[0,yy], A92y[1,yy], numpont))

        self.A92x = A92x1
        self.A92y = A92y1


    #= == == == == == == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A19.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A19c = grid

        A19x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A19y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A19x1 = np.zeros((numpont,numpont))
        A19y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A19x1[yy,:]= np.array(np.linspace(A19x[0,yy], A19x[1,yy], numpont))
            A19y1[yy,:]= np.array(np.linspace(A19y[0,yy], A19y[1,yy], numpont))

        self.A19x = A19x1
        self.A19y = A19y1


    #= == == == == == == == == == Tvøroyri == == == == == == == == == == == == == == == == == ==
        lonlat = np.genfromtxt('Aliøkir/A16.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A16c = grid

        A16x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A16y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A16x1 = np.zeros((numpont,numpont))
        A16y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A16x1[yy,:]= np.array(np.linspace(A16x[0,yy], A16x[1,yy], numpont))
            A16y1[yy,:]= np.array(np.linspace(A16y[0,yy], A16y[1,yy], numpont))

        self.A16x = A16x1
        self.A16y = A16y1


    #= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A15.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A15c = grid

        A15x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A15y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A15x1 = np.zeros((numpont,numpont))
        A15y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A15x1[yy,:]= np.array(np.linspace(A15x[0,yy], A15x[1,yy], numpont))
            A15y1[yy,:]= np.array(np.linspace(A15y[0,yy], A15y[1,yy], numpont))

        self.A15x = A15x1
        self.A15y = A15y1


    #= == == == == == == == == == == == = Sandoy == == == == == == == == == == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A90.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A90c = grid

        A90x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A90y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A90x1 = np.zeros((numpont,numpont))
        A90y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A90x1[yy,:]= np.array(np.linspace(A90x[0,yy], A90x[1,yy], numpont))
            A90y1[yy,:]= np.array(np.linspace(A90y[0,yy], A90y[1,yy], numpont))

        self.A90x = A90x1
        self.A90y = A90y1


    #= == == == == == == = Víkar A14 == == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/A14.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0], lonlat[1])
        self.A14c = grid

        A14x = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        A14y = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        A14x1 = np.zeros((numpont,numpont))
        A14y1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            A14x1[yy,:]= np.array(np.linspace(A14x[0,yy], A14x[1,yy], numpont))
            A14y1[yy,:]= np.array(np.linspace(A14y[0,yy], A14y[1,yy], numpont))

        self.A14x = A14x1
        self.A14y = A14y1


    #= == == == == == == == == == == == == royndarøkið at sleppa partiklum == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/data-2021-12-20.csv', skip_header=1, delimiter=',').T
        grid = geo2grid(lonlat[0],lonlat[1])
        self.Aexc = grid

        Aex = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        Aey = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        Aex1 = np.zeros((numpont,numpont))
        Aey1 = np.zeros((numpont,numpont))

        for yy in range(numpont):
            Aex1[yy,:]= np.array(np.linspace(Aex[0,yy], Aex[1,yy], numpont))
            Aey1[yy,:]= np.array(np.linspace(Aey[0,yy], Aey[1,yy], numpont))

        self.Aex = Aex1
        self.Aey = Aey1


        # = == == == == == == = All not land particles == == == == == == == == == =

        grid = [[20,1086,20,1086],[20,20,1486,1486]]
        self.All_pos_c = grid

        Aall_posx = np.array([np.linspace(grid[0][0], grid[0][1], numpont), np.linspace(grid[0][2], grid[0][3], numpont)])
        Aall_posy = np.array([np.linspace(grid[1][0], grid[1][1], numpont), np.linspace(grid[1][2], grid[1][3], numpont)])
        Aall_posx1 = np.zeros((numpont, numpont))
        Aall_posy1 = np.zeros((numpont, numpont))

        for yy in range(numpont):
            Aall_posx1[yy, :] = np.array(np.linspace(Aall_posx[0, yy], Aall_posx[1, yy], numpont))
            Aall_posy1[yy, :] = np.array(np.linspace(Aall_posy[0, yy], Aall_posy[1, yy], numpont))



        self.Aall_posx = Aall_posx1
        self.Aall_posy = Aall_posy1


        # = == == == == == == == == == == == == Sørvágsfjørður == == == == == == == == =
        lonlat = np.genfromtxt('Aliøkir/sv2.csv', skip_header=1, delimiter=',').T

        self.SVgrid = geo2grid(lonlat[0], lonlat[1])
        self.Svcoord = [(self.SVgrid[0][i],self.SVgrid[1][i]) for i in range(len(self.SVgrid[0]))]


        lonlat = np.genfromtxt('Aliøkir/sv_1.csv', skip_header=1, delimiter=',').T

        self.SV1grid = geo2grid(lonlat[0], lonlat[1])
        self.Sv1coord = [(self.SV1grid[0][i], self.SV1grid[1][i]) for i in range(len(self.SV1grid[0]))]


        lonlat = np.genfromtxt('Aliøkir/sv_2.csv', skip_header=1, delimiter=',').T

        self.SV2grid = geo2grid(lonlat[0], lonlat[1])
        self.Sv2coord = [(self.SV2grid[0][i], self.SV2grid[1][i]) for i in range(len(self.SV2grid[0]))]

        lonlat = np.genfromtxt('Aliøkir/sv_s.csv', skip_header=1, delimiter=',').T

        self.SVsgrid = geo2grid(lonlat[0], lonlat[1])
        self.Svscoord = [(self.SVsgrid[0][i], self.SVsgrid[1][i]) for i in range(len(self.SVsgrid[0]))]


        lonlat = np.genfromtxt('Aliøkir/sv_v.csv', skip_header=1, delimiter=',').T

        self.SVvgrid = geo2grid(lonlat[0], lonlat[1])
        self.Svvcoord = [(self.SVvgrid[0][i], self.SVvgrid[1][i]) for i in range(len(self.SVvgrid[0]))]


        lonlat = np.genfromtxt('Aliøkir/vestmannafjørður.csv', skip_header=1, delimiter=',').T

        self.Vestgrid = geo2grid(lonlat[0], lonlat[1])
        self.vestcoord = [(self.Vestgrid[0][i], self.Vestgrid[1][i]) for i in range(len(self.Vestgrid[0]))]


        lonlat = np.genfromtxt('Aliøkir/uttanfyri_vestmanna.csv', skip_header=1, delimiter=',').T

        self.u_Vestgrid = geo2grid(lonlat[0], lonlat[1])
        self.u_Vestcoord = [(self.u_Vestgrid[0][i], self.u_Vestgrid[1][i]) for i in range(len(self.u_Vestgrid[0]))]


        # = == == == == == == == == == == == == Sørvágsfjørður == == == == == == == == =
        lonlat = pd.read_csv('Aliøkir/Ian_sampling_onepoint.csv') #Ian_sampling_position_til_birgittu_app_area_300m.csv')
        self.IanSgrid = geo2grid(lonlat['lng'].values, lonlat['lat'].values)
        #self.IanScoord = [(self.IanSgrid[0][i],self.IanSgrid[1][i]) for i in range(len(self.IanSgrid[0]))]



    # #= == == == == == == = Hvalba A100 == == == == == == == == == =
    #     A100x = np.array([np.linspace(594, 592, numpont), np.linspace(599, 597, numpont)])
    #     A100y = np.array([np.linspace(442, 447, numpont), np.linspace(444, 449, numpont)])
    #     A100x1 = np.zeros((numpont,numpont))
    #     A100y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         A100x1[yy,:]= np.array(np.linspace(A100x[0,yy], A100x[1,yy], numpont))
    #         A100y1[yy,:]= np.array(np.linspace(A100y[0,yy], A100y[1,yy], numpont))
    #
    #     self.A100x = A100x1
    #     self.A100y = A100y1
    # #= == == == == == == = Norðkalsoy A101 == == == == == == == == == =
    #     A101x = np.array([np.linspace(680, 676, numpont), np.linspace(682, 678, numpont)])
    #     A101y = np.array([np.linspace(1168, 1180, numpont), np.linspace(1168, 1180, numpont)])
    #     A101x1 = np.zeros((numpont,numpont))
    #     A101y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         A101x1[yy,:]= np.array(np.linspace(A101x[0,yy], A101x[1,yy], numpont))
    #         A101y1[yy,:]= np.array(np.linspace(A101y[0,yy], A101y[1,yy], numpont))
    #
    #     self.A101x = A101x1
    #     self.A101y = A101y1
    # #= == == == == == == = Eystan nólsoy A102 == == == == == == == == == =
    #     A102x = np.array([np.linspace(717, 717, numpont), np.linspace(722, 722, numpont)])
    #     A102y = np.array([np.linspace(882, 887, numpont), np.linspace(882, 887, numpont)])
    #     A102x1 = np.zeros((numpont,numpont))
    #     A102y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         A102x1[yy,:]= np.array(np.linspace(A102x[0,yy], A102x[1,yy], numpont))
    #         A102y1[yy,:]= np.array(np.linspace(A102y[0,yy], A102y[1,yy], numpont))
    #
    #     self.A102x = A102x1
    #     self.A102y = A102y1
    # #= == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    # # = == == == == == == == == == == = Fyri delta time test == == == == == == == == == == ==
    #     A00x = np.array([np.linspace(280, 280, numpont), np.linspace(300, 300, numpont)])
    #     A00y = np.array([np.linspace(430, 450, numpont), np.linspace(430, 450, numpont)])
    #     A00x1 = np.zeros((numpont,numpont))
    #     A00y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         A00x1[yy,:]= np.array(np.linspace(A00x[0,yy], A00x[1,yy], numpont))
    #         A00y1[yy,:]= np.array(np.linspace(A00y[0,yy], A00y[1,yy], numpont))
    #
    #     self.A00x = A00x1
    #     self.A00y = A00y1
    #
    #     A01x = np.array([np.linspace(280, 280, numpont), np.linspace(300, 300, numpont)])
    #     A01y = np.array([np.linspace(1280, 1300, numpont), np.linspace(1280, 1300, numpont)])
    #     A01x1 = np.zeros((numpont,numpont))
    #     A01y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         A01x1[yy,:]= np.array(np.linspace(A01x[0,yy], A01x[1,yy], numpont))
    #         A01y1[yy,:]= np.array(np.linspace(A01y[0,yy], A19y[1,yy], numpont))
    #
    #     self.A01x = A01x1
    #     self.A01y = A01y1
    #
    #     A02x = np.array([np.linspace(400, 400, numpont), np.linspace(420, 420, numpont)])
    #     A02y = np.array([np.linspace(630, 650, numpont), np.linspace(630, 650, numpont)])
    #     A02x1 = np.zeros((numpont,numpont))
    #     A02y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         A02x1[yy,:]= np.array(np.linspace(A02x[0,yy], A02x[1,yy], numpont))
    #         A02y1[yy,:]= np.array(np.linspace(A02y[0,yy], A02y[1,yy], numpont))
    #
    #     self.A02x = A02x1
    #     self.A02y = A02y1
    # #= == == == == == == == == == == == == fyri at síggja ferd vectorin == == == == == ==
    #     Avecx = np.array([np.linspace(700, 700, numpont), np.linspace(720, 720, numpont)])
    #     Avecy = np.array([np.linspace(520, 540, numpont), np.linspace(520, 540, numpont)])
    #
    #     Avecx1 = np.zeros((numpont, numpont))
    #     Avecy1 = np.zeros((numpont, numpont))
    #
    #     for yy in range(numpont):
    #         Avecx1[yy, :] = np.array(np.linspace(Avecx[0, yy], Avecx[1, yy], numpont))
    #         Avecy1[yy, :] = np.array(np.linspace(Avecy[0, yy], Avecy[1, yy], numpont))
    #
    #     self.Avecx = Avecx1
    #     self.Avecy = Avecy1
    # #= == == == == == == == == == == == == fyri at síggja constituens == == == == == ==
    #
    #     Aconx = np.array([np.linspace(650, 650, numpont), np.linspace(750, 750, numpont)])
    #     Acony = np.array([np.linspace(450, 650, numpont), np.linspace(450, 650, numpont)])
    #     Aconx1 = np.zeros((numpont,numpont))
    #     Acony1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         Aconx1[yy,:]= np.array(np.linspace(Aconx[0,yy], Aconx[1,yy], numpont))
    #         Acony1[yy,:]= np.array(np.linspace(Acony[0,yy], Acony[1,yy], numpont))
    #
    #     self.Aconx = Aconx1
    #     self.Acony = Acony1
    # #= == == == == == == == == == == == == fyri at síggja particle dispersion == == == == == ==
    #     Aparx = np.array([np.linspace(719.975, 719.975, numpont), np.linspace(720.025, 720.025, numpont)])
    #     Apary = np.array([np.linspace(549.975, 550.025, numpont), np.linspace(549.975, 550.025, numpont)])
    #     Aparx1 = np.zeros((numpont,numpont))
    #     Apary1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         Aparx1[yy,:]= np.array(np.linspace(Aparx[0,yy], Aparx[1,yy], numpont))
    #         Apary1[yy,:]= np.array(np.linspace(Apary[0,yy], Apary[1,yy], numpont))
    #
    #     self.Aparx = Aparx1
    #     self.Apary = Apary1
    #
    #     Apar1x = np.array([np.linspace(644.975, 644.975, numpont), np.linspace(645.025, 645.025, numpont)])
    #     Apar1y = np.array([np.linspace(1129.975, 1130.025, numpont), np.linspace(1129.975, 1130.025, numpont)])
    #     Apar1x1 = np.zeros((numpont,numpont))
    #     Apar1y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         Apar1x1[yy,:]= np.array(np.linspace(Apar1x[0,yy], Apar1x[1,yy], numpont))
    #         Apar1y1[yy,:]= np.array(np.linspace(Apar1y[0,yy], Apar1y[1,yy], numpont))
    #
    #     self.Apar1x = Apar1x1
    #     self.Apar1y = Apar1y1
    #
    #     Apar2x = np.array([np.linspace(629.975, 629.975, numpont), np.linspace(630.025, 630.025, numpont)])
    #     Apar2y = np.array([np.linspace(939.975, 940.025, numpont), np.linspace(939.975, 940.025, numpont)])
    #     Apar2x1 = np.zeros((numpont,numpont))
    #     Apar2y1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         Apar2x1[yy,:]= np.array(np.linspace(Apar2x[0,yy], Apar2x[1,yy], numpont))
    #         Apar2y1[yy,:]= np.array(np.linspace(Apar2y[0,yy], Apar2y[1,yy], numpont))
    #
    #     self.Apar2x = Apar2x1
    #     self.Apar2y = Apar2y1
    # #= == == == == == == == == == == == == fyri at síggja tidal ellipse yvir alt FO == == == == == ==
    #     Afox = np.array([np.linspace(10, 10, numpont), np.linspace(1080, 1080, numpont)])
    #     Afoy = np.array([np.linspace(10, 1480, numpont), np.linspace(10, 1480, numpont)])
    #     Afox1 = np.zeros((numpont,numpont))
    #     Afoy1 = np.zeros((numpont,numpont))
    #
    #     for yy in range(numpont):
    #         Afox1[yy,:]= np.array(np.linspace(Afox[0,yy], Afox[1,yy], numpont))
    #         Afoy1[yy,:]= np.array(np.linspace(Afoy[0,yy], Afoy[1,yy], numpont))
    #
    #     self.Afox = Afox1
    #     self.Afoy = Afoy1



