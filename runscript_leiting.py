mode = 'cython'
print(f'Mode is on: {mode}. cython mode is fast while python mode is slower')
import time
from datetime import datetime, timedelta
import numpy as np
import numpy.matlib as npm

import matplotlib.pyplot as plt


from particle_tracking_engine.particledata2 import particle_data
import pandas as pd
if mode == 'cython':
    from particle_tracking_engine.particle_tracking_cython import agent_simulation
    from particle_tracking_engine.particle_tracking_cython import A_landi
else:
    from particle_tracking_engine.particle_tracking import agent_simulation
    from particle_tracking_engine.particle_tracking import A_landi

from particle_tracking_engine.plot_particle_FO import plotting_particles

##======== Run import data ==========================================

if __name__ == '__main__':

    t = 35 #27.5  # Simulation time(hours)
    dt = 0.005  # Timestep(hours)
    rh = 1  # how many times you want to realese agents - every hour

    # ======== pre define position and age of each partile beforehand =====
    data = particle_data(numpont=5)
    n = 1000
    posx =np.array([417.7] * n) #npm.repmat(417.7, 1, rh).flatten('F')  # Position of Particles in X or East direction
    posy =np.array( [899] * n) #npm.repmat(898, 1, rh).flatten('F')  # Position of Particles in Y or North direction
    area = [data.IanSgrid]
    # = == == == == == Particle Tracking simutaion == == == == == == == == == == == == == == == ==
    print(f'dt: {dt}')
    runsim = agent_simulation(
        areas=area,
        run_time=t,
        dt=dt,
        diff=True,
    )

    age = np.zeros((len(posx)))
    x_track = [[] for _ in posx]
    y_track = [[] for _ in posy]

    a_count = []

    start2 = time.time()
    #========== Run all particles ===============
    start_date = datetime(2022, 10, 7) + timedelta(hours=9)
    last_pos_x = []
    last_pos_y = []
    for x, y, a, x_t, y_t in zip(posx, posy, age, x_track, y_track):
        try:
            output = runsim.run_particle(x, y, a,start_date)
            x_t.append(output[1])
            y_t.append(output[2])
            a_count.append(output[0])
        except A_landi:
            x_t.append(np.array([x]))
            y_t.append(np.array([y]))
            a_count.append(0)
            print('vit eru á landi')
        last_pos_x.append(output[1][-1])
        last_pos_y.append(output[2][-1])
    data = {'x': last_pos_x,
            'y': last_pos_y}
    data = pd.DataFrame(data)
    end2 = time.time()
    print(f'time taken all particles: {end2 - start2}')
    print(np.size(np.nonzero(a_count)))
    print(np.shape(a_count))
    print(a_count)

    Plotting_particles = plotting_particles(runsim.A,area)
    Plotting_particles.plot_particle(x_track,y_track)
    plt.title('Á sjógv kl. 08 tann 07-okt-2022 og 30 tímar fram')



    Plotting_particles.plot_sea_born_map(data=data)




    plt.show()
