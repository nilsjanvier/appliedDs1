# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:39:14 2020

@author: Le boss d'Angers
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


df = pd.read_csv("base_earnings.csv")



plt.plot(df.GDP)

plt.show()
