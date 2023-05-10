# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:05:07 2023

@author: Pei ziyu
"""

''' 
    import part
'''
import numpy as np #import numpy
# Use the numpy library to convert the data in a file to array format.

import matplotlib.pyplot as plt #import matplotlib
# The Matplotlib library is used to display the images

import matplotlib.backends.backend_tkagg as tkagg
# Provides an interface to embed Matplotlib graphics into Tkinter programs

import csv # read data

import tkinter as tk  #import tkinter
# TKinter is a module for windowing visual design using python. The interface library is easy to use.

import os #To use startfile and save function

import doctest #For code test

''' 
    import part
'''

#Global variables
#Define global variable to store current canvas object
current_canvas1 = None
current_canvas2 = None
#calculate weight
scaled_sum = None
fig_s = None


#Using tkinter to define the GUI window
#Instantiating object
window = tk.Tk()


#Change icon
window.iconbitmap("./icon/stone.ico")
#Naming the window
window.title('Rock Aggregate Site Suitability Analysis')

#Set window size
window.geometry("1100x720")



####
#Define all functions
#Read input data
def read_data(file_path):
    '''
    This function reads the input file specified by file_path. 
    The file is assumed to be in a comma-separated value (CSV) format where each line represents a row of data, and values are separated by commas. 
    
    Parameters
    ----------
    file_path : Str
             The path to the input file to be read.

    Returns
    -------
    data : List
        Representing the data read from the input file..
    num_rows : Int
        The number of rows in the input file.
    num_cols : Int
        The number of columns in the input file.
    
    
    >>> read_data('./test/test_read_data.txt')
    ([[1.0, 1.0, 1.0], [4.0, 4.0, 4.0], [6.0, 6.0, 6.0]], 3, 3)
    '''
    with open(file_path, newline='') as f:
        data = []
        for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
            row = []
            for value in line:
                row.append(value)
            data.append(row)
    num_rows = len(data)
    num_cols = len(data[0])
    return data, num_rows, num_cols



#Creat slider class
class Slider:
    '''
    Parameters:
    -----------
    master : object
        The master object of the slider.
    label_text : str
        The text to display above the slider.
    default_value : float
        The default value of the slider.
    from_ : float
        The minimum value of the slider.
    to : float
        The maximum value of the slider.
    resolution : float
        The resolution of the slider.
    length : int
        The length of the slider.

    Returns:
    --------
    None.
    '''
    def __init__(self, master, label_text, default_value, from_=0, to=1, resolution=0.01, length=200):
        self.master = master
        self.label_text = label_text
        self.from_ = from_
        self.to = to
        self.resolution = resolution
        self.length = length

        # Create label
        self.label = tk.Label(self.master, text=self.label_text)
        self.label.grid()

        # Create slider
        self.slider = tk.Scale(self.master, from_=self.from_, to=self.to, resolution=self.resolution,
                               orient=tk.HORIZONTAL, length=self.length)
        self.slider.set(default_value)
        self.slider.grid(padx=10, pady=10)

    def get(self):
        
        """
        Gets the current value of the slider.

        Parameters:
        -----------
        None.

        Returns:
        --------
        float
            The current value of the slider.
        """
        return self.slider.get()

    def set(self, value):
        """
        Sets the value of the slider to a specified value.

        Parameters:
        -----------
        value : float
            The value to set the slider to.

        Returns:
        --------
        None.
        """
        self.slider.set(value)


#Define Matplotlib figure function
def plot_data(data_list, title_list):
    '''
    This is a function that plots a Matplotlib graph; 
    The following is a description of each parameter and return value:

    Parameters
    ----------
    data_list: 
        A list of the data to be plotted.
    title_list: 
        A list of the titles corresponding to each dataset.

    Returns
    -------
    fig_f: 
        Matplotlib graph object.
    
    canvas1: 
        the canvas object for drawing Matplotlib graphs in the Tkinter window.
    
    
    global variables: 
        current_canvas1: the current canvas object in the Tkinter window on which the Matplotlib graph is drawn
    
    The main steps in the function are:

        1.Clear the canvas object in the current window.
        2.Create a new Matplotlib graph.
        3.Iterate over each dataset, creating subplots and plotting the corresponding dataset, setting the title and colour bar.
        4.Adjust the spacing between the subplots.
        5.Create a Tkinter canvas and display the Matplotlib graph in it.
        6.Update global canvas variables and return Matplotlib graphs and Tkinter canvas objects for external calls.
    
    '''
    global current_canvas1
    #Clear current canvas
    clear_canvas1()
        
    #Create Matplotlib figure
    fig_f, ax1 = plt.subplots(1, len(data_list), figsize=(10, 4)) # 1 row, Cols of data numbers
    fig_f.subplots_adjust(wspace=0.3)      
    #Iteration makes the data correspond to
    for i in range(len(data_list)):
        img1 = ax1[i].imshow(data_list[i], cmap='viridis')
        ax1[i].set_title(title_list[i])
        fig_f.colorbar(img1, ax=ax1[i], shrink=0.9, pad=0.05) # shrink to resize, pad to adjust distance

    #Adjust spacing between subplots
    plt.tight_layout() #Automatic spacing between subplots using the plt.tight_layout()
    #Create the FigureCanvasTkAgg object
    #Create a canvas to display the figure in the Tkinter window
    canvas1 = tkagg.FigureCanvasTkAgg(fig_f, master=factor_frame) #FigureCanvasTkAgg is a Canvas component used to display Matplotlib graphics in the Tkinter window
    canvas1.get_tk_widget().pack() # Return the Canvas object and place in window
    #Update global canvas variable
    current_canvas1 = canvas1
    #Fig binded in windowTK 
    canvas1.draw()
    return fig_f,canvas1 #For external calls


#test calculate()
def test_calculate():
    '''
        This function is mainly to test that the calculation function is working properly
        
    
    >>> test_calculate()
    [[0, 0, 0], [127, 127, 127], [255, 255, 255]]
    '''
    geology_weight = 0.2
    population_weight = 0.2
    transport_weight = 0.6
    num_rows = 3
    num_cols = 3
    geology_data = [[1,1,1],[2,2,2],[3,3,3]]
    population_data =[[4,4,4],[5,5,5],[6,6,6]]
    transport_data = [[7,7,7],[8,8,8],[9,9,9]]
     #Define the total of weights to facilitate if statements
    #Check if all weights are non-zero
    if geology_weight == 0 or population_weight == 0 or transport_weight == 0:
        tk.messagebox.showinfo(title='Error', message= 'All weights must be non-zero.')
        raise ValueError("Error: All weights must be non-zero.")
        return
    
    #Check if total weight equals to 1
    total_weight = geology_weight + population_weight + transport_weight
    if total_weight != 1.0:
        tk.messagebox.showinfo(title='Error', message= 'Weights must sum to 1.00.')
        raise ValueError("Weights must sum to 1.0")
        return
  
    #Weighted sum calculation --> suitability
    suitability = [[0 for _ in range(num_cols)] for _ in range(num_rows)] #Initialization data
    for i in range(num_rows):
        for j in range(num_cols):
            suitability[i][j] = (geology_data[i][j] * geology_weight +
                                  population_data[i][j] * population_weight +
                                  transport_data[i][j] * transport_weight)

    #Get maximum and minimum values --> normalized --> scaled to 0-255
    min_val = min(min(row) for row in suitability)
    max_val = max(max(row) for row in suitability)
    scaled_sum = [[int((val - min_val) / (max_val - min_val) * 255) for val in row] for row in suitability]

    return scaled_sum


#Defining the main function -- Weighting and generation of suitability fig
def calculate():
    '''
    This is a function called "calculate", 
    which is responsible for calculating the suitability score for each factor based on the weights assigned to each layer.
    
    
    Parameters:
        None

    Raises
    ------
    ValueError
        When the condition is not met, the program reports an error.

    Returns
    -------
    scaled_sum : 
        A list of lists representing the calculated suitability score for each factor, scaled to 0-255.
    fig_s : 
        A Matplotlib figure object representing the suitability map.



    Global Variables:
        current_canvas2
        
    The main steps of this function are:
        
        1. Get the weights assigned to each factor from the slider values.
        2. Check if all weights are non-zero and if their total equals 1.0.
        3. Calculate the suitability score for each factor based on the weights assigned to each layer.
        4. Normalize and scale the suitability score to a range of 0-255.
        5. Create a new Matplotlib figure.
        6. Display the suitability map on the Matplotlib figure.
        7. Create a Tkinter canvas and display the Matplotlib figure in it.
        8. Update global canvas variable and return the suitability score and Matplotlib figure objects for external calls.
    '''
    global current_canvas2, fig_s,scaled_sum
   
    # Get slider value
    geology_weight = geology_slider.get()
    population_weight = population_slider.get()
    transport_weight = transport_slider.get()
    
    
    #Define the total of weights to facilitate if statements
    # Check if all weights are non-zero
    if geology_weight == 0 or population_weight == 0 or transport_weight == 0:
        tk.messagebox.showinfo(title='Error', message= 'All weights must be non-zero.')
        raise ValueError("Error: All weights must be non-zero.")
        return
    
    # Check if total weight equals to 1
    total_weight = geology_weight + population_weight + transport_weight
    if total_weight != 1.0:
        tk.messagebox.showinfo(title='Error', message= 'Weights must sum to 1.00.')
        raise ValueError("Weights must sum to 1.0")
        return
    # Clear current canvas
    clear_canvas2()
    # Weighted sum calculation --> suitability
    suitability = [[0 for _ in range(num_cols)] for _ in range(num_rows)] #Initialization data
    for i in range(num_rows):
        for j in range(num_cols):
            suitability[i][j] = (geology_data[i][j] * geology_weight +
                                  population_data[i][j] * population_weight +
                                  transport_data[i][j] * transport_weight)

    #Get maximum and minimum values --> normalized --> scaled to 0-255
    min_val = min(min(row) for row in suitability)
    max_val = max(max(row) for row in suitability)
    scaled_sum = [[int((val - min_val) / (max_val - min_val) * 255) for val in row] for row in suitability]
    
    #Create a new figure
    fig_s, ax2 = plt.subplots(1, 1, figsize=(10, 4))
    #Show the matrix as an image with a specified colormap
    img2 = ax2.imshow(scaled_sum, cmap='viridis')
    #Add the location of the colorbar[left, bottom, width, height]
    cbar_ax = fig_s.add_axes([0.63, 0.12, 0.02, 0.77])
    fig_s.colorbar(img2, cax=cbar_ax)
    #Add a title to the plot
    ax2.set_title('Suitability Map')
    canvas2 = tkagg.FigureCanvasTkAgg(fig_s, master=suitability_frame) #FigureCanvasTkAgg is a Canvas component used to display Matplotlib graphics in the Tkinter window
    canvas2.get_tk_widget().pack() # Return the Canvas object and place in window
    #Update global canvas variable
    current_canvas2 = canvas2
    #fig binded in windowTK 
    canvas2.draw()
    #In the calculate() function, the result image is assigned to result img and returned. Then, in the download_result() function, the calculate() function is called to get the result image and save it to a local file.
    return scaled_sum, fig_s



# Test function download_result()
def test_download_result():
    '''
        This function is mainly to test that the download_result function is working properly

    
    >>> test_download_result()
    <Figure size 720x288 with 2 Axes>
    '''
    scaled_sum = [[0, 0, 0], [127, 127, 127], [255, 255, 255]]
    # Create a sample Matplotlib figure object
    fig_t, ax3 = plt.subplots(1,1,figsize=(10,4))
    img3 = ax3.imshow(scaled_sum, cmap='viridis')
    ax3.set_title('test')
    #Add the location of the colorbar[left, bottom, width, height]
    cbar_ax_t = fig_t.add_axes([0.7, 0.12, 0.02, 0.77])
    fig_t.colorbar(img3, cax=cbar_ax_t)
    # Set the global variable fig_s to the sample figure object
    global fig_s
    fig_s = fig_t
    #Call the download_result() function
    #Get the absolute path to the directory where the current script is located
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #Splice the output folder and image file names into a full path
    image_path = os.path.join(script_dir, 'test', 'test_download.png')
    txt_path = os.path.join(script_dir, 'test', 'test_download.txt')
    #Save img
    fig_s.savefig(image_path) #Save result image to file
    #os.startfile(image_path)  #Use the os.startfile() function to open a file --> Like auto open
    #os.startfile(txt_path)    #Use the os.startfile() function to open a file --> Like auto open
    np.savetxt(txt_path,scaled_sum,delimiter=",", fmt='%d')
    return fig_s



# Print result image
def download_result():
    '''
    This function downloads the result of the suitability analysis as an image file and a text file.

    Parameters:
        None
    
    Returns:
        None

    Global Variables:
        fig_s: The current Matplotlib figure object.
        scaled_sum: The matrix representing the scaled suitability values.

    The main steps of this function are:
        
        1. Check if there is a valid Matplotlib figure object. If not, raise an error and show a message box.
        2. Get the absolute path to the directory where the current script is located.
        3. Splice the output folder and image file names into a full path.
        4. Save the current Matplotlib figure object as a PNG image to the specified location.
        5. Use the os.startfile() function to open the saved image file.
        6. Save the matrix of scaled suitability values as a text file to the specified location.
        7. Show a message box to indicate that the download is complete.
    '''
    
    global fig_s,scaled_sum
    if fig_s is None:
        tk.messagebox.showinfo(title='Error', message= 'The current result is empty, please perform suitability analysis first.')
        raise ValueError("The current result is empty, please perform suitability analysis first.")
    else:
        #Get the absolute path to the directory where the current script is located
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #Splice the output folder and image file names into a full path
        image_path = os.path.join(script_dir, 'output', 'suitabilityMap.png')
        txt_path = os.path.join(script_dir, 'output', 'suitabilityMap.txt')
        #Save img
        fig_s.savefig(image_path) #Save result image to file
        os.startfile(image_path)  #Use the os.startfile() function to open a file --> Like auto open
        np.savetxt(txt_path,scaled_sum,delimiter=",", fmt='%d')
        tk.messagebox.showinfo(title='Success', message= 'Download image complete.')


# Define clear canvas1 function
def clear_canvas1():
    global current_canvas1
    if current_canvas1 is not None:
        current_canvas1.get_tk_widget().destroy()
        current_canvas1 = None
  

# Define clear canvas2 function
def clear_canvas2():
    global current_canvas2,fig_s
    #clear alculated fig
    fig_s =None
    if current_canvas2 is not None:
        current_canvas2.get_tk_widget().destroy()
        current_canvas2 = None

# Define clear all canvas function
def clearAll():
    clear_canvas1() #clear first
    clear_canvas2() #clear second
    
    
#Define quit tk function
def quit_window():
    window.quit() #Stopping the Tkinter event loop
    window.destroy() #Destroy the window and release all resources




####
#Read data
#Read the geology, population, and transport data from their respective input files
geology_data, num_rows, num_cols = read_data('./input/geology.txt')
population_data, _, _ = read_data('./input/population.txt')
transport_data, _, _ = read_data('./input/transport.txt')


#Create the Matplotlib figure
data_list = [geology_data, population_data, transport_data]
title_list = ['Geology', 'Population', 'Transport']


####
## Create the GUI elements
#Title frame
title_frame = tk.Frame(window)
title_frame.pack(fill=tk.BOTH, expand=False) 

#Title label
title_label = tk.Label(title_frame, text="Rock Aggregate Site Suitability Assessment System", fg='#0066cc', font=("Arial", 24))
title_label.pack()


#Content frame
content_frame = tk.Frame(window)
content_frame.pack(fill=tk.Y, expand=False) #cancel fill all space and auto expand

#Left frame
left_frame = tk.Frame(content_frame)
left_frame.grid(row=0, column=0, padx=20, pady=10)

#left content
factor_frame = tk.LabelFrame(left_frame, text="Influence factors", width=722, height=306, bd=0.5, relief=tk.SOLID, labelanchor='n')
factor_frame.pack(side="top", padx=10, pady=10)

suitability_frame = tk.LabelFrame(left_frame, text="Suitability site", width=722, height=306, bd=0.5, relief=tk.SOLID, labelanchor='n')
suitability_frame.pack(side="bottom", padx=10, pady=10)

#right frame
right_frame = tk.Frame(content_frame,bd=0.5, relief=tk.SOLID)
right_frame.grid(row=0, column=1)

#right content
control_frame = tk.LabelFrame(right_frame, text="Control panel", width=200, height=380, bd=0.5, relief=tk.SOLID, labelanchor='n')
control_frame.pack(side="top",padx=15, pady=15)

output_frame = tk.LabelFrame(right_frame, text="Output panel", width=300, height=380, bd=0.5, relief=tk.SOLID, labelanchor='n')
output_frame.pack(side="bottom",padx=15, pady=15)



##button
#control_frame button
showfig_button = tk.Button(control_frame, text='Display Image', bg='#429ce3', command=lambda: plot_data(data_list, title_list), width=17,padx=3, pady=2) #lambda <->simple callback functions.
calculate_button = tk.Button(control_frame, text='Calculate Suitability',bg='#429ce3', font=('Arial', 10),command=calculate,width=15,padx=3)
#output_frame button
download_button = tk.Button(output_frame, text="Save & Print", bg='#429ce3',font=('Arial', 10), command=download_result,width=15,padx=3)
clearAll_button = tk.Button(output_frame, text="Clear",bg='#429ce3', command=clearAll, width=17,padx=3, pady=2) #clear all canvas
quit_button = tk.Button(output_frame, text="Quit",bg='#429ce3', command=quit_window, width=17,padx=3, pady=2)


showfig_button.grid(padx=8, pady=15)
calculate_button.grid(padx=8, pady=10)
# slider
geology_slider = Slider(control_frame, 'Geology weight', 0, 0, 1, 0.01)
population_slider = Slider(control_frame, 'Population weight', 0, 0, 1, 0.01)
transport_slider = Slider(control_frame, 'Transport weight', 0, 0, 1, 0.01)

download_button.grid(padx=47, pady=15)
clearAll_button.grid(padx=47, pady=12)
quit_button.grid(padx=47, pady=15)




 
#Main window loops
'''
    The mainloop is a very crucial thing for the window file.
    If there is no mainloop, it is a static window.
'''
window.mainloop() 



#For test
doctest.testmod()










