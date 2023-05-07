# 🏭 Rock Aggregates Plant Suitability Assessment

## 🌍 Background
A company producing rock aggregates was planning to build a plant in the UK. In order to gain an advantage in a competitive market and maximise profits, they needed to assess the suitability of three influencing factors for different sites: geological conditions, transport conditions and population density. Each of these three influences was provided by the company with a two-dimensional raster. The value of each raster represents the suitability of the site for that factor, with higher coefficients being more suitable for the plant. However, given the different importance of each factor, they are multiplied by their respective weights and the weighted factors are added together to give the overall suitability. I developed this project in order to make it easier for companies to adjust the factor weights and to visualise suitability.


## 📝 Description
This project is a Python-based tool. As described in the project background, this system is used to analyse site suitability to help companies select the best site for their plant. The user can calculate the results by entering two-dimensional raster data for three factors and selecting the respective weights, and generating a suitability image.  The project can be re-used for other scenarios. It can be used wherever geographic suitability assessment is involved, i.e. to analyse the impact factor weights and generate a suitability atlas. 

The main functions of this project include:
- Reading and processing impact factors (2D raster data)
- Selecting weights to measure each factor
- Calculating overall suitability
- Visualisation of suitability results

## 📁 Structure
The project mainly consists of the following files and folders:
```css
Site-suitability-analysis/
├── icon/
│   ├── stone.ico
├── input/
│   ├── geology.txt
│   ├── population.txt
│   └── transportation.txt
├── output/
│   ├── suitabilityMap.png
│   └── suitabilityMap.txt
├── src/
│   ├── assignment_2.py
├── test/
│   ├── test_download.png
│   ├── test_download.txt
│   └── test_read_data.txt
├── LICENSE
├── README.md
├── Additional notes.doc
└── requirements.txt
```
- icon: The project's GUI window icon.
- input: Store two-dimensional raster data.
- output: Store the output suitability raster data and suitability images.
- src: folder containing the Python code to implement the site suitability analysis function, where assignment_2.py is the source code file.
- test: folder containing the project run test files. This includes the project's read data test and download data test.
- LICENS: file is the open source license of the project, this project is under the MIT license.
- README.md: This file is the documentation for the project and contains an introduction to the project, instructions for use, development guides etc.
- Additional notes.doc: file is a supplement to README.md. More detailed code notes and problems encountered in writing and debugging the code are described in this file.
- requirements.txt: The file lists the Python libraries that the project depends on, such as NumPy, Matplotlib, tkinter and os. You can install these dependencies by running pip install -r requirements.txt.

## 🌟 Features
- Easy adjustment of factor weights
- Efficient calculation of the overall score for site suitability
- Visual representation of site suitability


## 🛠️ Installation
To install this project, you will first need to have Python 3.5 or higher installed on your machine. 
Then, follow these steps:

1. Clone the repository to your local machine using git clone https://github.com/perry699/Site-suitability-analysis.git.
2. Navigate to the directory where the repository is located.
3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary dependencies.
```bash
pip install -r requirements.txt
```

## 🚀 Usage
To use this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Running the GUI interface: src/ assignment_2.py
4. By clicking on Display Image, the program will automatically read the raster data file of the influence factors from the input folder and display it as an image.
5. Adjust the weighting sliders for the three factors at the control panel.
6. Click on the Calculate button and the program will automatically generate a suitability image.
7. In the output panel click on the Save & Print button to save the suitability image and raster data in the output folder, which will open automatically.
8. Clicking on the Clear button will clear all images from the interface canvas.
9. Clicking on the Quit button will end the process and close the program.


## Testing
This project uses doctest for code testing. Doctest enables quick writing and maintenance of test code, improving the quality and readability of the code. The comments section of the code provides a reliable basis for testing.
The project focused on testing the core functions of the code:

1. def read_data(file_path): This function reads the input file specified by file_path. It returns data, num_rows, and num_cols, which represent the data in the input file, the number of rows of data, and the number of columns of data, respectively. As this function requires the input file to be specified, a simple three-row, three-column sample file is written and placed in the test folder for testing purposes. Test at the function comment: 
```python
>>> read_data('./test/test_read_data.txt')
    ([[1.0, 1.0, 1.0], [4.0, 4.0, 4.0], [6.0, 6.0, 6.0]], 3, 3)
```
2. def calculate(): This function is the core part of the code. It is responsible for calculating the weighting factor and normalising the result to a range of 0-255. This function is responsible for the validity of the final result and needs to be carefully tested to ensure that the code works properly. As the function eventually returns an image, additional test code is written for this function in order not to interfere with testing. The computed part of the function is copied into the def test_calculate() function, which returns 'scaled_sum', the raster data for suitability. To test this function, first declare the example variables: 
```python
    #Preparing example variables
    geology_weight = 0.2
    population_weight = 0.2
    transport_weight = 0.6
    num_rows = 3
    num_cols = 3
    geology_data = [[1,1,1],[2,2,2],[3,3,3]]
    population_data =[[4,4,4],[5,5,5],[6,6,6]]
    transport_data = [[7,7,7],[8,8,8],[9,9,9]]
```
The example variables are ready for testing. 

```python
>>> test_calculate()
    [[0, 0, 0], [127, 127, 127], [255, 255, 255]]
```
After verification, the test results are correct and the function works fine.


## 📄 License
This project is based on the [MIT](https://choosealicense.com/licenses/mit/) license, please refer to the LICENSE file for details. You are welcome to use, modify and share it freely. If you find any problems or want to contribute code, please submit an Issue or Pull Request. Thank you very much for your participation and support!

## 💰 Credits
This project was developed independently by Pei Ziyu (Perry). The GUI interface draws inspiration from similar tools commonly used by urban planners and GIS professionals. I would like to thank these professionals for their invaluable contribution to the field of spatial analysis, which has paved the way for my work. In addition, I would like to thank the developers of the following open source libraries who played an important role in the development of this project: NumPy: Travis E. Oliphant, et al. Matplotlib: John D. Hunter, et al. Tkinter: Python Software Foundation, et al. 

## 📣 Questions and feedback
If you encounter problems using this tool, or have any suggestions or feedback, please contact the author at: Perry.yu699@gmail.com.

## 📅 Release History
- 2023/05/01 v1.0.0: Initial release with main features.















