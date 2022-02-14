'''Reference no : 21005572
Developed by : Rakshitha devi.j'''
num_words =0
with open('text.txt','r') as file1:
    for i in file1:
        word =i.split()
        num_words += len(word)
print("Number of words={0}".format(num_words))