## Python Homework 9/28/21
## Ishai Masada
## Lab 04/05

def name_reverse(name):
    name = name.split()
    name.reverse()
    print(", ".join(name))
    
def nameReverse():
    num_names = int(input("Type in the number of names you want to be reversed: "))
    print(f'num names: {num_names}')
    count = 0
    if num_names == 1:
        while count < 1:
            name = input("Type in the name in first-last order: ")
            name_reverse(name)
            count+=1
    elif num_names == 2:
        while count < 2:
            name = input("Type in the name in first-last order: ")
            name_reverse(name)
            count+=1
    elif num_names == 3:
        while count < 3:
            name = input("Type in the name in first-last order: ")
            name_reverse(name)
            count+=1

def company_strip(company):
    company = company.lstrip("www.").rstrip(".com")
    print(company)

def companyName():
    num_company = int(input("How many company urls do you want to enter? "))
    count = 0
    if num_company == 1:
        while count < 1:
            company = input("Type in the name of the company website: ")
            company_strip(company)
            count+=1
    elif num_company == 2:
        while count < 2:
            company = input("Type in the name of the company website: ")
            company_strip(company)
            count+=1
    elif num_company == 3:
        while count < 3:
            company = input("Type in the name of the company website: ")
            company_strip(company)
            count+=1


def initial(first_name, last_name):
    initials = []
    for letter in first_name:
        initials.append(letter)
        break
    for letter in last_name:
        initials.append(letter)
        break
    return initials

def find_initials():
    num_names = int(input("Enter in how many names you want: "))
    count = 0
    if num_names == 1:
        while count < 1:
            first_name = input("Type in the first name of the student: ")
            last_name = input("Type in the last name of the student: ")
            initials = initial(first_name, last_name)
            print(''.join(initials))
            count+=1
    elif num_names == 2:
        while count < 2:
            first_name = input("Type in the first name of the student: ")
            last_name = input("Type in the last name of the student: ")
            initials = initial(first_name, last_name)
            print(''.join(initials))
            count+=1
    elif num_names == 3:
        while count < 3:
            first_name = input("Type in the first name of the student: ")
            last_name = input("Type in the last name of the student: ")
            initials = initial(first_name, last_name)
            print(''.join(initials))
            count+=1

def wordCount():
    num_sentences = int(input("Type in the number of sentences you want: "))
    count = 0
    if num_sentences == 1:
        while count < 1:
            sentence = input("Type in your sentence here: ")
            print(f'Number of words in the sentence: {len(sentence.split())}')
            count+=1
    elif num_sentences == 2:
        while count < 2:
            sentence = input("Type in your sentence here: ")
            print(f'Number of words in the sentence: {len(sentence.split())}')
            count+=1
    elif num_sentences == 3:
        while count < 3:
            sentence = input("Type in your sentence here: ")
            print(f'Number of words in the sentence: {len(sentence.split())}')
            count+=1

def average(sentence):
    lengths = []
    sentence = sentence.split()
    for word in sentence:
        lengths.append(len(word))
        average = (sum(lengths))/len(lengths)
    print(round(average, 3))


def wordAverage():
    num_sentences = int(input("Type in the number of sentences you want: "))
    count = 0
    if num_sentences == 1:
        while count < 1:
            sentence = input("Type in your sentence here: ")
            average(sentence)
            count+=1
    elif num_sentences == 2:
        while count < 2:
            sentence = input("Type in your sentence here: ")
            average(sentence)
            count+=1
    elif num_sentences == 3:
        while count < 3:
            sentence = input("Type in your sentence here: ")
            average(sentence)
            count+=1



# nameReverse()
# companyName()
# find_initials()
# wordCount()
# wordAverage()
