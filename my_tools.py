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