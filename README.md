# Word-count
## AIM:
To write a python program for getting the word count from a text.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
```
## Step 1:
Create a txt file to count the number of word in that file.

## Step 2:
Open the txt file in read mode using open().

## Step 3:
Using split() function to split the words in the txt file and count it.

## Step 4:
Save the python program using .py extention.

## Step 5:
Run the python program in terminal to get the output.

## Step 6:
Number of words in the txt file is displayed as the output.
```
## PROGRAM:
```
'''Reference no : 21005572
Developed by : Rakshitha devi.J'''
num_words =0
with open('name.txt','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={0}".format(num_words))
```
### OUTPUT:
## word.py:
![image](https://user-images.githubusercontent.com/94165326/153898944-71fb2775-122c-495f-9ea3-eb7b33d116b8.png)


## Terminal and text.txt:
![image](https://user-images.githubusercontent.com/94165326/153899054-32e4fd1b-7812-4fff-9329-b8bf1607a9ae.png)




## RESULT:
Thus the program is written to find the word count from a text.
