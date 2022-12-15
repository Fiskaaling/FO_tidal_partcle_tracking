import pandas as pd

mode = 'cython'
print(f'Mode is on: {mode}. cython mode is fast while python mode is slower')
import time
from datetime import datetime
import numpy as np
import numpy.matlib as npm

import matplotlib.pyplot as plt


from particle_tracking_engine.particledata2 import particle_data

if mode == 'cython':
    from particle_tracking_engine.particle_tracking_cython import agent_simulation
    from particle_tracking_engine.particle_tracking_cython import A_landi
else:
    from particle_tracking_engine.particle_tracking import agent_simulation
    from particle_tracking_engine.particle_tracking import A_landi

from particle_tracking_engine.plot_particle_FO import plotting_particles
from multiprocessing import Pool
from particle_tracking_engine.Tidal_data import tidal_data

numpont =200
daysdelay = 3
data = particle_data(numpont=numpont)
DATA = tidal_data()
class Sim_run:
    def __init__(self):
        t = 24 * daysdelay  # Simulation time(hours)
        dt = 0.005  # Timestep(hours)
        # ======== pre define position and age of each partile beforehand =====
        #numpont = 100
        self.data = particle_data(numpont=2)

        self.area = [self.data.IanSgrid]

        # = == == == == == Particle Tracking simutaion == == == == == == == == == == == == == == == ==
        print(f'dt: {dt}')
        self.runsim = agent_simulation(
            areas=self.area,
            run_time=t,
            dt=dt,
            diff=True,
            open_box = 24*(daysdelay-0.5),
            close_box = 24*(daysdelay)
        )



def init_pool():
    global sim_run
    sim_run = Sim_run()



def job(args):
    #output = self.runsim.run_particle(x, y, a, start_date)

    a = args[2]
    sim_run.runsim.set_sim_period(args[-1])

    b_count =[]
    for x, y in zip(args[0], args[1]):
        try:
            output = sim_run.runsim._run_particle(x,y,a)
        except A_landi:
            output = None
        b_count.append(output)
    return b_count


##======== Run import data ==========================================
init_pool()
if __name__ == '__main__':
    #init_pool()
    Ian_sample_dates = pd.read_csv('sample_dates_Ian.csv')
    Ian_sample_dates.Dates = pd.to_datetime(Ian_sample_dates.Dates)

    start_dates = Ian_sample_dates.Dates.iloc[:] - pd.DateOffset(days=daysdelay)
    rh = 1
    posx = npm.repmat(data.Aall_posx, 1, rh).flatten('F')  # Position of Particles in X or East direction
    posy = npm.repmat(data.Aall_posy, 1, rh).flatten('F')  # Position of Particles in Y or North direction

    # ======== remove all land positions =================
    idx_2_remove = []
    for idx, (yi, xi) in enumerate(zip(posy, posx)):
        if DATA.MajM2[int(round(yi)), int(round(xi))] == 0:
            idx_2_remove.append(idx)
    posx = np.delete(posx, idx_2_remove)  # Position of Particles in X or East direction
    posy = np.delete(posy, idx_2_remove)

    for start_date in start_dates[0:1]:
        age = np.zeros((len(posx)))
        x_track = [[] for _ in posx]
        y_track = [[] for _ in posy]

        a_count = []
        start2 = time.time()
        # ========== Run all particles ===============
        runs = []
        a =0
        num_processes = 7
        split_particles = np.linspace(0,len(posx)-1,num_processes+1,dtype = int,endpoint=True)
        for idx,i in enumerate(split_particles):
            if idx<=num_processes-2:
                #print(idx)
                runs.append((posx[split_particles[idx]:split_particles[idx+1]],posy[split_particles[idx]:split_particles[idx+1]], a, start_date))

        with Pool(num_processes, init_pool) as pool:
            combined_sim = pool.map(job, runs)

        # print(combined_sim,"einki goymt her??")
        #print(combined_sim)
        #for a_counts in combined_sim:
        #    a_count.append(a_counts[0])
        for list in combined_sim:
            a_count.extend(list)
        #for x, y, a, x_t, y_t in zip(posx, posy, age, x_track, y_track):
        #    try:
        #        output = runsim.run_particle(x, y, a,start_date)
        #        #x_t.append(output[1])
        #        #y_t.append(output[2])
        #        a_count.append(output[0])
        #    except A_landi:
        #        #x_t.append(np.array([x]))
        #        #y_t.append(np.array([y]))
        #        a_count.append(0)
        #        print('vit eru á landi')

        end2 = time.time()
        print(f'time taken all particles: {end2 - start2}')
        print(np.size(np.nonzero(a_count)))
        x_pos_origin = posx[np.nonzero(a_count)]
        y_pos_origin = posy[np.nonzero(a_count)]
        print(np.shape(a_count))
        #print(a_count)

        Plotting_particles = plotting_particles(sim_run.runsim.A,sim_run.area)
        #Plotting_particles.plot_particle(x_track,y_track)

        data = {'x': x_pos_origin,
                'y': y_pos_origin}
        data = pd.DataFrame(data)
        date_input = start_date.strftime('%Y%m%d')
        data.to_csv( f'Data_Ian_project/Ian_sampledate_{date_input}_particle_age{daysdelay}_Nparticles_{numpont**2}.csv')
        Plotting_particles.plot_sea_born_map(data=data)

plt.show()
