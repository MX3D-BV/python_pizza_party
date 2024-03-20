# Python Pizza Session

## Start 
Disclaimer: this is meant to be fun and light, not a thurough and strict course of Python.

Verify Everybody has Python installed.

Make duos based on laptops and skill level

### Assignment:
Open a python shell and type:
```
print(hello MX3D!)
```

## Script 

Run code from a file

### Assignment:
Put the code from before in a file `hello.py` and run with `python hello.py`

## Variables
Python variables are simply containers for storing data values

```
my_int = 5
```
```
first = "Hello"
second = "MX3D!"
```
### Assignment:
Write a script that prints "Hello MX3D!" using the variables a and b


## List and iteration

Let's define a list:
```
a = [1, 2, 3, 4, 5]
```
We can use the following code to *iterate* over the list:
```
for number in a:
    print(number)
```
If the index is needed as well, we can use the `enumerate` function:
```
for index, number in enumerate(a):
    print(f"{index}:{number})
```
To loop a number of times, we can use the `range` function:
```
for index in range(100):
    print(f"{index})
```




### Assignment:
Create a list with entries M, X, 3 and D
Create a for loop that prints each entry of the list. 


### Assignment:
Print something cool to the terminal 1000 times

## Imports

Are used to import external modules and to structure your own code.
```
from otherfile import myfunction

```


## Functions
Are the building blocks of software. They are reusable blocks of code that perform a specific task.


```
def myfunction():
    print("Hello MX3D!")
```

# Challenges

## Challenge 1: Post Post Processor
Create a post_post_processor that adds a call to a custom Rapid procedure every X welds.
See the folder post_post_processor for a setup of the challenge. 


## Challenge 2: Elastic Automation
Create a script that requests the fields `created`, `state_name` and `s_duration` for robot:"mx3d_robot_9" from the elastic search server at http://10.11.12.201:9200 for all documents between 01-01-2024 and 01-02-2024 and writes those to a csv file. The index name that the documents can be found in is called mx3d-duration-state-ds. Basic auth is used, with user DV and password DashboardViewer

Hint: use chatgpt

## Demo: Save as google sheet:

Upload the csv to google drive with and convert it to a google sheet.

## Challenge 3: PixelFlut
See example.py in the PixelFlut folder for challenges. 






<!-- reusability
exercise
Modules/imports (10m)
explain
imports
pip install
pip install --user
exercise
import your function
install matplotlib
Cases
plot weld file
Testing
Where to go from here
dictionaries
classes
standard library
python in rhino/GH
web
server
scraping
numpy
excel
ipython -->


