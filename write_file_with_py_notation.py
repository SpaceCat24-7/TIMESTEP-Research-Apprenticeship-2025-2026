# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 01:01:28 2025

@author: Riley
"""
'''
def replace_D(filename):
    #the data is given in scientific notation but in FORTRAN format
    #in order for python to handle it, we will rewrite the same file
    #with E in place of D
    file = open(filename,"r")
    new_name = input("What would you like the updated file to be called?")
    updated_file = open(new_name,"w")
    for line in file:
        for char in line:
            if char=="D":
                char.replace("D","E")
        updated_file.write(line)
    return updated_file

def main():
    replace_D("EpsEri_whole_comet_1au.dat")
    
main()
'''
#let's try a more efficient way

'''
def fix_format(filename):
    #the data is given in scientific notation but in FORTRAN format
    #to replace D with E, we'll use the r+ mode of open() 
    #and use the original file instead of wasting memory
    file = open(filename,"r+")
    for line in file:
        new_line = ""
        for char in line:
            if char=="D":
               new_line+= char.replace("D","E")
            else:
                new_line+= char
        file.write(new_line)
    return file
    
    
def main():
    fix_format("EpsEri_whole_comet_1au.dat")
    
main()
'''
#that didn't work either
#"r+" didn't overwrite the existing file, it just appended it
#the result was this weird recursive thing where the file got longer
#with more repetitions each time I ran the code

#third try's the charm!

def fix_format(filename):
    #the data is given in scientific notation but in FORTRAN format
    #in order for python to handle it, we will rewrite the same data
    #with E in place of D, but in a new file
    file = open(filename,"r")
    new_name = input("What would you like the updated file to be called? \n")
    updated_file = open(new_name,"w")
    for line in file:
        new_line = ""
        for char in line:
            if char=="D":
               new_line+= char.replace("D","E")
            else:
                new_line+= char
        updated_file.write(new_line)
    
    
def main():
    fix_format("cometfile.dat")
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
