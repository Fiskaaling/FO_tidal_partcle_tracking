mode = 'cython'
print(f'Mode is on: {mode}. cython mode is fast while python mode is slower')
from datetime import datetime
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import  dates

from particle_tracking_engine.particledata2 import particle_data
if mode == 'cython':
    from particle_tracking_engine.particle_tracking_cython import agent_simulation
    from particle_tracking_engine.particle_tracking_cython import A_landi
else:
    from particle_tracking_engine.particle_tracking import agent_simulation
    from particle_tracking_engine.particle_tracking import A_landi

from particle_tracking_engine.plot_particle_FO import plotting_particles
from matplotlib.widgets import Button,TextBox

##======== Run import data ==========================================

if __name__ == '__main__':

    t = 24*7  # Simulation time(hours)
    dt = .005 # Timestep(hours)
    rh = 1  # how many times you want to realese agents - every hour

    #mpl.rcParams['toolbar'] = 'None'
    fig = plt.figure()
    ax = fig.add_subplot(111)

    print('uttan mp')
    data = particle_data(numpont=2)
    print("data:", data)

    area = [data.SVgrid] #Sørvágur

    # ======== pre define position and age of each partile beforehand =====

    # = == == == == == Particle Tracking simutaion == == == == == == == == == == == == == == == ==
    print(f'dt: {dt}')

    runsim = agent_simulation(
        areas=area, #Sørvágur
        run_time=t,
        dt=dt,
        diff=True,
    )

    start2 = time.time()

    Plotting_particles = plotting_particles(runsim.A)
    Plotting_particles.plot_particle([],[], ax=ax)
    ax.set_title('trýst her og fylg lúsini :)',fontsize=15)
    datax = []
    datay = []


    def get_cmap(n, name='hsv'):
        '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
        RGB color; the keyword argument name must be a standard mpl colormap name.'''
        return plt.cm.get_cmap(name, n)

    class interactive_plot:
        def __init__(self,df3,df3_color,start_date):
            self.birth_time = dates.date2num(start_date)
            self.df3 = df3
            self.df3_color = df3_color
            self.lines = []
            self.initial = 0
            self.count_id = 0
        def onclick(self,event):

            x, y = event.xdata, event.ydata
            if x>1 and y>1:
                self.count_id += int(1)
                x_t = []
                y_t =[]
                start2 = time.time()
                #========== Run all particles ===============
                print(self.birth_time,'nú havi eg klikka')
                birth_timestamp = self.birth_time
                print(dates.num2date(birth_timestamp))
                birth_time = dates.num2date(self.birth_time).replace(tzinfo=None)

                a = 0

                try:
                    print("\n   x:", x, "\n   y:", y, "\n   a:", a,'Hví??')
                    output = runsim.run_particle(x, y, a,birth_time)
                    x_t.append(output[1]) #runsim.X.copy())
                    y_t.append(output[2]) #runsim.Y.copy())

                except A_landi:
                    x_t.append(np.array([x]))
                    y_t.append(np.array([y]))
                    print('vit eru á landi')

                print(len(x_t[0])*dt,dt,len(x_t[0]))
                Date = np.arange(0,len(x_t[0])*dt,dt)/24+birth_timestamp

                print(Date,np.size(Date))
                print(np.random.rand(3,))
                print(self.count_id)

                data = {'Date': Date,
                        'id':   self.count_id,
                        'x':    x_t[0],
                        'y':    y_t[0],
                        }
                data = pd.DataFrame(data)

                print(data)
                self.df3 = pd.concat([self.df3, data], ignore_index=True, sort=False)


                end2 = time.time()
                print(f'time taken all particles: {end2 - start2}')
            return

        def play(self, event):

            if self.initial!=1:
                self.initial =1
                start_date_num = dates.date2num(start_date)
                sim_time = np.linspace(start_date_num,start_date_num+(t+24*10)/24,int((t/dt)*0.01))

                dt_loop = sim_time[1] - sim_time[0]
                times = sim_time[0] - dt_loop
                lines = []
                markers = []
                have_particles_enterd = []
                have_particles_been_removed =[]

                cmap = get_cmap(50)  # len(df_now.id.unique()))
                while True:
                    start3 = time.time()
                    times += dt_loop
                    self.birth_time = times
                    self.df3 = self.df3[self.df3.Date>(times-0.25)]
                    df_now = self.df3[self.df3.Date.between(times-0.25,times)]

                    num_particles = df_now.id.unique()

                    for idx in num_particles:

                        if idx not in have_particles_enterd:
                            have_particles_enterd.append(idx)
                            random_color = np.random.randint(1,50)
                            df_now_per_id = df_now[df_now.id == idx]
                            if len(df_now_per_id.x)!=0:
                                markers.extend(ax.plot(df_now_per_id.x.iloc[-1], df_now_per_id.y.iloc[-1], 'o', c = cmap(random_color), markersize=4, mec='k'))
                            lines.extend(ax.plot(df_now_per_id.x.iloc[0::80], df_now_per_id.y.iloc[0::80], '-',c = cmap(random_color), mec='k'))

                        elif len(df_now_per_id.x)>0:

                            for i,(line, marker, idxx) in enumerate(zip(lines, markers, have_particles_enterd)):
                                df_now_per_id = df_now[df_now.id == idxx]

                                x = df_now_per_id.x.iloc[0::80]
                                y = df_now_per_id.y.iloc[0::80]
                                if len(df_now_per_id.x)!=0:
                                    x_m = df_now_per_id.x.iloc[-1]
                                    y_m = df_now_per_id.y.iloc[-1]
                                    marker.set_xdata(x_m)
                                    marker.set_ydata(y_m)
                                line.set_xdata(x)
                                line.set_ydata(y)




                    if len(have_particles_enterd)>0:
                        remove_from_list = []
                        for i,(line, marker, idmix) in enumerate(zip(lines, markers, have_particles_enterd)):

                            df_now_per_id = df_now[df_now.id==idmix]

                            if len(df_now_per_id.x)==0 and idmix not in have_particles_been_removed:
                                remove_from_list.append(i)
                                line.remove()
                                marker.remove()
                                have_particles_been_removed.append(idmix)
                        for i in remove_from_list[::-1]:
                            lines.pop(i)
                            markers.pop(i)
                            have_particles_enterd.pop(i)
                    date_disp = dates.num2date(times)

                    if len(lines)==0:


                        a = 0
                        x = [600,618,200,900,760,150]
                        y = [600,1234,333,760,542,999]
                        for x_0,y_0 in zip(x,y):
                            x_t = []
                            y_t =[]
                            birth_time = dates.num2date(self.birth_time).replace(tzinfo=None)
                            self.count_id += int(1)
                            birth_timestamp = self.birth_time
                            try:
                                output = runsim.run_particle(x_0, y_0, a,birth_time)
                                x_t.append(output[1]) #runsim.X.copy())
                                y_t.append(output[2]) #runsim.Y.copy())

                            except A_landi:
                                x_t.append(np.array([x_0]))
                                y_t.append(np.array([y_0]))
                                print('vit eru á landi')
                            Date = np.arange(0,len(x_t[0])*dt,dt)/24+birth_timestamp



                            data = {'Date': Date,
                                    'id':   self.count_id,
                                    'x':    x_t[0],
                                    'y':    y_t[0],
                                    }
                            data = pd.DataFrame(data)

                            self.df3 = pd.concat([self.df3, data], ignore_index=True, sort=False)

                    txt = ax.text(90, 1390, date_disp.strftime(("%m/%d/%Y, %H:%M")),fontsize=16)


                    plt.pause(0.001)

                    for txt in ax.texts:
                        txt.remove()

                    end4 = time.time()

                    print(f'time to plot all particles: {end4 - start3}')


                Plotting_particles.plot_particle_tracks(df_now.x, df_now.y, times, ax=ax, fig=fig)
                fig.canvas.draw_idle()

        #def submit(self,expression):
        #    """
#
 #           """
 #           self.start_date = dates.date2num(pd.to_datetime(expression))


    #def full(event):
        #manager = plt.get_current_fig_manager()
        #manager.full_screen_toggle()
    #    plt.get_current_fig_manager().full_screen_toggle()

    df2 = { 'Date': [],
            'id': [],
            'x': [],
            'y': [],
          }
    data_color = {'id': [],
                  'color': [],
                  }
    print(df2)

    df3 = pd.DataFrame(df2)
    df3_color = pd.DataFrame(data_color)
    count_id = 0
    start_date = pd.to_datetime("01-jan-2001") # TODO finn utav hvat byrjunar dato er í tidal data
    start_date = datetime(2000, 1, 1)

    Interactive_plot = interactive_plot(df3,df3_color ,start_date)

    #axplay = fig.add_axes([0.88, 0.08, 0.1, 0.075])
    #bnext = Button(axplay, 'Byrja')

    #axbox = fig.add_axes([0.88, 0.28, 0.1, 0.075])
    #text_box = TextBox(axbox, "Evaluate", textalignment="center")
    #text_box.on_submit(Interactive_plot.submit)
    #text_box.set_val("2000-01-01")  # Trigger `submit` with the initial string.

    #axfull = fig.add_axes([0.91, 0.05, 0.1, 0.075])
    #bfull = Button(axfull, 'Full')
    #Interactive_plot.play(4)
    #Interactive_plot.play(9)
    #Interactive_plot.onclick(7)
    #bnext.on_clicked(Interactive_plot.play)
    #bfull.on_clicked()
    cid = fig.canvas.mpl_connect('button_press_event', Interactive_plot.onclick) # 'key_press_event' # 'button_press_event'
#===============================================================
    plt.subplots_adjust(left=0.017,
                        bottom=0.16,
                        right=0.976,
                        top=1,
                        wspace=0.05,
                        hspace=0.1)
                    #ax[0].legend(loc="upper left", fontsize=15)
    fig.set_size_inches(20,15)#(14.69, 10.27)
    Interactive_plot.play(9)


    plt.show()
