# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:21:22 2023

@author: Pei ziyu
"""
import unittest
import os
import numpy as np
import matplotlib.pyplot as plt

from GUI import download_result
# Test function download_result()
def test_download_result():
    # Create a sample Matplotlib figure object
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    # Set the global variable fig_s to the sample figure object
    global fig_s
    fig_s = fig
    # Call the download_result() function
    download_result()
    # Check if the output files exist
    assert os.path.exists('output/suitabilityMap.png')
    assert os.path.exists('output/suitabilityMap.txt')
    # Clean up the output files
    os.remove('output/suitabilityMap.png')
    os.remove('output/suitabilityMap.txt')
