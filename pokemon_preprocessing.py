#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:07:22 2020

@author: gabrielmedeirosdonascimento
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans

df = pd.read_csv('Pokemon.csv')

## Select Gen 1 Pokemon 
    # this selection is going to be fairly easy, since there is
    # a generation column

gen1_df = df[df.Generation == 1]
gen1_df

## Erase Mega Evolutions, since we are only taking in acount the "raw" pokemon

gen1_df_no_mega = gen1_df[gen1_df.Name.map(len) < 15]


## As the cleaning removed the indexes, we should reindex.
# This code sets the new index to match the Pokedex value
clean_pkmn = gen1_df_no_mega.set_index('#')

clean_pkmn.to_csv(r'\clean_pokemon.csv', index = True)