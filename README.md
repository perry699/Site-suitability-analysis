# Site Suitability Assessment System
The project was used for site suitability analysis.


## Project Background
A company producing rock aggregates was planning to build a plant in the UK. In order to gain an advantage in a competitive market and maximise profits, they needed to assess the suitability of three influencing factors for different sites: geological conditions, transport conditions and population density. Each of these three influences was provided by the company with a two-dimensional raster. The value of each raster represents the suitability of the site for that factor, with higher coefficients being more suitable for the plant. However, given the different importance of each factor, they are multiplied by their respective weights and the weighted factors are added together to give the overall suitability. I developed this project in order to make it easier for companies to adjust the factor weights and to visualise suitability.


## Project description
This project is a Python-based tool. As described in the project background, this system is used to analyse site suitability to help companies select the best site for their plant. The user can calculate the results by entering two-dimensional raster data for three factors and selecting the respective weights, and generating a suitability image.  The project can be re-used for other scenarios. It can be used wherever geographic suitability assessment is involved, i.e. to analyse the impact factor weights and generate a suitability atlas. 

The main functions of this project include:
- Reading and processing impact factors (2D raster data)
- Selecting weights to measure each factor
- Calculating overall suitability
- Visualisation of suitability results


## Features

- Easy adjustment of factor weights
- Visual representation of site suitability
- Efficient calculation of overall suitability score


## Installation
To install this project, you will first need to have Python 3.5 or higher installed on your machine. Then, follow these steps:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

## Usage

## License
This project is based on the [MIT](https://choosealicense.com/licenses/mit/) license, please refer to the LICENSE file for details. You are welcome to use, modify and share it freely. If you find any problems or want to contribute code, please submit an Issue or Pull Request. Thank you very much for your participation and support!
