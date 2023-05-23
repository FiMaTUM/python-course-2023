# Virtual Environments

This article is a tutorial and a reference for the usage of virtual environments. You will learn how to create, manage, and use virtual environments and how Poetry makes this easier.

## Resources

If you want to learn more about virtual environments or you did not find the information you were looking for on this page, you can also search the following links:

- [Virtualenv tutorial on Real Python](https://realpython.com/python-virtual-environments-a-primer/)
- [Requirements files](https://pip.pypa.io/en/stable/user_guide/?highlight=requirements#requirements-files)

## Introduction to virtual environments

Virtual environments serve an important purpose in the workflow of every Python programmer. You will at some point in your Python tenure have used Python for various projects on your PC and installed various packages and their dependencies. However, you might need to install a certain version of a package for one project you are working on and another version for another package. While package A might need version 1.0.0 of package C, package B might need version 2.0.0. But you cannot install both version on your PC since Python distinguishes packages only by name and not by version.

There is also the problem that you will install many packages over the course of your Python career and this will clutter up your Python installation. At some point, you can no longer be sure which package is necessary to be installed for your project to run or which package was already installed.

In the words of Raymond Hettinger:

![There must be a better way](https://media.giphy.com/media/3scoQYue48MeZL2bBi/giphy.gif)

Virtual environments allow you to create new "Python installations" with their own collection of packages. Therefore, every project can have its own virtual environment and thereby its own dependencies.

## Using the `virtualenv` package

First, make sure you have the `virtualenv` package by installing it with `pip install virtualenv`. Then, you can create a virtual environment in your current directory by running:

```cmd
virtualenv venv
```

This will create a new directory `venv` (usually this directory will be called `venv`, `.venv`, `env`, `.env`, `virtualenv`, or `.virtualenv`) with your virtual environment inside of it.

If you type `where python` into a shell, this will give you the `python.exe` that were found in your local path. If you use `python ...` to run a python script or a module, then the first `python.exe` that was found in `where python` will be used to run this command.

To tell your system that it should use the virtual environment instead of your system Python, you need to **activate** the environment first:

```cmd
./venv/Scripts/activate
```

You will see that now the command line prompt starts with a `(venv)` and if you run `where python` the first `python.exe` that is found will be located in your new folder `venv`. This way, if you run `python`, it will use your newly created virtual environment. The same is true for the `pip` command. Every package that you install with `pip install ...` will be installed inside of your virtual environment.

---

**Warning**: Never add the files of your virtual environment to git. You should always add the virtual environment folder to your `.gitignore` file. The packages installed in the virtual environment are dependent on your individual computer (the architecture of the CPU, etc.) and somebody else will need other package files. You will learn how to keep track of dependencies down below.

---

## Command reference for virtual environments

| Command                 | Explanation                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `virtualenv venv`       | Creates a new virtual environment inside of a new folder called `venv` in your current directory.                   |
| `venv/Scripts/activate` | Activates the virtual environment located in `venv` (`python`, `pip`, etc. will point to your virtual environment). |
| `deactivate`            | Deactivates the virtual environment. Running any Python command will use the system wide Python again.              |

## Package dependencies

If you start writing your own package, you will find yourself installing and using a number of different packages (like `requests` or `numpy`). If somebody else also wants to be able to develop or use your package, he will need to install these packages first before he can use your package (since it depends on them). Therefore, there needs to be a way to reference other packages as dependencies.

We will focus in this tutorial on the use case where you want other developers to quickly be able to edit your package. This way, they need a local copy of your package's code and also the dependencies. A good way to install the dependencies would be inside of a virtual environment. The list of dependencies is then kept in a `requirements.txt` ([documentation](https://pip.pypa.io/en/stable/user_guide/?highlight=requirements#requirements-files)) file that simply lists the dependencies line by line with their version.

You can install all the packages in this file with:

```cmd
pip install -r requirements.txt
```
