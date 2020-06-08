# passw0rd-generator

Use this program to generate a list of passwords of desired length. You also have the option to store the passwords in a
``.csv`` file. (**Warning**: This feature is for educational purpose only. Do not use passwords which are stored on your machine in unprotected form. Use a password manager or memorize them).
The program uses the Python ```random.choice()``` function to pick from the range of the unicode characters except ```\\```:

```python
all_chars = [chr(i) for i in range(33, 127)]
all_chars.remove("\\")
```

## Usage

Use this program in two ways:

1. The ```password_generator.ipynb``` file. Just execute the first and only cell and follow the prompted questions. It is self-explanatory.

2. The script ```passw0rd-generator.py```.

In both cases, if you opt to save as ```.csv```, you will find the ```.csv``` in the same folder in which the program is executed named ```your_password_list.csv```.

Allowed values for the input variables are:

* **number of characters**: A positive Integer value.
* **number of passwords**: A positive Integer value.
* **choice to save**: The keys 'Y', 'y', 'N' or 'n'.

### The script
#### Without keyword arguments

Type the following command


```console
foo@bar:~$ python3 passw0rd-generator.py
```
and answer the following questions of how much characters you want your passwords to have, how many and if you want them to save to ```.csv```.

#### With keyword arguments

Use the above commad with the following keyword arguments:

* ```-h```, to display correct usage.
* ```-c```, ```--charsize```, length of every password. Mandatory. Provide at least 1.
* ```-n```, ```--numberofpwds```, number of passwords to be generated. Optional, defaults to 1.
* ```-s```, ```--savetocsv```, save as ```.csv```. Allowed values are 'Y', 'y', 'N', 'y'. Optional, defaults to 'n'.

### Example

The command
```console
foo@bar:~$ python3 passw0rd-generator.py -c 5 -n 10 -s y
```
would print out 10 passwords with 5 randomly generated characters each to the console and save them as ```.csv``` to the folder the script is executed in.
