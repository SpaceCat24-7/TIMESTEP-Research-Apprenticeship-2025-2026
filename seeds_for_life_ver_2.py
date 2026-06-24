# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 10:48:59 2025

@author: Riley
"""


import numpy as np
import matplotlib.pyplot as plt

t_axis = np.linspace(0,800,801)

def get_data(filename):
    #previous script should have already replaced D with E 
    raws = np.genfromtxt(filename)
    timesteps = []
    ID = []
    init_axes = []
    semi_major_axes = []
    eccentricities = []
    inclinations = []
    longitudes = []
    for row in raws:
        timesteps.append(row[0])
        ID.append(row[1])
        init_axes.append(row[2])
        semi_major_axes.append(row[3])
        eccentricities.append(row[4])
        inclinations.append(row[5])
        longitudes.append(row[6])
 
    data = [timesteps,ID,init_axes,semi_major_axes,eccentricities,
            inclinations, longitudes]
    return data
    
def filter_by_e(e_array,other,less):
    if less:
        indices = np.where(np.asarray(e_array)<0.2)
    else:
        indices = np.where(np.asarray(e_array)>0.2)
    indices = list(indices)
    new = [item for index, item in enumerate(other) if index in indices[0]]
    return new

def hist_of_a(a_array):
    figs, ax = plt.subplots()
    ax.hist(a_array,451)
    ax.set_xlabel("Initial Semi-Major Axis (AU)")
    ax.set_yscale("log")
    ax.set_ylabel("Log of Number of Occurences")
    ax.set_title("Lifetime of Particle Orbits By Origin")
    plt.show()
    
def graph_of_a_vs_t(t_array,a_array):
    figs, ax = plt.subplots()
    ax.plot(t_array,a_array,"o")
    ax.set_xlabel("Time Elapsed in Simulation (Myr)")
    ax.set_ylabel("Semi-Major Axis (AU)")
    ax.set_title("Evolution of Semi-Major Axes Over Time")
    plt.show()
    
def hist_of_times(t_array):
    figs, ax = plt.subplots()
    ax.hist(t_array,451)
    ax.set_xlabel("Time Elapsed in Simulation (Myr)")
    ax.set_ylabel("Number of Cometary Orbits")
    ax.set_title("Proportion of Bodies in Cometary Orbits")
    plt.show()
    
def hist_of_IDs(id_array):
    figs, ax = plt.subplots()
    ax.hist(id_array,100)
    ax.set_xlabel("ID Number")
    ax.set_yscale("log")
    ax.set_ylabel("Log of Number of Occurences Where 1AU From Star")
    ax.set_title("Lifetime of Particle Orbits")
    plt.show()
    
def times_vs_rates(t_array, a_array):
    # for later: include mass of star in Kepler's law
    
    passages_per_t = find_rate_of_passages(t_array, a_array)
    figs, ax = plt.subplots()
    t_array, i = np.unique(t_array,return_index = True)
    # ask Virginie why time array goes to 451
    # still don't know but this works, just perhaps slightly offset
    ax.plot(t_array[:-1],np.asarray(passages_per_t))
    ax.set_xlabel("Time (Myr)")
    ax.set_ylabel("Amount of Passages Per Myr")
    ax.set_title("Rate of Particle Passages Over Time")
    plt.show()
    
def find_rate_of_passages(t_array, a_array):
    array_of_comet_arrays = []
    comets = []
    
    for i in range(len(t_array)-1):
        if i==0:
            comets.append(a_array[i])
        elif t_array[i]==t_array[i-1]:
            print(i)
            comets.append(a_array[i])
        else:
            array_of_comet_arrays.append(np.asarray(comets))
            comets = []
            comets.append(a_array[i])
    array_of_orbit_arrays = []
    for obj in array_of_comet_arrays:
        orbits = obj**(3/2)
        array_of_orbit_arrays.append(orbits)
    passages_per_t = []
    for orbits in array_of_orbit_arrays:
        tot_passages = 0
        p_max = max(orbits)
        for p in orbits:
            tot_passages+= p_max/p
        rate_per_year = tot_passages/p_max
        passages_per_t.append(rate_per_year)
    return passages_per_t
    
def hist_of_e(e_array):
    figs, ax = plt.subplots()
    ax.hist(e_array,100) 
    ax.set_yscale("log")
    ax.set_xlabel("Eccentricity of Orbit")
    ax.set_ylabel("Log of Amount of Particles")
    ax.set_title("Eccentricity of Particle Orbits")    
    plt.show()   
    
def a_occurence_by_e(lim_a_array, less):
    figs, ax = plt.subplots()
    ax.hist(lim_a_array, 1000)
    ax.set_yscale("log")
    ax.set_xlabel("Semi-Major Axis (AU)")
    ax.set_ylabel("Log of Amount of Particles")
    if less:
        ax.set_title("Figure 7: Semi-Major Axes of Particles with Eccenticity Less Than 0.2") 
    '''
    else: 
        plt.xlim(0,4)
        ax.set_title("Figure 8: Semi-Major Axes of Paricles with Eccenticity Greater Than 0.2")
    '''
    plt.show()
        
def plot_rates_by_es(t_array, filtered_a_array, a_array):
    filtered_t_array = []
    i = 0
    for a in a_array:
        if a in filtered_a_array:
            filtered_t_array.append(t_array[i])
        i+=1
    passages_per_t = find_rate_of_passages(filtered_t_array, filtered_a_array)
    figs, ax = plt.subplots()
    #ax.set_xlim(0,451)
    ax.set_xlabel("Time Elapsed in Simulation (Myr)")
    ax.set_ylabel("Amount of Passages Per Myr")
    ax.set_title("Rate of Passages Over Time for Particles With \n Eccentricity Less Than 0.2")
    ax.plot(np.unique(filtered_t_array)[:-1], np.asarray(passages_per_t))     
    plt.show() 
    
    
def two_d_hist_nu_vs_i(nu_array, i_array):
    figs, ax = plt.subplots()
    counts, xedges, yedges, im = ax.hist2d(nu_array, i_array, 100, cmap = "inferno")
    ax.set_label("label via method")
    ax.set_title("Distribution in Inclination and Longitude of Periastron")
    ax.set_xlabel("Longitude of Periastron (degrees)")
    ax.set_ylabel("Inclination (degrees)")
    #ax.set_xlim(0,3)
    #ax.set_ylim(0,3)
    cbar = figs.colorbar(im, ax=ax)
    cbar.set_label('Counts in bin')
    plt.show()
    
def normalize_angles(angles):
    normed = []
    for angle in angles:
        normalized_angle = (angle + 180) % 360 - 180
        normed.append(normalized_angle)
    return normed
    
    
def main():
    
    data = get_data("EpsEri_whole_comet_1AU-450Myr.dat")
    hist_of_a(data[2])
    #graph_of_a_vs_t(data[0], data[3])
    #hist_of_times(data[0])
    #hist_of_IDs(data[1])
    #times_vs_rates(data[0], data[3])
    hist_of_e(data[4])
    #a_occurence_by_e((data[4], data[3], False), False)
    normed_longitudes = normalize_angles(data[6])
    normed_inclinations = normalize_angles(data[5])
    normed_longitudes = (filter_by_e(data[4], normed_longitudes, False))
    normed_inclinations = (filter_by_e(data[4], normed_inclinations, False))
    #two_d_hist_nu_vs_i(normed_longitudes, normed_inclinations)
    filtered_a_array = filter_by_e(data[4], data[2], True)
    plot_rates_by_es(data[0],filtered_a_array, data[2])
    
    
main()