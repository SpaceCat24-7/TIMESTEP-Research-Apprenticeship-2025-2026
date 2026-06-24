# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 00:45:44 2025

@author: Riley
"""

import numpy as np
import matplotlib.pyplot as plt


def get_data(filename):
    #previous script should have already replaced D with E 
    raws = np.genfromtxt(filename)
    timesteps = []
    ID = []
    semi_major_axes = []
    eccentricities = []
    longitudes = []
    for row in raws:
        timesteps.append(row[0])
        ID.append(row[1])
        semi_major_axes.append(row[2])
        eccentricities.append(row[3])
        longitudes.append(row[4])
    data = [timesteps,ID,semi_major_axes,eccentricities,longitudes]
    return data
    
def hist_of_a(a_array):
    figs, ax = plt.subplots()
    ax.hist(a_array,100)
    ax.set_xlabel("Semi-Major Axis (AU)")
    ax.set_yscale("log")
    ax.set_ylabel("Log of Number of Occurences")
    ax.set_title("Figure 1: Occurences of Semi-Major Axes")
    plt.show()
    
def graph_of_a_vs_t(t_array,a_array):
    figs, ax = plt.subplots()
    ax.plot(t_array,a_array,"o")
    ax.set_xlabel("Time Elapsed in Simulation (Myr)")
    ax.set_ylabel("Semi-Major Axis (AU)")
    ax.set_title("Figure 2: Evolution of Semi-Major Axes Over Time")
    plt.show()
    
def hist_of_times(t_array):
    figs, ax = plt.subplots()
    ax.hist(t_array,100)
    ax.set_xlabel("Time Elapsed in Simulation (Myr)")
    ax.set_ylabel("Number of Cometary Orbits")
    ax.set_title("Figure 3: Proportion of Bodies in Cometary Orbits")
    plt.show()
    
def hist_of_IDs(id_array):
    figs, ax = plt.subplots()
    ax.hist(id_array,100)
    ax.set_xlabel("ID Number")
    ax.set_yscale("log")
    ax.set_ylabel("Log of Number of Occurences Where 1AU From Star")
    ax.set_title("Figure 4: Lifetime of Particle Orbits")
    plt.show()
    
def times_vs_rates(t_array):
    pass
    
def main():
    data = get_data("EpsEri_1_updated")
    hist_of_a(data[2])
    graph_of_a_vs_t(data[0], data[2])
    hist_of_times(data[0])
    hist_of_IDs(data[1])
    
    
main()