# Calci (First Version of the Docs)
The newest mini calculator you'll find. 
[Example of https://diataxis.fr/ in action]
## Why use this calculator and not any other?
Because it's easy to use and only contains 11 lines of code,
which makes is super robust.

## Tutorial
We got a short Calci at a Glance section and a longer
"Calci get your hands dirty" section.

### Calci at a Glance
Calci is a basic calculator. It takes two numbers, an operator
and provides you with the result, like:

```bash
python Calci/main.py 1 "+" 2
>> 3
```


### Get Started
To get started clone the repository & install the Python dependencies.
Clone this repository
```bash 
git clone git@github.com:sbalnojan/Calci.git
```
or 
```bash 
git clone https://github.com/sbalnojan/Calci.git
```
and then install the dependencies via 
```bash 
pip install -r requirements.txt
```

. Now run a test command to see whether it worked

```bash
$ python Calci/main.py
ERROR: The function received no value for the required argument: number1
Usage: main.py NUMBER1 OPERATOR NUMBER2

For detailed information on this command, run:
  main.py --help
(venv)
```
Perfect, it worked! 

### Calci Step 1, doing simple calculus
Let us calculate 2 times 4+1
First, calculate 2 times 4 via

```bash 
python Calci/main.py 2 "*" 4
```
In the Output you get the result

```bash 
8
```
. Now continue with thes rest of the calculation 8 + 1
```bash 
python Calci/main.py 8 "+" 1
>> 9
```

Great! You calculated your first expression using Calci.