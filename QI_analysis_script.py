

import matplotlib.pyplot as plt

from aa_JPK_AFM_classes import QIMap



#%%
file = '*your path to .jpk-qi-data file*'
result_path = '*your generic result path*'

#%% make a QIMap object and import the data/open the file
qi = QIMap()
qi.import_data(file)
qi.set_save_directory(result_path) #results will be saved at this location

#%% prepare the data for analysis by defining how each force curve should be corrected
 
qi.open_sample_fd_curve()
qi.correct_sample_fd_curve(baseline_correction = {'method':'linear', 'frac_data': (0.0,0.5)})
qi.set_corrections()


#%% analyze the topograhy

qi.get_topography()
qi.plane_fit_topography()


#%% plot the topography


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
c2 = ax2.imshow(qi.data['topography_mod'], extent = [0, 5, 0, 5], origin = 'lower', cmap = 'afmhot')
cbar2 = fig2.colorbar(c2, ax=ax2)
cbar2.set_label('Measured height / \u03BCm', rotation = 270, labelpad = 20)
ax2.set_xlabel('Position / \u03BCm')
ax2.set_ylabel('Position / \u03BCm')
ax2.set_title('Biofilm Topography')