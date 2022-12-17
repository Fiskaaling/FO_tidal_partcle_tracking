import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from particle_tracking_engine.Tidal_data import tidal_data
from particle_tracking_engine.plot_particle_FO import plotting_particles
import matplotlib.colors as Cmap
import os


def get_cmap(n, name='hsv'):
       '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
       RGB color; the keyword argument name must be a standard mpl colormap name.'''
       return plt.cm.get_cmap(name, n)
# folder path
dir_path = r'Data_Ian_project'

# list file and directories
res = os.listdir(dir_path)
print(res)

#========== Load tidal data ==============
DATA = tidal_data()



fig, ax = plt.subplots()
#=============== define the 9 different FO areas ===================
y_definde_areas = [1488/3,1488/3*2,1488/3*3]
x_definde_areas = [1088/3,1088/3*2,1088/3*3]

Land = np.where(DATA.MajM2>0, 1, 0)


#ax.invert_yaxis()


Plotting_particles = plotting_particles(Land)
# Plotting_particles.plot_particle(x_track,y_track)
for file in res:
       #fig,ax = plt.subplots()
       #ax.set_title(file)
       data = pd.read_csv(f'Data_Ian_project/{file}', index_col=0)
       #Plotting_particles.plot_sea_born_map(data=data,ax=ax,fig=fig)


       for i,(x_d,y_d) in enumerate(zip(x_definde_areas,y_definde_areas)):
              area_nr = i+1
              ax.plot([0,1088],[y_d,y_d],'k-',lw=1.5)
              ax.plot([x_d, x_d],[0, 1488], 'k-', lw=1.5)

              if i==0:
                     ax.text(x_d-(1088/3)/2,425,f'{1}',fontsize = 13)
                     ax.text(x_d-(1088/3)/2,925, f'{2}',fontsize = 13)
                     ax.text(x_d-(1088/3)/2,1425, f'{3}',fontsize = 13)
              elif i ==1:
                     ax.text(x_d - (1088 / 3) / 2, 425, f'{4}', fontsize=13)
                     ax.text(x_d - (1088 / 3) / 2, 925, f'{5}', fontsize=13)
                     ax.text(x_d - (1088 / 3) / 2, 1425, f'{6}', fontsize=13)
              elif i==2:
                     ax.text(x_d - (1088 / 3) / 2, 425, f'{7}', fontsize=13)
                     ax.text(x_d - (1088 / 3) / 2, 925, f'{8}', fontsize=13)
                     ax.text(x_d - (1088 / 3) / 2, 1425, f'{9}', fontsize=13)


       Xlims = np.array([0, 1088])
       Ylims = np.array([0, 1488])
       #ax.set_xlim(Xlims)
       #ax.set_ylim(Ylims)

#fig = plt.figure(figsize=(6, 5), dpi=200)
#left, bottom, width, height = 0.2, 0.1, 0.7, 0.8
#ax = fig.add_axes([left, bottom, width, height])

Ian_sample_dates = pd.read_csv('sample_dates_Ian.csv')
Ian_sample_dates.Dates = pd.to_datetime(Ian_sample_dates.Dates)
ticks_0 = Ian_sample_dates.iloc[0:3]
ticks =[]
cmap = get_cmap(9)
for file in res:

       ticks.append(file[15:19] + '-' + file[19:21] + '-' + file[21:23])
print(ticks)
df_area_all = pd.DataFrame([])
#==================== devide particle origens into map regions =====================
for idx, (files,sample_dates) in enumerate(zip(res,Ian_sample_dates.Dates)):
       # ========== Load simulation data ==================
       Data_particle_origin = pd.read_csv(f'Data_Ian_project/{files}', index_col=0)
       #print(Data_particle_origin)
       print(files)
       region_origin =[]
       x_d_0 =0
       test_area = 0
       for x_d in x_definde_areas:

              y_d_0 = 0
              for y_d in y_definde_areas:
                     number_particle_inarea = Data_particle_origin[Data_particle_origin.x.between(x_d_0,x_d)
                                                            & Data_particle_origin.y.between(y_d_0,y_d)]

                     region_origin.append(len(number_particle_inarea))
                     test_area += 1
                     print(x_d_0, x_d, y_d_0, y_d,len(number_particle_inarea),test_area)
                     y_d_0 = y_d

              x_d_0 =x_d
       #print(region_origin)

       df_area = {'sample_date':ticks[idx],
                  'delay': 6,
                  'area_1': region_origin[0],
                  'area_2': region_origin[1],
                  'area_3': region_origin[2],
                  'area_4': region_origin[3],
                  'area_5': region_origin[4],
                  'area_6': region_origin[5],
                  'area_7': region_origin[6],
                  'area_8': region_origin[7],
                  'area_9': region_origin[8],

                  }
       df_area = pd.DataFrame(df_area,index=[0])
       df_area_all  = pd.concat([df_area_all,df_area])
        #np.arange(len(names))
       #print(ticks)
       #for i in region_origin:
       '''
       if idx ==0:
              for j in range(9):
                     if j==0:
                            ax.bar(ticks[idx], region_origin[j], width, label=f'area {j+1}',color=cmap(j))
                     else:
                            ax.bar(ticks[idx], region_origin[j], width, label=f'area {j+1}',bottom =region_origin[j-1],color=cmap(j) )
       else:
              for j in range(9):
                     if j == 0:
                            ax.bar(ticks[idx], region_origin[j], width, label=f'area {j+1}',color=cmap(j))
                            print(region_origin[j],j)
                     else:
                            ax.bar(ticks[idx], region_origin[j], width, label=f'area {j+1}', bottom=region_origin[j - 1],color=cmap(j))
                            print(region_origin[j],j)
       '''
#ax.bar(ticks, coffee, width, align="center", label='Tea',
#       bottom=water)
#ax.bar(ticks, water, width, align="center", label='Water')

df_area_all.reset_index(inplace =True)
df_area_all = df_area_all.drop('index',axis=1)
print(df_area_all)
df_area_all.set_index('sample_date',inplace=True)
df_area_all.drop('delay',axis=1).plot.bar(stacked=True,rot=45)
plotdata = df_area_all.drop('delay',axis=1)
stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
stacked_data.plot.bar(stacked=True,rot=45)
plt.legend(loc='lower left', bbox_to_anchor=(1, 0.8))
#plt.legend()
plt.show()
'''
import matplotlib.pyplot as plt
#==================== devide Faroese into 6 sections

Cross_points_x = 1088/6
Cross_points_y = 1488/6


Sampledate_9 = [4,5,7,2,1]

plt.hist(Sampledate_9)
plt.show()
'''