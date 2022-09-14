# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 00:48:29 2022

@author: Noatok
"""

import json, os, pygame


def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        stats = json.load(file)
        return stats



def write_save(data):
    with open(os.path.join(os.getcwd(), 'save.json'), 'w') as file:
        json.dump(data, file)
        
def load_save():
    try:
        save = load_existing_save('save.json')
        
    except:
        save = create_save()
        write_save(save)
        
    return save
        
def create_save():
    stats = {'mana': 0,
                             'health': 0,
                             'stamina': 0,
                             'curr_exp': 0,
                             'exp_points_limit': 150,
                             'exp_level': 0}

    
    
    return stats
        
        
        
        