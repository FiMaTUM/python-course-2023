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
