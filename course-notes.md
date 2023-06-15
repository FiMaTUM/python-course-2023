# Course Notes

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

## Notes

### Introduction

#### FiMaTUM Alumni Club

- Goal: Bring together current and former students of (Financial) Mathematics at TUM.
- Multiple advantages as a student:
  - Be the first to know about events like this course.
  - Contact to alumni and understand different career paths and ways into the industry.
  - Invitations to networking events.
- Become a member! We will soon have our yearly member assembly where you can get to know other members and the board.

#### Who are we?

We are all Python coders with a good level of experience!

- Alexander: B.Sc. Mathematics at TUM, FIM with focus on Quantitative Finance, Software Engineer at finccam
- Michel: B.Sc. Mathematics at TUM, TopMath + PhD at Chair of Mathematics
- Katharina: B.Sc. Mathematics at TUM, currently enrolled in Financial Mathematics and Actuarial Sciences at TUM
- Janos: currently finishing his B.Sc. Informatics at TUM, senior working student at finccam
- Jonas: B.Sc. Mathematics and Computer Science at TUM, currently enrolled in Mathematics in Data Science at TUM

All instructors are not paid by the club and are doing this to help you. So make the best of this great effort!

#### Python

- Python: invented in 1990s, evolved to one of the most popular languages.
- It is used in the [banking and finance sector](https://calpaterson.com/bank-python.html) and the largest bank in the US (JP Morgan) [uses it extensively](https://www.techrepublic.com/article/jpmorgans-athena-has-35-million-lines-of-python-code-and-wont-be-updated-to-python-3-in-time/).
- MAN, a large hedge fund and asset manager, uses it and recently released their data frame database [ArcticDB](https://arcticdb.io/).
- Python is also a very popular choice for machine learning. Its easy interface to C code has made it a great choice for using performance critical code written in C / C++ but without having to learn C / C++.

#### Quants

- What is a Quant?
  - Quantitative analyst: works in many contexts in the financial industry.
  - They work on:
    - Pricing and Risk (with financial models)
    - ESG (Economic Scenario Generation)
    - Trading Signal Generation / Trading Strategies
- Tasks need knowledge in:
  - Stochastic processes
  - Calibrating financial models
  - Working with large datasets
  - Utilizing ML to improve quality of predictions

Many jobs that involve datasets or mathematical modelling have a pipeline similar to this one:

- Read / Collect: Read the data from storage, collect the data from APIs or by scraping off the internet.
- Clean: Your raw data will include errors or unwanted features that need to be removed.
- Save: You will want to save your data for easier access in the future. Depending on the size of the data, this is more or less challenging.
- Process: Process the data and generate insights.
- Distribute: Distribute your data and / or your insights.

For all these steps, there are Python tools that help you do these steps.

- Read / Collect: pandas, requests, selenium, playwright, ...
- Clean: pandas, numpy, pydantic, ...
- Save: sqlite, pyodbc, csv, pyarrow, sqlalchemy, ...
- Process: TensorFlow, PyTorch, Keras, ...
- Distribute: FastAPI, flask, dash, plotly, matplotlib, seaborn, django, ...

#### Structure of the Course

What you should learn even if you have no pre-existing knowledge:

- Basics of the language (variable declaration, data types, for, if, functions, modules, debugging).
- Managing packages via pip and utilizing virtual environments.
- Using Jupyter notebooks for data analysis and exploration.
- Popular Python packages like numpy, pandas, requests, flask.

##### Thursday, 15. of June

1. Intro
2. Agenda for the 3 days
3. Start with Jupyter Notebooks
4. Basics of Python
5. Work on projects / problems

##### Friday, 16. of June

1. Repetition: list, dict, for, if, starting Jupyter
2. What are packages and modules?
3. Install and manage packages
4. Package management with virtual environments
5. Work on projects / problems

##### Saturday, 17. of June

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

### Start with Jupyter Notebooks

Start by installing Jupyter on your machine.

`pip install jupyterlab`

Then, all you should have to do is:

`python -m jupyter lab`

Then, a new browser tab should be opened automatically with Jupyter lab. If nothing happens, look at your console and see if you can find a link similar to:

`http://localhost:8888/?token=fdfa7d80b98ad162420b22db3af9ef217b7ff547f9d89adf1d`

Then, create a new Jupyter notebook. You can use this notebook similar Wolfram Mathematica. Every cell is a little bit of code or a Markdown document. Therefore, you can create long documents containing interactive code and text. Every cell can have outputs that will be displayed below the cell.

If you want to run a cell with Python code, click on the "Run" button or press `Shift + Enter`.

You can find more information about the user interface on the [JupyterLab website](https://jupyterlab.readthedocs.io/en/latest/user/interface.html).

### Basics of Python

If you are new to programming, welcome to an amazing world! If you are already familiar with other languages or even Python, be invited to follow this guide that teaches you the basics to start you on your Quant journey.

First, Python is a very expressive language. You use whitespace (tabs / spaces) to communicate to the compiler what the structure of your program is. This is different from Java or C# that use curly brackets `{}`.

Programs are put together with the help of variables that store data of different types. Logic is defined through control structures like `if` and `for`. More complex programs are structured with the help of functions and modules.

If you want to define a variable, you will need a name for your variable and some value:

```python
count = 5
```

This defines a new variable `count` that stores the value `5`. In this case, `5` is an `integer`. We can also store more complex numbers:

```python
pi = 3.1416
```

Experimental physicists would agree with me here. More importantly, `pi` is a variable that stores a `float`. `float` is the data type for floating point numbers in Python.

```python
your_instructors_name = "Alex"
```

If you forgot since my introduction, do not worry. Happy to remind you about my name - and also teach you about the `str` data type in Python that stores string data.

```python
your_tutors = ["Katharina", "Jonas", "Janos", "Stefan", "Michel"]
```

These are the names of your tutors. I put them into a `list`. Lists in python can be defined with this short syntax. You will learn more about lists later.

There is also a very similar data type to lists in Python, called `tuple`. Tuples have a few major differences to lists but the most important one is that they are immutable (you cannot change them):

```python
your_tutors_as_tuple = ("Katharina", "Jonas", "Janos", "Stefan", "Michel")
```

Finally, one of the most important data types in Python is a map or how it is better known: the `dict`.

```python
participants = {
    "newcomers": 6,
    "beginners": 26,
    "intermediate": 6,
    "advanced": 2
}
```

With the `dict` you can map keys to values.

If you want to put some logic in your programs, you will need `if` and `for` a lot.

With `if` you can split your code execution in two parts:

```python
if hour > 16:
    print("It's tea time")
else:
    print("It's not tea time")
```

`print` will write the arguments to the console or in the case of the Jupyter lab, display it in the output of the cell.

With `for` you can iterate over a list and do something with every element:

```python
for tutor in your_tutors:
    print("Hello " + tutor)
```

You can also use it to iterate over dicts:

```python
for level in participants:
    print("We have " + participants[level] + " " + level + " in the course")
```

We have used `participants[level]` to access the value for the key that is stored in the variable `level`.

To set a value in a dict, you can use `[...]`:

```python
participants["python overlord"] = 0
```

If you have a snippet of your code that you want to use multiple times, you can put this code into a function:

```python
def greet_user(name):
    print("Hello, " + name + ". Have a great day!")
```

### What are packages and modules?

One of the reasons why Python is so popular is that it has a large ecosystem of other people's code that you can use. There is a package for almost any use-case and a lot of the things that Quants usually do during their day:

- Ingest data into databases.
- Transform and filter huge datasets.
- Provide ways to run your code and generate results to others.
- Automate processes and react to external events.

Packages are a way to make code reusable and provide a way to efficiently reuse that code. Python comes with a large standard library. That is a collection of helpful functions that are grouped into packages. Instead of loading all these functions every time which would slow down your code considerably, you import only those that you need.

```python
import math
print(math.pi)
```

To make your code even more efficient, you should only import what you use.

```python
from math import sin, pi
print(sin(pi))
```

You can also use packages that are not part of the standard library such as the very popular `numpy` and `pandas`.

`numpy` has many functions that help you deal with vectors and matrices. `pandas` provides a great interface to work with tabular data.

To install any package, we use `pip`. This is the package manager that comes with Python. To install a package, you can do:

`pip install numpy`

If you want to install multiple packages:

`pip install numpy pandas`

In the case of `numpy`, we usually import everything:

```python
import numpy as np

np.array([1, 2, 3, 4]) + np.array([1, 2, 3, 4])
```

`numpy` implements component-wise addition for us. Compare that to the standard python:

```python
[1, 2, 3, 4] + [1, 2, 3, 4]
```

### Package management best practices

- Use a virtual environment to separate dependencies for your project from dependencies of your other projects.
- Useful if your projects need different versions of dependencies.
- Keep dependencies in `requirements.txt` to keep track of them and also make it easier to setup your project on other machines / simplify the deployment.
- Activate / deactivate virtual environment

### Repetition

Quick recap: list, dict, tuple, for, if, imports

### Create your own modules

We have talked about importing from packages like `import numpy as np` or `import pandas as pd`. You can then use any function that this package provides through the imported variables `np` and `pd`.

You can also create your own modules and import from them. This will help you structure your code. For this, follow these steps:

In your Jupyter notebook (`python -m jupyter lab`), create a new file `func.py` and create a single function:

```python
def print_export():
    print("Imported from your module!")
```

Then, in your notebook, you can do:

```python
from func import print_export

print_export()
```

Or, alternatively, you can import the module itself:

```python
import func

func.print_export()
```

In general, the first way of importing your module is preferred as you should only import what you actually need. If you place `.py` files in directories, you can import them by specifying the directory path in your import `from dir1.dir2.dir3 import func`.

### Packages


When you look at the examples with `numpy` and `pandas` from above, you will ask yourself the question: Why can I import something that is not in my current directory? (You have no `numpy` or `pandas`.)

That is because you can not only import from the same directory as your current python file but also from all installed packages.

A package is a collection of modules that can be made available to your Python program by installing it with `pip`.

### Package Management

`pip` helps you manage packages. You can install and deinstall packages with `pip`. We say that the packages are installed in your library.

You install packages from [PyPI](https://pypi.org/), the **Py**thon **P**ackage **I**ndex. If you have worked with other languages, it is similar to R's CRAN or Rust's crates.io.

If you work with many dependencies, it is a good idea to collect them in a file so that when other people want to work with your project, they can install the necessary dependencies with not too much work. One solution is to use a `requirements.txt` file. Every line is a package and you can install all dependencies with `pip install -r requirements.txt`.

### Virtual Environments

Another good idea is to create a separate library (i.e. set of installed packages) for every project that you work on. This way, you make sure that you only have the packages available that you need for the project and that you correctly update your `requirements.txt` if you need more dependencies.

It also has other benefits that are beyond the scope of this course.

You can create a new virtual environment with `python -m venv .env`. The most important things to remember are:

- Virtual environments make it so that you are detached from the library (i.e. set of installed packages) of your Python installation but use a clean library.
- To use a virtual environment, you need to activate it. If you use the create command from above, you can use `.env/Scripts/activate` to activate your virtual environment. Successive `pip install xxx` and also `python xxx` calls will then be made using your virtual environment. This also means that only the packages that are installed in your virtual environment are available.
- If you no longer want to use the virtual environment, you can use `deactivate`. You can also close and reopen the terminal.
- If you install or remove packages, you only install and remove them in your virtual environment. These packages are not available to your global Python.

### Introduction to numpy and pandas

When do I use which library?

- If you want to do mathematical calculations with vectors or matrices, you should use numpy. It makes it simple to work with vectors and matrices and implements efficient operations on these.
- If you want to manipulate and clean tabular or timeseries data, pandas is a great choice. It helps you filter and reshape this kind of data.

Of course, you can use both together. You can clean up your dataset in pandas and then use numpy to calculate specific metrics on specific columns.

If you want to get deeper into both, I would advise you to pick a project and work with them. There are also many great tutorials out there that can be found via Google.

#### pandas

We will use the Iris example dataset and can load this into a pandas data frame via:

```python
import pandas as pd

iris = pd.read_csv("https://raw.githubusercontent.com/practiceprobs/datasets/main/iris/iris.csv")
```

Then, we can take a look with:

```python
iris.head()
```

The first step to learning pandas is learning how to extract data from your data frame with indexing. If you want to retrieve a single column called `sepal_length`:

```python
iris["sepal_length"]
```

You can get a list of all columns via:

```python
iris.columns
```

You can also get the dimensions of the data frame with:

```python
iris.shape
```

The [pandas documentation](https://pandas.pydata.org/docs/index.html) is a very good place to start if you are looking for help. Because pandas is so popular, there is a Stack Overflow thread for every introductory question you might have.

If you want to combine two columns, you can do:

```python
iris["sepal_length"] + iris["sepal_width"]
```

You will receive a `pandas.Series` object that contains the data for the sum of the two columns.

If you want to get only the first 20 rows, you can use the row indexing:

```python
iris.loc[1:20, :]
```

You can also use this to combine row and column indexing:

```python
iris.loc[1:20, ["sepal_length", "sepal_width"]]
```

This type of indexing will always return a new data frame to you.

#### numpy

numpy is very helpful if you want to work with vectors and matrices. There are functions for many mathematical operations and you can work with vectors and matrices using the usual mathematical operations `+`, `-`, `*`, `/`.

A simple numpy vector can be created with:

```python
import numpy as np

a = np.array([6, 7, 8])
```

The variable `a` is an instance of class `numpy.ndarray`. Arrays are the equivalent of vectors. You can also have two-dimensional arrays (the equivalent of matrices):

```python
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
```

You can use numpy to calculate the sinus element-wise:

```python
np.sin(b)
```

We can also use the functions `ones` and `zeros` to create vectors and matrices with zeros and ones:

```python
np.ones((3, 3))
np.zeros((3, 3))
```

To create the identity matrix, use the `eye` function:

```python
np.eye(3)
```

If you want to learn more about numpy, you can follow along the [quickstart guide](https://numpy.org/doc/stable/user/quickstart.html) on the numpy website.

### Classes / OOP

- How to define a class
- Methods
- Inheritance
- Special methods: constructor, property, repr, abstract and class method

### FastAPI + flask

- Why FastAPI or flask? Why does a Quant need that?
- What is a server? What is a HTTP request?
- How can I send a HTTP request (GET / POST)?
- How can I setup my own API with FastAPI?
