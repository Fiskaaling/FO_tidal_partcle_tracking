import numpy as np
from particle_tracking_engine.Tidal_data import tidal_data
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

import time as time0
from datetime import datetime

class A_landi(Exception):
    pass

class agent_simulation:
    '''Defines agent for particle tracking'''

    def __init__(self,
                 areas,
                 run_time=1000,
                 dt=0.05,
                 diff=False,
                 start=datetime(2000, 1, 1),
                 open_box = 0,
                 close_box = 0):

        '''params:
        posx: Array with positions of particles in X or east direction
        posy: Array with positions of particles in Y or south direction
        area: list of X and Y coordinate tuples for defined area to observe
        time: time to run  simulation in hours
        dt: timestep in hours
        diff: inclusion of diffusion in simulation, True or False
        rh: number of times particles are released at start of simulation
        '''

        self.diff = diff

        #= == == == = time and grid varibles == == == == =
        start2 = time0.time() #TODO at taka hesar tíðinar skal út aftur einaferð, minst til at start skal ikki vera tað sama sum í sim_period
        DATA = tidal_data()
        end2 = time0.time()
        print(f'time taken to load data: {end2 - start2}')

        self.run_time = run_time
        self.dt = dt
        self.dtsek = self.dt*3600
        self.dz = DATA.dz
        self.time_dt = int(self.run_time / dt)
        #self.set_sim_period(start) # TODO Bogi sigur at start punkti í simulering er 1 jan 1975
                                   # TODO Bárur N. sigur at start punkti í simulering er 1 jan 2000
        #self.run_time = self.dt_time
        #= == == == == Diffusion == == == == == == == == == == =
        self.Dh = 0.1 # m ^ 2 / s;

        #= == == == = land or not land matrix == == == ==
        A = DATA.MajM2
        # ind = np.array([np.where(A==0)])
        self.A = np.where(DATA.MajM2 > 0, 1, 0)
        #self.A = np.where(A>0,2,A)
        # = == == == == m2 == == == == == == == == ==
        self.M_u1 = DATA.M_u1
        self.M_u2 = DATA.M_u2
        self.M_v1 = DATA.M_v1
        self.M_v2 = DATA.M_v2
        self.Pha_all = DATA.Pha_all

        #= == == == == Res == == == == == == ==
        self.ResU = DATA.ResU
        self.ResV = DATA.ResV
        #= == == == == == == == == == == == == == == == == ==

        #self.mark_A(areas)

        self.per = np.array(DATA.per)
        self.per_constant = np.dot((2 * np.pi), 1/self.per) * self.dt
        ##========= Hvussu leingi skal boxin vera opin og nær=========
        self.open_box = open_box
        self.close_box = close_box

    def run_particle(self, posxi, posyi, age,startdate=0):
        #======= Time initialization ======
        start = int( (startdate - datetime(2000, 1, 1,0,0)).total_seconds()/(60*60)/self.dt )

        end = start + int(self.run_time/self.dt)
        len_sim = len(range(start, end)) #self.len_sim
        #=================================
        xi_old, yi_old = 0, 0
        X = []
        Y = []
        AGE = []
        if self.diff:
            rand = (
                x 
                for x in 
                (2*np.random.rand(2*len_sim)-1) *\
                np.sqrt(6 * self.Dh * self.dtsek) / self.dz
            )
        else:
            rand = (
                x 
                for x in 
                (np.zeros(2*len_sim))
            )

        ferd_mod = self.dtsek / self.dz
        counter = 0



        #=== Agent position == == =

        xi, fractx = divmod(posxi, 1)
        xi = int(xi)
        yi, fracty = divmod(posyi, 1)
        yi = int(yi)

        for t in range(start,end):
            age += self.dt

            if xi != xi_old or yi != yi_old:

                xi_old, yi_old = xi, yi

                try:
                    M_u1_use = self.M_u1[:, yi:yi+2, xi:xi+2]
                    M_u2_use = self.M_u2[:, yi:yi+2, xi:xi+2]
                    M_v1_use = self.M_v1[:, yi:yi+2, xi:xi+2]
                    M_v2_use = self.M_v2[:, yi:yi+2, xi:xi+2]
                    A_use = self.A[yi:yi+2, xi:xi+2]

                    #
                    Pha = self.Pha_all[:, yi:yi+2, xi:xi+2]

                    #= == == Residual U and V == == == == == =
                    uRes = self.ResU[yi:yi+2,xi:xi+2]
                    vRes = self.ResV[yi:yi+2,xi:xi+2]
                except IndexError:
                    break

                land = (A_use == 0).sum()
            #============================
            #= == == = cos / sin M2 == == == == ==
            wt1 = self.per_constant * t

            cos_all = np.cos(wt1[:, None, None] - Pha)

            sin_all = np.sin(wt1[:, None, None] - Pha)

            # = == == == == == == == == uM2 == == == == == == == == == == == == == == ==
            u = np.multiply(M_u1_use, cos_all) -\
                    np.multiply(M_u2_use, sin_all)

            #= == == == == == == == == vM2 == == == == == == == == == == == == == == ==
            v = np.multiply(M_v1_use, cos_all) +\
                    np.multiply(M_v2_use, sin_all)

            #= == == u and v
            u_all = u.sum(axis=0)+uRes
            v_all = v.sum(axis=0)+vRes

            # = == == = defining the agent the in x - axis between 1 and 2

            vec_x = np.array([1-fractx, fractx])
            vec_y = np.array([1-fracty, fracty])

            ux = np.dot(vec_y, np.dot(vec_x, u_all))
            # = == == == == == == = y position == == == == == == == == =
            vy = np.dot(vec_y, np.dot(vec_x, v_all))

            # = == == == velosity profile == == == == == == =
            dx = ux * ferd_mod + next(rand)
            dy = vy * ferd_mod + next(rand)
            posxi += dx
            posyi += dy
            #= == Agent position == == =

            xi, fractx = divmod(posxi, 1)
            xi = int(xi)
            yi, fracty = divmod(posyi, 1)
            yi = int(yi)

            # = == == == == == == == == == == = Boundary condition - Reflection == == == == == == == =
            #= == == == == = Tjek if Particles are on land or not == == == == == == ==
            #  eru vit nær við land
            if land and A_use[int(round(fracty)), int(round(fractx))] == 0:

                #= == == == == == == == == == = X position == == == == == == == == == == == == =
                if land == 1:
                    if (fractx - 0.5) * dx > 0:
                        fractx = 1 - fractx
                        posxi = xi + fractx

                    if (fracty - 0.5) * dy > 0:
                        fracty = 1 - fracty
                        posyi = yi + fracty

                elif land == 2:
                    if A_use[int(round(fracty)), 1 - int(round(fractx))] == 0:
                        fractx = 1 - fractx
                        posxi = xi + fractx
                    elif A_use[1 - int(round(fracty)), int(round(fractx))] == 0:
                        fracty = 1 - fracty
                        posyi = yi + fracty
                    else:
                        raise Exception('hettar burda ikki hent')

                elif land == 3:
                    if A_use[int(round(fracty)), 1 - int(round(fractx))] == 0:
                        fractx = 1 - fractx
                        posxi = xi + fractx
                    if A_use[1 - int(round(fracty)), int(round(fractx))] == 0:
                        fracty = 1 - fracty
                        posyi = yi + fracty

                else:
                    raise A_landi('Tú ert á landi')
                    
            # copoint = Point(posxi, posyi)

            # check if point is inside area
            # if self.area.contains(copoint):
            if A_use[int(round(fracty)),int(round(fractx))] == 2:
                if age >=self.open_box and age <=self.close_box:
                    counter += 1
            age += self.dt

            X.append(posxi)
            Y.append(posyi)
            AGE.append(age)

        return counter,X,Y

    def set_sim_period(self, start: datetime, run_time:float=None) -> None:
        ''' set sim periode '''

        if run_time is not None:
            self.time = run_time

        self.start = (start - datetime(2000, 1, 1)).days
        self.end = self.start + int(self.run_time/self.dt)

        self.sim_period = np.arange(self.start, self.start + int(self.time/self.dt))
        if (not hasattr(self, 'len_sim')) or (self.len_sim != getattr(self, 'len_sim')):
            self.len_sim = len(self.sim_period)
            self.X = np.empty((self.len_sim,), np.double)
            self.Y = np.empty((self.len_sim,), np.double)
            self.AGE = np.empty((self.len_sim,), np.double)
#= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

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
                    if self.area.contains(Point(x,y)):
                        self.A[y,x]=i+2

    def cos(self,x):
        return (x)/np.linalg.norm(x, axis=1)
