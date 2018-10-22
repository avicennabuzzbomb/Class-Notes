## Table of Contents:
- [Background information](#background-information)
	- [Glossary]
- [Basic Python commands](#basic-shell-commands)
	- [Variables](#variables)
	- [Arithmetic](#arithmetic)
	- [Working with arrays](#working-with-arrays)
- [Doing Things basics](#doing-things-basics)
	- [Functions](#functions)
	- [Libraries](#libraries)
- [Visualization](#visualization)
	- [matplotlib](#matplotlib)
- [Functions by library](#functions-by-library)

	
----

## Background information

“The purpose of computing is insight, not numbers."  --Richard Hamming

- Python interpreters:
	- ``python``:
	- ``ipython``:
	- ``jupyter lab``:

### Glossary

- **array:** 
- argument:
- **element:** 
- **floating point:** 
- function: 
- **integer:** 
- **library:**
- **members:** AKA attributes. Metadata about a variable. For example, the NumPy array 
   ``data`` has members including ``data.dtype``, ``data.shape``
- **string:** 
- **shape:** (of an array) dimensions.
- **variable:**


----

## Basic Python commands

- ``#``: Everything in a line after the octothorpe is a comment.
- ``command?``: get help on ``command``
	- ``help(command)``: get help on ``command``

### Variables
"A variable is analogous to a sticky note with a name written on it."  (Software Carpentry)

- ``%whos``: display a table of all variables currently set.
- ``weight_kg = 60``: set ``weight_kg`` to 60. No need to declare a variable ahead of time.
	- Varnames can:
		- include alphanumerics & underscores
	- Varnames CANNOT:
		- include dots
		- start with a digit
	- Varnames are case sensitive.
- 3 **basic** data types: integers (``int``), floating point numbers (``float``), & strings 
   (``str``).
	- ``varname 60``: ``varname`` is an int, value 60 .
	- ``varname 60.0``: ``varname`` is a float, value 60.0 .
	- ``weight_in_kilos "sixty"``: ``weight_in_kilos`` is a string, value "sixty".
- ``print(weight_kg)``: displays the value of ``weight_kg``.
	- ``print(weight_kg, weight_in_kilos)``: displays the value of ``weight_kg`` and then 
	   of ``weight_in_kilos``, with no separator.
	- ``print("weight in pounds: ", weight_kg * 2.2)``: You can do math and specify values
	   within a ``print()`` command.
- ``type(weight)``: returns the data type for ``weight``. For arrays, will only return the 
   array itself, not its elements.

### Arithmetic

- Basic arithmetic operations are very simple: `` 3 + 5 * 4`` returns ``20``.
- Some array operations with ``numpy``:
	- ``numpy.mean(data, axis=0)``: returns a vector of the averages of each row in ``data``
	- ``numpy.mean(data, axis=1)``: returns a vector of the averages of each column in ``data``

### Working with arrays

- ``data[0, 0]``: first (top-left) value in an array. (Python is zero-indexed because it's
   part of the C family, like C++ and Perl.)
	- The first value is the row (Y-coord), the second value is the column (X-coord). They
	   work like matrices, not Cartesian coordinates.
	- ``data[0:4, 1:10]``: rows 0-3 (the 1st-3rd) of columns 1-9 (the 2nd-10th). Note that
	   this is *up to, but not including* row 4 and column 10.
	- ``data[:3, 10:]``: rows up to 3 (i.e. 0-2) of all columns after 10
	- ``data[0:3, :]``: rows up to 3 (i.e. 0-2) of all columns
- Arrays have attributes:
	- ``data.shape``: the dimensions of the array ``data`` (rows, cols)
	- ``data.dtype``: the data type of elements in ``data``
- 

---

## Doing Things basics

### Functions

- Not all functions take input (arguments).
- ``%``: denotes a IPython magic function, which is only valid within the notebook
   environment

### Libraries

- ``import numpy``: accesses the library ``numpy`` (NumPy) and loads it up for use. 
   "Importing a library is like getting a piece of lab equipment out of a storage locker 
   and setting it up on the bench." (Software Carpentry)
	- ``import matplotlib.pyplot``: imports the ``pyplot`` module from the ``matplotlib``
	   library
- ``numpy.mean()``: the function ``mean()`` drawn from library ``numpy``.
- ``numpy. \t``: In IPython and Jupyter Notebook, you can use tab completion to get a
   list of all functions in a library or attributes in an object.
- 


----

## Visualization

### matplotlib.pyplot



----

## Functions by library

- ``matplotlib``
	- 
- ``numpy``
	- ``numpy.max()``: 
		- ``numpy.max(data[2, :]))``
		- ``patient_0.max()``
- ``time``
	- ``time.ctime()``: current date & time
	
	
	
