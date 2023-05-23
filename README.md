# Introduction to Python for Quants

Since Python was invented in the early 1990s it has evolved to one of the most popular and wide used languages. It is used in the [banking and finance sector](https://calpaterson.com/bank-python.html) and the largest bank in the US (JP Morgan) [uses it extensively](https://www.techrepublic.com/article/jpmorgans-athena-has-35-million-lines-of-python-code-and-wont-be-updated-to-python-3-in-time/). MAN, a large hedge fund and asset manager, uses it and recently released their data frame database [ArcticDB](https://arcticdb.io/).

Python is also a very popular choice for machine learning. Its easy interface to C code has made it a great choice for using performance critical code written in C / C++ but without having to learn C / C++.

Quantitative analysts (or quants) work in many contexts in the financial industry. Their work involves the following main areas:

- Pricing and Risk (with financial models)
- ESG (Economic Scenario Generation)
- Trading Signal Generation / Trading Strategies

All these tasks involve a lot of knowledge of stochastic processes, calibrating financial models, and working with large datasets. Today, this also means utilizing machine learning to improve the quality of predictions.

This course will teach you the basics of Python with a focus on the basic knowledge of a quant. It is designed as a three day course and can be adapted to students with varying pre-existing knowledge in Python.

Each day is structured into one part where the instructor will give a brief presentation about a particular aspect of python and a larger part where the students can work on projects of their choice.

Learning to program in a new language is like learning a new theory in maths. While it helps if someone points you in the right direction, you will ultimately need to get your hands dirty and apply your knowledge to problems.

To make the course suitable to students with various pre-existing knowledge in Python, we provide projects with different levels of difficulty or scope.

We will focus on teaching you about the following aspects of Python:

- Basics of the language (variable declaration, data types, for, if, functions, modules, debugging).
- Managing packages via pip and utilizing virtual environments.
- Using Jupyter notebooks for data analysis and exploration.
- Popular Python packages like numpy, pandas, requests, flask.

## Agenda

### Day 1

1. Intro
2. Agenda for the 3 days
3. Start with Jupyter Notebooks
4. Basics of Python
5. Work on projects / problems

### Day 2

1. Repetition: list, dict, for, if, starting Jupyter
2. What are packages and modules?
3. Install and manage packages
4. Package management with virtual environments
5. Work on projects / problems

### Day 3

1. Classes / OOP
2. Work on projects / problems
3. Lunch
4. FastAPI + flask
5. Advanced topics (when there is interest for them)
   1. Context Managers
   2. Web Servers in detail (flask)
   3. Advanced dicts
   4. Dunder methods
6. Work on projects / problems

## Projects

Here are some projects with different levels of difficulty / scope. Some of the beginner projects have more explanations and detailed steps. This is because beginners need to learn the language while also thinking about the details of the project.

For the intermediate, advanced, and expert level projects we provide only a scaffold. We tell you the general direction you should go and leave the rest up to you. This is for several reasons:

- Preparing detailed tutorials is hard and costs a lot of time. There are also many brilliant tutorials available on almost all of the subjects and packages we touch on.
- Use the tutors if you have problems or if you need inspiration with the projects. They can help you if you feel lost or if you are unable to proceed.
- We want you to explore the language and the tools that we talk about here. You should learn the following things:
  - How can I achieve what I want to do with Python?
  - How do I have to phrase my questions so that I find what I am looking for on Google? (One of **the most important skills** in programming.)
  - If I have never or rarely ever used a certain package / tool, how do I find out more about it and where do I have to look for guidance and help?

### Beginner

#### Guess the number game

In [this tutorial](https://www.youtube.com/watch?v=ZsRMQHbx6Xc) you will learn the basics of Python (for, if, functions) by implementing a simple game.

#### QR Code

In [this tutorial](https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s) you will learn how to create your own QR codes and also how to decode them into URLs.

#### Live weather desktop notifications

In [this tutorial](https://www.geeksforgeeks.org/get-live-weather-desktop-notifications-using-python/) you will learn how to scrape data off a website and how to display notifications on Windows. (Only works on Windows!)

#### Stock analysis

Download the [US stock market dataset](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data) from Kaggle first. Then, use numpy and pandas to analyse returns over multiple periods (1Y, 3Y, 5Y). The next step is to use matplotlib to plot the following diagrams for the stocks:

- Plot the price of the stock historically (i.e. x-axis = time, y-axis = price).
- Calculate the returns of every stock. Then use [matplotlib](https://matplotlib.org/) to plot different diagrams to analyse the distribution of the returns historically (kernel density, histogram, box plot).

#### Intermediate

#### Webscraping & Data API

This project guides you through the steps whenever you want to scrape some data off a website and make it accessible to yourself / others through an API.

1. Scrape data from website using [requests](https://requests.readthedocs.io/en/latest/).
2. Clean this data using pandas (+ numpy).
3. Put this data into a csv.
4. Make this data accessible through an API (using flask or FastAPI). Whenever someone queries your API, load the data from the CSV and extract the queried data.

Possible data sources:

- Download data for multiple stocks from [Yahoo Finance](https://de.finance.yahoo.com/quote/BMW.DE/history?p=BMW.DE).
- Use VIX and other data from the [CBOE](https://www.cboe.com/tradable_products/vix/vix_historical_data/).
- Use economic indicators (inflation, FED funds rate, GDP growth, ...) from [FRED database](https://fred.stlouisfed.org/).

### Advanced

#### Advanced Webscraping & Data API

This project guides you through the steps from the beginner webscraping project but uses much more advanced tools and packages.

1. Scrape data from website (using [selenium](https://selenium-python.readthedocs.io/) or [playwright](https://playwright.dev/python/docs/intro)).
2. Clean the data using pandas (+ numpy).
3. Put this data into an [sqlite](https://docs.python.org/3/library/sqlite3.html) database.
4. Create an API using [FastAPI](https://fastapi.tiangolo.com/) to query your data.
5. Create Plotly graphs using [Plotly express](https://plotly.com/python/plotly-express/). Take a look at the examples in the "Gallery" section.

Possible data sources:

- Use the [problem notifications from the S-Bahn München twitter account](https://github.com/kummerer94/sbahn-stoerungen/blob/master/stoerungen.xlsx) to analyse the problems the S-Bahn has had over the years. You will have to clean and filter this data first.
- Download data for multiple stocks from [Yahoo Finance](https://de.finance.yahoo.com/quote/BMW.DE/history?p=BMW.DE). You could download data for multiple stocks, put this into your database, and then build an API around it.
- Use VIX and other data from the [CBOE](https://www.cboe.com/tradable_products/vix/vix_historical_data/). You will probably not have to do too much cleaning here but you could put this data into your database and build an API around it.
- Use economic indicators (inflation, FED funds rate, GDP growth, ...) from [FRED database](https://fred.stlouisfed.org/). You could ingest this data into your database and then use it to regress against the major stock indices (S&P 500, EuroStoxx 50, MSCI World) to see if the economic indicators have any predictive qualities.
- Download some weather data from [Open-Meteo](https://open-meteo.com/) and compare the weather at different locations in the world. You could also use the historical data they have available to ingest this data historically.

### Expert

#### Dashboard

1. Scrape data from website (see advanced webscraping project for possible data sources).
2. Look at the tutorial for [Plotly Dash](https://dash.plotly.com/tutorial).
3. Design and implement a dashboard for your data. Use any database you like (sqlite or simple csv file) in the background to store your data.
