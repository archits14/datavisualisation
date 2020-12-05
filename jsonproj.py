import matplotlib.pyplot as plt 
import pandas as pd 

#importing the crime data from json file
crimedata = pd.read_json('crimedata.json', orient='columns')

#user prompt for asking what data needs to be plotted
option = input("Pls let us know what data you would be interested in seeing in the plot: Enter 1 for No. of Crimes against Year and 2 for No. of Settled Cases against Year:")

#condition to plot data which is for number of crimes against years
if (option == '1'):
    plt.plot((crimedata.loc[:,'year']), (crimedata.loc[:,'crimes']), label='line 1', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.title('Crimes against Years - Line Plot')
    plt.show()

    plt.bar((crimedata.loc[:,'year']), (crimedata.loc[:,'crimes']), label='line 1', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.title('Crimes against Years - Bar Graph')
    plt.show()

#condition to plot data which is for number of settled cases against years
elif(option == '2'):
    plt.plot((crimedata.loc[:,'year']), (crimedata.loc[:,'settledCases']), label='line 1', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Number of Settled Cases')
    plt.title('Settled Cases against Years - Line Plot')
    plt.show()

    plt.bar((crimedata.loc[:,'year']), (crimedata.loc[:,'settledCases']), label='line 1', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Number of Settled Cases')
    plt.title('Settled Cases against Years - Bar Graph')
    plt.show()

else:
    print("Wrong Input")