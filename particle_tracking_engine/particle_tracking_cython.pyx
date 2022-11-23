import numpy as np
cimport numpy as np
from cpython.datetime cimport datetime
from particle_tracking_engine.Tidal_data import tidal_data
from shapely.geometry import Polygon, Point

from datetime import datetime

from libc.stdlib cimport rand, srand, RAND_MAX
from libc.math cimport cos
from libc.math cimport sin
from libc.math cimport round as round_c
cimport cython

np.import_array()

DATA = tidal_data()

class A_landi(Exception):
    pass

class agent_simulation:
    '''Defines agent for particle tracking'''

    def __init__(
        self,
        areas,
        run_time=1000,
        dt=0.05,
        diff=False,
        start=datetime(2000, 1, 1)
    ):

        '''params:
        area: list of X and Y coordinate tuples for defined area to observe
        run_time: how long is the simolation in hours
        dt: timestep in hours
        diff: inclusion of diffusion in simulation, True or False
        rh: number of times particles are released at start of simulation
        start: start time
        '''

        self.diff = diff
        self.dt = dt
        self.numa = len(areas)

        # TODO Bogi sigur at start punkti í simulering er 1 jan 1975
        # TODO Bárur N. sigur at start punkti í simulering er 1 jan 2000
        # and sets X, Y, AGE
        print(run_time)
        self.set_sim_period(start, run_time) 

        # Land og POI matrica land hevur virði 0 
        self.A = np.where(DATA.MajM2>0, 1, 0)
        self.mark_A(areas)

        ##=========Area to observe=========
        self.per_constant = (2 * np.pi * self.dt)/DATA.per

        dtsek = self.dt*3600
        if self.diff:
            self.Dh = 0.1 # m ^ 2 / s;
            self.diff_fac = np.sqrt(6 * self.Dh * dtsek) / DATA.dz
        else:
            self.diff_fac = 0.

        self.ferd_mod = dtsek / DATA.dz

        cdef int randseed = np.random.randint(0, 1000000)
        srand(randseed)

    def run_particle(
            self, 
            posxi,
            posyi,
            age,
            startdate
            ):

        self.set_sim_period(startdate)

        counter = self._run_particle(posxi, posyi, age)

        return counter, self.X.copy(), self.Y.copy(), self.AGE.copy()

    @cython.wraparound(False)  # turn off negative index wrapping for entire function
    @cython.boundscheck(False) # turn off bounds-checking for entire function
    @cython.cdivision(True)
    def _run_particle(
        self,
        double posxi,
        double posyi,
        double age
    ):

        # Hvar eru vit
        cdef int xi_old, yi_old, xi, yi, x_initial, y_initial
        cdef double fractx, fracty
        xi_old, yi_old = 0, 0

        # iter index
        cdef int t, i1, i2, i3, temp_int

        # temp til at rokna index skjótt
        cdef int temp_i1
        cdef int temp_i2
        cdef int temp_i3

        # hvussu nógvir land puntar eru nær við
        cdef int land = 0
        cdef int numa = self.numa

        # updatera stað
        cdef double dx, dy
        cdef double tempu
        cdef double tempv
        cdef double dt = self.dt
        cdef double ferd_mod = self.ferd_mod

        # tær globalu matricunar
        cdef np.ndarray[np.double_t, ndim=3] M_u1    = DATA.M_u1
        cdef np.ndarray[np.double_t, ndim=3] M_u2    = DATA.M_u2
        cdef np.ndarray[np.double_t, ndim=3] M_v1    = DATA.M_v1
        cdef np.ndarray[np.double_t, ndim=3] M_v2    = DATA.M_v2
        cdef np.ndarray[np.int_t,    ndim=2] A       = self.A
        cdef np.ndarray[np.double_t, ndim=3] Pha_all = DATA.Pha_all
        cdef np.ndarray[np.double_t, ndim=2] ResU    = DATA.ResU
        cdef np.ndarray[np.double_t, ndim=2] ResV    = DATA.ResV

        # tær localu matricunar sum c listar
        cdef double M_u1_use[24]
        cdef double M_u2_use[24]
        cdef double M_v1_use[24]
        cdef double M_v2_use[24]
        cdef double A_use[4]
        cdef double Pha[24]
        cdef double uRes[4]
        cdef double vRes[4]
        cdef double u[24]
        cdef double v[24]
        cdef double vec_x[2]
        cdef double vec_y[2]

        # konsutient ferðir
        cdef double per_constant[6]
        per_constant= self.per_constant

        # dummy variablar til at rokna konsutientar skjótt
        cdef double wt1
        cdef double arg
        cdef double cos_all
        cdef double sin_all

        # config variablar
        cdef int diff = self.diff
        cdef double diff_fac = self.diff_fac

        # hvussu lang er simoleringin
        cdef int len_sim = self.len_sim
        cdef int start = self.start
        cdef int end = self.end

        #Variablar til at fylgja við trackinum
        cdef np.ndarray[np.double_t, ndim=1] X = self.X
        cdef np.ndarray[np.double_t, ndim=1] Y = self.Y
        cdef np.ndarray[np.double_t, ndim=1] AGE = self.AGE

        cdef int X_Y_index = 0
        cdef int counter = 0

        #= == Agent position == == =
        fractx = posxi % 1
        xi = int(posxi)
        fracty = posyi % 1
        yi = int(posyi)

        # Main loop
        for t in range(start, end):

            # updatera local variablar um vit skifta kvadrat
            if xi != xi_old or yi != yi_old:
                xi_old, yi_old = xi, yi
                land = 0
                if yi<2 or xi<2 or yi>1486 or xi>1086:
                    break
                for i2 in range(2):
                    temp_i2 = 6*i2
                    for i3 in range(2):
                        temp_i3 = temp_i2 + 12*i3
                        for i1 in range(6):
                            temp_i1 = temp_i3 + i1
                            M_u1_use[temp_i1] = M_u1[i1, yi+i2, xi+i3]
                            M_u2_use[temp_i1] = M_u2[i1, yi+i2, xi+i3]
                            M_v1_use[temp_i1] = M_v1[i1, yi+i2, xi+i3]
                            M_v2_use[temp_i1] = M_v2[i1, yi+i2, xi+i3]
                            Pha[temp_i1] = Pha_all[i1, yi+i2, xi+i3]
                        temp_int = A[yi+i2, xi+i3]
                        A_use[i2+2*i3] = temp_int
                        if temp_int == 0:
                            land += 1

                        uRes[i2+2*i3] = ResU[yi+i2,xi+i3]
                        vRes[i2+2*i3] = ResV[yi+i2,xi+i3]

            # rokna summin av konstieentinum
            for i1 in range(6):
                temp_i1 = i1
                wt1 = per_constant[i1] * t
                for i2 in range(2):
                    temp_i2 = temp_i1 + 6*i2
                    for i3 in range(2):
                        temp_i3 = temp_i2 + 12*i3
                        arg = wt1 - Pha[temp_i3]

                        cos_all = cos(arg)
                        sin_all = sin(arg)
                        
                        u[temp_i3] = M_u1_use[temp_i3] * cos_all -\
                                M_u2_use[temp_i3] * sin_all
                        v[temp_i3] = M_v1_use[temp_i3] * cos_all +\
                                M_v2_use[temp_i3] * sin_all

            # rokna ferð
            vec_x = [1-fractx, fractx]
            vec_y = [1-fracty, fracty]

            dx = 0.
            dy = 0.
            for i2 in range(2):
                temp_i2 = 6*i2
                for i3 in range(2):
                    temp_i3 = temp_i2 + 12*i3
                    tempu = uRes[i2+2*i3]
                    tempv = vRes[i2+2*i3]
                    for i1 in range(6):
                        temp_i1 = temp_i3 + i1
                        tempu += u[temp_i1]
                        tempv += v[temp_i1]
                    dx += tempu * vec_x[i2] * vec_y[i3]
                    dy += tempv * vec_x[i2] * vec_y[i3]

            dx = dx * ferd_mod
            dy = dy * ferd_mod

            if diff:
                dx += diff_fac*(2*(rand()/(RAND_MAX+1.0))-1)
                dy += diff_fac*(2*(rand()/(RAND_MAX+1.0))-1)

            posxi += dx
            posyi += dy

            # Rokna index of frac fyri nýggju positión
            fractx = posxi % 1
            xi = int(posxi)
            fracty = posyi % 1
            yi = int(posyi)

            #  eru vit nær við land/ farin á land
            if land:
                if A_use[int(round_c(fracty)+2*round_c(fractx))] == 0:

                    #= == == == == == == == == == = X position == == == == == == == == == == == == =
                    if land == 1:
                        if (fractx - 0.5) * dx > 0:
                            fractx = 1 - fractx
                            posxi = xi + fractx

                        if (fracty - 0.5) * dy > 0:
                            fracty = 1 - fracty
                            posyi = yi + fracty

                    elif land == 2:
                        if A_use[int(round_c(fracty)+2*(1 - round_c(fractx)))] == 0:
                            fractx = 1 - fractx
                            posxi = xi + fractx
                        elif A_use[int(1 - round_c(fracty)+2*round_c(fractx))] == 0:
                            fracty = 1 - fracty
                            posyi = yi + fracty
                        else:
                            print('hetta burdi ikki hent')
                            #raise Exception('hettar burda ikki hent')

                    elif land == 3:
                        if A_use[int(round_c(fracty)+2*(1 - round_c(fractx)))] == 0:
                            fractx = 1 - fractx
                            posxi = xi + fractx
                        if A_use[int(1 - round_c(fracty)+2*round_c(fractx))] == 0:
                            fracty = 1 - fracty
                            posyi = yi + fracty

                    else:
                        raise A_landi('Tú ert á landi')

            if A_use[int(round_c(fracty)+2*round_c(fractx))] == 2:
                if 24*5.5 <= age <= 24*6:
                    counter += 1
            age += dt

            X[X_Y_index] = posxi
            Y[X_Y_index] = posyi
            AGE[X_Y_index] = age
            X_Y_index += 1
        X[X_Y_index:] = 0
        Y[X_Y_index:] = 0
        AGE[X_Y_index:] = 0

        return counter

    def set_sim_period(self, start: datetime, run_time:float=None) -> None:
        ''' set sim periode '''

        if run_time is not None:
            self.time = run_time

        self.start = (start - datetime(2000, 1, 1)).days
        self.end = self.start + int(self.time/self.dt)

        self.sim_period = np.arange(self.start, self.start + int(self.time/self.dt))
        if (not hasattr(self, 'len_sim')) or (self.len_sim != getattr(self, 'len_sim')):
            self.len_sim = len(self.sim_period)
            self.X = np.empty((self.len_sim,), np.double)
            self.Y = np.empty((self.len_sim,), np.double)
            self.AGE = np.empty((self.len_sim,), np.double)

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
