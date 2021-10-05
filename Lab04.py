## Python Homework 9/28/21

def name_1():
    name_1 = input("Type a name in \'first last\' order: ")
    name_1 = name_1.split()
    name_1.reverse()
    print(", ".join(name_1))

def name_2():
    name_2 = input("Type a name in \'first last\' order: ")
    name_2 = name_2.split()
    name_2.reverse()
    print(", ".join(name_2))


def name_3():
    name_3 = input("Type a name in \'first last\' order: ")
    name_3 = name_3.split()
    name_3.reverse()
    print(", ".join(name_3))
    
def nameReverse():
    num_names = int(input("How many names do you want to enter? "))
    if num_names == 1:
        name_1()
    elif num_names == 2:
        name_1()
        name_2()
    elif num_names == 3:
        name_1()
        name_2()
        name_3()

def company_1():
    company_1 = input("Type a company url with the company name starting with a capital letter: ")
    return company_1

def company_2():
    company_2 = input("Type a company url with the company name starting with a capital letter: ")
    return company_2

def company_3():
    company_3 = input("Type a company url with the company name starting with a capital letter: ")
    return company_3

def company_strip(company):
    company = company.lstrip("www.").rstrip(".com")
    print(company)


def companyName():
    num_companies = int(input("How many company urls do you want to enter? "))
    if num_companies == 1:
        company_1()
        company_strip(company_1)
    elif num_companies == 2:
        company_1()
        company_strip(company_1)
        company_2()
        company_strip(company_2)
    elif num_companies == 3:
        company_1()
        company_strip(company_1)
        company_2()
        company_strip(company_2)
        company_3()
        company_strip(company_3)



def initials():
    num_names = int(input("Enter in how many names you want: "))
    names = []
    dump = []
    initial_pool = []
    count = 0
    while count < num_names:
        name = input("Enter the name in first-last format: ")   
        names.append(name)
        count += 1
    for name in names:
        name = name.split()
        for word in name:
            initial = word[0]
            dump.append(initial) 
            if len(name) == (name.index(word)+1):
                initial_pool.append(''.join(dump))
                dump = []
    print(', '.join(initial_pool))

def wordCount():
    num_sentences = int(input("Type in the number of sentences you want: "))
    if num_sentences == 1:
        sentence_1()
        print(f'Number of words in sentence #1: {len(sentence_1.split())}')
    elif num_sentences == 2:
        sentence_1()
        print(f'Number of words in sentence #1: {len(sentence_1.split())}')
        sentence_2()
        print(f'Number of words in sentence #2: {len(sentence_2.split())}')
    elif num_sentences == 3:
        sentence_1()
        print(f'Number of words in sentence #1: {len(sentence_1.split())}')
        sentence_2()
        print(f'Number of words in sentence #2: {len(sentence_2.split())}')
        sentence_3()
        print(f'Number of words in sentence #3: {len(sentence_3.split())}')

def sentence_1():
    sentence_1 = input("Type in your sentence here: ")
    return sentence_1

def sentence_2():
    sentence_2 = input("Type in your sentence here: ")
    return sentence_2

def sentence_3():
    sentence_3 = input("Type in your sentence here: ")
    return sentence_3

def average(sentence):
    lengths = []
    sentence = sentence.split()
    for word in sentence:
        lengths.append(len(word))
        average = (sum(lengths))/len(lengths)
    print(round(average, 3))


def wordAverage():
    num_sentences = int(input("Type in the number of sentences you want: "))
    if num_sentences == 1:
        average(sentence_1())
    elif num_sentences == 2:
        average(sentence_1())
        average(sentence_2())
    elif num_sentences == 3:
        average(sentence_1())
        average(sentence_2())
        average(sentence_3())



# nameReverse()
# companyName()
# initials()
# wordCount()
# wordAverage()
