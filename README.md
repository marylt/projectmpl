# Project MATPLOTLIB
*Final INST326 Project using video game sales data and the Python library matplotlib.*

Define a goal for the project -- what is the purpose of the tool you are creating?
- A goal for this project is to visualize possible relationships between entities in the video game sales dataset, using matplotlib.

Define the scope for the project -- what are you trying to accomplish, and what is out of scope?
- The scope of this project is to successfully learn and utilize matplotlib in Python. An objective is to identify and plot at least one relationship between two entities in the dataset. Examples of things not in our scope include creating our own plotting libraries, creating queries with sqlite3, and using regional expressions.

## Getting Started
The python library matplotlib is required for this repository. For more information on matplotlib, visit: https://matplotlib.org/.

The dataset for Video Game Sales in CSV file (https://www.kaggle.com/gregorut/videogamesales/data#) will be used.
- Also available as a .csv file in the 'files' section of this repository.

### Defining each .py file:
- __Genre and Country.py__: This code will first read the data of the video game sales .csv file into a data frame using pandas. Then, the data will be sorted by (Country_Sales) and (Genre), descending. This will show the top genres sold in each country. This is done for Japan, North America, and Europe. The matplotlib.pyplot (shortened as plt) function is used to create a scatter plot for each country.
  - Scatter plots created (JP, NA, EU), click for full image(s):
![Imgur](https://imgur.com/otbcxEv.png)
![Imgur](https://imgur.com/nhFFL9C.png)
![Imgur](https://imgur.com/rWi360e.png)
