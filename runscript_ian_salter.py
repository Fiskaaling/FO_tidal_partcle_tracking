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

##======== Run import data ==========================================

if __name__ == '__main__':

    t = 24*6  # Simulation time(hours)
    dt = 0.005  # Timestep(hours)
    rh = 1  # how many times you want to realese agents - every hour

    # ======== pre define position and age of each partile beforehand =====
    numpont = 50
    data = particle_data(numpont=numpont)

    area = [data.IanSgrid]

    # = == == == == == Particle Tracking simutaion == == == == == == == == == == == == == == == ==
    print(f'dt: {dt}')
    runsim = agent_simulation(
        areas=area,
        run_time=t,
        dt=dt,
        diff=False,
    )
    Ian_sample_dates = pd.read_csv('sample_dates_Ian.csv')
    Ian_sample_dates.Dates = pd.to_datetime(Ian_sample_dates.Dates)
    daysdelay = 6
    start_dates = Ian_sample_dates.Dates.iloc[10:]-pd.DateOffset(days=daysdelay)

    posx = npm.repmat(data.Aall_posx, 1, rh).flatten('F')  # Position of Particles in X or East direction
    posy = npm.repmat(data.Aall_posy, 1, rh).flatten('F')  # Position of Particles in Y or North direction

    for start_date in start_dates:
        #======== remove all land positions =================
        idx_2_remove =[]
        for idx,(yi,xi) in enumerate(zip(posy,posx)):
            if runsim.A[int(round(yi)),int(round(xi))]==0:
                idx_2_remove.append(idx)

        posx = np.delete(posx,idx_2_remove)  # Position of Particles in X or East direction
        posy = np.delete(posy,idx_2_remove)

        age = np.zeros((len(posx)))
        x_track = [[] for _ in posx]
        y_track = [[] for _ in posy]

        a_count = []

        start2 = time.time()
        #========== Run all particles ===============

        for x, y, a, x_t, y_t in zip(posx, posy, age, x_track, y_track):
            try:
                output = runsim.run_particle(x, y, a,start_date)
                #x_t.append(output[1])
                #y_t.append(output[2])
                a_count.append(output[0])
            except A_landi:
                #x_t.append(np.array([x]))
                #y_t.append(np.array([y]))
                a_count.append(0)
                print('vit eru á landi')

        end2 = time.time()
        print(f'time taken all particles: {end2 - start2}')
        print(np.size(np.nonzero(a_count)))
        x_pos_origin = posx[np.nonzero(a_count)]
        y_pos_origin = posy[np.nonzero(a_count)]
        print(np.shape(a_count))
        print(a_count)

        Plotting_particles = plotting_particles(runsim.A,area)
        #Plotting_particles.plot_particle(x_track,y_track)

        data = {'x': x_pos_origin,
                'y': y_pos_origin}
        data = pd.DataFrame(data)
        date_input = start_date.strftime('%Y%m%d')
        data.to_csv( f'Data_Ian_project/Ian_sampledate_{date_input}_particle_age{daysdelay}_Nparticles_{numpont**2}_age_{3}.csv')
        Plotting_particles.plot_sea_born_map(data=data)

        plt.show()
