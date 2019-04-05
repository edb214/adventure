import json

# For appending an item (string, integer, list etc.) to a json file with a list
def write_list(name, add):
    contents = read(name)
    contents.append(add)
    name=str(name)+".txt"
    file=open(name, "w")
    json.dump(contents, file)
    file.close()

# For reading a json file
def read(name):
    name=str(name)+".txt"
    file=open(name, 'r')
    contents=json.load(file)
    file.close()
    return contents

# For entirely writing over a json file with a list
def replace_list(name, add):
    name=str(name)+".txt"
    file=open(name, "w")
    json.dump(add, file)
    file.close()

# For making the first letter of every word in a string a capital letter. (e.g 'hello world' becomes 'Hello World')
def capitalize_phrase(phrase):
    phrase = phrase.split()
    for i in range(len(phrase)):
        phrase[i] = phrase[i].capitalize()
    phrase = ' '.join(phrase)
    return phrase

# For reading a text file (not json) and converting it into a list
def read_file_as_list(filename):
    filename = str(filename + '.txt')
    file = open(filename, 'r')
    contents = file.read()
    contents = contents.split()
    file.close()
    return contents

# For writing to a text file (not json) 
def write_file(filename, new_content):
    filename = str(filename + '.txt')
    file = open(filename, 'a+')
    file.write(new_content)
    file.close()
    
# Ensures there is one single space between each word (no new lines though)
def format_spaces(phrase):
    phrase = phrase.split()
    phrase = ' '.join(phrase)
    return phrase

# For doing a bubble sort in an embeded list based on a specific position e.g. scores all in pos [1]
def embedded_bubble_sort(alist, n):
    for j in range(len(alist)-1):
        for i in range(len(alist)-1):
            if alist[i][n] < alist[i+1][n]:       
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp         
    return alist