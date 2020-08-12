# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:43:00 2020

@author: Jujar Panesar

Code reads in time stamped results. E.g. 12.0000.plt, 14.0000.plt, etc
Results have format x, y, variable_1, variable_2, variable_3, etc, 
where x and y are 2D grid positions and can be x and z, or y and z

The code plots a time stamped color map of a variable
mapped onto the 2D grid positions

E.g. Plot variable_1 on grid positions x and y at time 14.0000

N.b. The data file needs to have headers, and need to know the header names
E.g. In results file:
    column 1 might have header called "x"
    column 2 might have header called "y"
    column 3 might have header called "temperature"
"""

import matplotlib.pyplot as plt                                         #Matplotlib toolkit
import numpy as np                                                      #Numpy toolkit
import pandas as pd                                                     #Pandas toolkit
from mpl_toolkits.axes_grid1 import make_axes_locatable                 #Used to customise plot axes
import collections as cl                                                #Use specialized container datatypes
import re                                                               #Import regular expression operations
import os                                                               #import operating system interfaces

###################################################
################SEARCH WD FOR FILES################
###################################################

curDir = os.getcwd()                                                    #Stores current work dir as a string

for subdir, dirs, files in os.walk(curDir):                             #Loop through subdirectories
    for file in files:                                                  #Loop through the files
        filepath = subdir + os.sep + file                               #Convert filepaths to string
        if filepath.endswith(".plt"):                                   #Isolate .plt results files only

####################################################
############ISOLATE TIME VALUE FROM FILE############
####################################################

            time=re.findall('\d*\.?\d+',filepath)                       #store integers and incl period for item in list
            time=[float(i) for i in time]                               #float the time
            time=int(time[0])                                           #Isolate item 0 in time list

################################################
################READ IN THE DATA################
################################################

            data = pd.read_table(filepath,sep="\s+")                    #Import data from .plt as a pandas table

            x = data["x"].values                                        #Assign variable name
            y = data["y"].values                                        #Assign variable name
            xy_ux = data["ux"].values                                   #Assign variable name
            xy_uy = data["uy"].values                                   #Assign variable name
            xy_uz = data["uz"].values                                   #Assign variable name
            xy_dux = data["dux"].values                                 #Assign variable name
            xy_duy = data["duy"].values                                 #Assign variable name
            xy_duz = data["duz"].values                                 #Assign variable name

################################################
################REORDER THE DATA################
################################################

            extentx=cl.Counter(np.array(x))                             #Makes x a numpy array so we can identify the grid size
            gridsizex = extentx[1]                                      #Identifies the grid size in x
            extenty=cl.Counter(np.array(y))                             #Makes y a numpy array so we can identify the grid size
            gridsizey = extenty[1]                                      #Identifies the grid size in y

            xy_ux = xy_ux.reshape(gridsizex,gridsizey,order='F')        #reshape the variables using fortran ordering
            xy_uy = xy_uy.reshape(gridsizex,gridsizey,order='F')        #reshape the variables using fortran ordering
            xy_uz = xy_uz.reshape(gridsizex,gridsizey,order='F')        #reshape the variables using fortran ordering
            xy_dux = xy_dux.reshape(gridsizex,gridsizey,order='F')      #reshape the variables using fortran ordering
            xy_duy = xy_duy.reshape(gridsizex,gridsizey,order='F')      #reshape the variables using fortran ordering
            xy_duz = xy_duz.reshape(gridsizex,gridsizey,order='F')      #reshape the variables using fortran ordering

##################################################
############WHAT DO YOU WANT TO PLOT?#############
##################################################

            var=xy_uz                                                   #Which variable do you want to plot?

##################################################
################GRAPHING OPTIONS##################
##################################################

            fig, ax = plt.subplots(1, 1, figsize=(7, 7))                #Creates figure for plotting
            asratio = x.max()/y.max()                                   #Aspect ratio for plots
            ax.xaxis.set_ticks([-1,-0.5,0,0.5,1])                       #x axis ticks
            ax.yaxis.set_ticks([-1,-0.5,0,0.5,1])                       #y axis ticks
            ax.set_xlabel(r'$x$', fontsize=16)                          #x label
            ax.set_ylabel(r'$y$', fontsize=16)                          #y label

            plt.imshow(var, aspect=asratio, origin='lower',             #Display contour image
            interpolation='bicubic', extent = (-1,1,-1,1))

            divider = make_axes_locatable(ax)                           #Allows colorbar to be modifiable
            cax = divider.append_axes("right", size="6%", pad=0.2)      #Parmaters for colorbar
            plt.colorbar(cax=cax,ticks=[var.min(),var.max()])           #Plot the colorbar

            time=int(time)                                              #Convert time to an integer
            ttl = fig.suptitle('%1.4f' % time)                          #Set title of contour plot
            ttl.set_position([0.5, 0.95])                               #Position the title
            plt.savefig('%s.png' % (str(time)))                         #Save the figure
            plt.show()                                                  #Show the figure