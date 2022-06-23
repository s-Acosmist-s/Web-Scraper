from bs4 import BeautifulSoup

#command to open a file and read its content
#arguments:file name,method u want to apply when u open the file in python's memory(read,write,both)
#html_file - variable name
with open('home.html','r') as html_file:
    content = html_file.read()
    #reading the content of the html html_file
    #print(content)

    #creating instance of beutifulsoup
    #argument:content you wanna scrape,parser method
    soup = BeautifulSoup(content,'lxml')
    #prettify helps to see the code in a more pretty way
    #print(soup.prettify())

    #to grab all the html tags that are created as h5 tag
    #tags - variable
    #find - searches for the specified html tag till its first occurance
    #tags = soup.find('h5')
    #find - searches for the specified html tag for all its occurance
    #one_html_tags = soup.find_all('h5')
    #print(tags) #result is outputted in the form of a list
    #for i in one_html_tags:
        #print(i.text)#displays only the text attribute with the tags preceeding or following it
    course_cards = soup.find_all('div', class_='card')
    for i in course_cards:
        #print(i)#prints the contents of course_cards, namely the contents of the div tags having class = card
        #print(i.h5)#prints the h5 tag in each div tag having class = card
        course_name = i.h5.text
        course_price = i.a.text.split()[-1]
        #split - function to split a string into a list , default splitting parameter is a blank space
        # -1 - index of the last element of a list 
        
        #print(course_name)
        #print(course_price) 
        #usinf f string to print a dynamic sentence
        print(f'{course_name} costs {course_price}')