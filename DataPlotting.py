
'''
Remaining Steps:
	1. Manually Lookup Missing Data and Save to CSV
	2. Import Manual Data and Plot as Dotted Line

'''
import matplotlib.pyplot as plt
import pandas as pd
import os

project_folder = r'C:\Users\Ryan Tamashiro\Desktop\Ryan\UCI Bootcamp\Project-01\Regional_Climate_Data'
os.chdir(project_folder)

Africa = pd.read_csv(r'Jeddah.csv')
Europe = pd.read_csv(r'Europe-London_United_Kingdom.csv')
Middle_East = pd.read_csv('Middle_East_Jerusalem_Israel.csv')
N_America = pd.read_csv(r'North_American-WashingtonDC_USA.csv')
S_America = pd.read_csv(r'Mexico.csv')
Asia = pd.read_csv(r'East_Asia-Beijing_China.csv')
SE_Asia = pd.read_csv(r'South_Asia-Bangkok_Thailand.csv')
Manual_Example = pd.read_csv(r'Example_Manually_Input_Data.csv')


# Define Plot Dimensions
plt.figure(figsize=(20,10))
plt.style.use('seaborn-darkgrid')
plt.grid(True)
plt.xlim(1968,2020)
plt.ylim(50,100)

# Title, X-Label, Y-Label
plt.title('Regional Temperatures (1970-2018)', color='red', fontsize=20, fontweight=5)
plt.xlabel('Recorded Year', fontsize=16)
plt.ylabel('Temperature (Max)', fontsize=16)

# Plot Regional Temperature Data
plt.plot(Africa['DATE'],Africa['TMAX'], color='orange', label='Sub-Saharan Africa',linewidth=1, marker='.')
plt.plot(Europe['DATE'],Europe['TMAX'], color='blue', label='Europe', linewidth=1, marker='.')
plt.plot(Middle_East['DATE'], Middle_East['TMAX'], color='fuchsia', linewidth=1, marker='.')
plt.plot(N_America['DATE'],N_America['TMAX'], color='green', label='North America', linewidth=1, marker='.')
plt.plot(S_America['DATE'],S_America['TMAX'], color='brown', label='South America', linewidth=1, marker='.')
plt.plot(Asia['DATE'],Asia['TMAX'], color='red', label='Asia', linewidth=1, marker='.')
plt.plot(SE_Asia['DATE'],SE_Asia['TMAX'], color='purple', label='South-East Asia', linewidth=1, marker='.')

# Manual Data Example Plot
plt.plot(Manual_Example['DATE'], Manual_Example['TMAX'], color='fuchsia', label='Middle East', linewidth=1, marker='.', linestyle=':')

# Line Plot Labels
plt.text(Africa['DATE'].tail(1)+.5, Africa['TMAX'].tail(1), 'Sub-Saharan Africa', color='orange', size='medium', horizontalalignment='left')
plt.text(Europe['DATE'].tail(1)+.5, Europe['TMAX'].tail(1), 'Europe', color='blue', size='medium', horizontalalignment='left')
plt.text(Middle_East['DATE'].tail(1)+.5, Middle_East['TMAX'].tail(1), 'Middle East', color='fuchsia', size='medium', horizontalalignment='left')
plt.text(N_America['DATE'].tail(1)-1, N_America['TMAX'].tail(1)-1, 'North America', color='green', size='medium', horizontalalignment='left')
plt.text(S_America['DATE'].tail(1)+.5, S_America['TMAX'].tail(1), 'South America', color='brown', size='medium', horizontalalignment='left')
plt.text(Asia['DATE'].tail(1), Asia['TMAX'].tail(1)-1, 'East Asia', color='red', size='medium', horizontalalignment='left')
plt.text(SE_Asia['DATE'].tail(1)+.5, SE_Asia['TMAX'].tail(1), 'South-East Asia', color='purple', size='medium', horizontalalignment='left')

plt.text(Manual_Example['DATE'].tail(1)-1, Manual_Example['TMAX'].tail(1)+.5, 'Middle East (Ext)', color='fuchsia', size='medium', horizontalalignment='left')

#plt.legend(loc='best')
plt.tight_layout()

save_path = r'C:\Users\Ryan Tamashiro\Desktop\Regional Temperature Plot.png'
plt.savefig(save_path)
plt.show()