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

## Testing
You can run some tests for loading .csv data into lists x and y in the test.py module using [pytest]:
```
pytest test.py
```

### Installation
Besides needing the latest version of Python installed, you will also need to install the matplotlib Python library. This can be accomplished by running the following code in the terminal you are using:
```
pip install matplotlib
```

#### Defining each .py file:
- __Genre and Country.py__: This code will first read the data of the video game sales .csv file into a data frame using pandas. Then, the data will be sorted by (Country_Sales) and (Genre), descending. This will show the top genres sold in each country. This is done for Japan, North America, and Europe. The matplotlib.pyplot (shortened as plt) function is used to create a scatter plot for each country.
  - Scatter plots created (JP, NA, EU), click for full image(s):
![Imgur](https://imgur.com/otbcxEv.png)
       - The top three genres in Japan are Role-Playing, Platform, and Simulation.
![Imgur](https://imgur.com/nhFFL9C.png)
       - The top three genres in North America are Sports, Platform, and Shooting.
![Imgur](https://imgur.com/rWi360e.png)
       - The top three genres in Europe are Sports, Racing, and Simulation.

- __Publisher and Global Sales.py__: This code will first read the data of the video game sales .csv file into a handle named 'data.' A for loop created for that sorted data will append the first 5 most popular game publishers in global sales. This will show the top publishers sold in global sales. The matplotlib.pyplot (shortened as plt) function is used to create a bar plot that shows the global top 5 game publishers.
  - Bar plot created, click for full image(s):
  ![Imgur](https://imgur.com/M6kpjm7.png)
       - The top five global gaming publishers are Nintendo, Activision, Sony Computer Entertainment, Take-Two Interactive, and Microsoft Game Studios.

- __Game and Global Sales.py__: This code will first read the data of the video game sales .csv file into a handle named 'data.' A for loop created for that sorted data will append the first 5 most popular games in global sales. This will show the top games sold in global sales. The matplotlib.pyplot (shortened as plt) function is used to create a bar plot that shows the global top 5 games.
  - Bar plot created, click for full image(s):
  ![Imgur](https://imgur.com/ny8Q0tS.png)
       - The top five selling games globally are Pokemon Red/Pokemon Blue (topping at 82.74 million sales), Wii Sports Resort, Mario Kart Wii Game, Super Mario Bros, and Wii Sports (starting directly at 31.37 million sales, not 0).

- __Platform and Global Sales.py__: This code will first read the data of the video game sales .csv file into a dataframe named 'df.' A variable named 'sum' is made of a .groupby dataframe, consisting of (Platform) and (Global_Sales). The sum of (Global_Sales) is taken. The matplotlib.pyplot (shortened as plt) function is used to create a pie chart that shows the percentages that each platform has in terms of (Global_Sales) for the first 90 games.
  - Pie chart created, click for full image(s):
  ![Imgur](https://imgur.com/qyOt3m3.png)
       - The top five platforms in Global_Sales for the first 90 games are Wii (23.3%), DS (14.9%), XBOX360 (12.6%), GB(9.3%) and PS3 (8.0%).
       
- __Game and NA Sales.py__ : This code will first read the data of the video game sales .csv file into a .reader named data. Then, a counter is established to stop the for loop from appending more than 10 games to the x and y lists. The pyplot function from matplotlib (plt) will be used to create a lollipop plot. This will show the top 10 games sold in North America.
  - Lollipop chart created, click for full image(s):
  ![Imgur](https://imgur.com/TiLMJuD.png)
       - The top five games sold in North America are Wii Sports, Super Mario Bros., Wii Duck Hunt, Tetris, and Mario Kart Wii.
