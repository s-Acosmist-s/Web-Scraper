from bs4 import BeautifulSoup
import requests 
import time

#using get method of requests library to get specific info. from a website
#requests library basically requests information from a specific website
#arguments : url to be scraped,
#html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
#print(html_text)#checks the request status
#OUTPUT : <Response [200]> ; this is the convention no. in web that the request is done successfully

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    #to avoid the status code and bring the html code of the specific page
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text,'lxml')
    #jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    #since pagination is there in the website, this is going to bring the result of the first page only
    #print(jobs)
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    #to search for a tag inside the 'job' element 
    # replace function is used to remove the unnecessary white spaces in the output
    #index - counter variable for the job i am interating on, job - refers to beautifulsoup job object itself
    for index, job in enumerate(jobs):
        publish_date = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in publish_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_= 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                #print(publish_date)
                #print(copmany_name)
                #print(skills)
                # ''' (triple quote) method is used to print the text in multipe lines
                #print(f'''
                #Company Name: {company_name}
                #Required Skills: {skills}
                #''')
                #to get rid of the leading and trailing blank spaces by using the strip method which is used with strings
                with open(f'posts/{index}.txt','w') as fl:
                    #writing to the file with the fl variable
                    fl.write(f"Company Nmae : {company_name.strip()} \n")
                    fl.write(f"Required skills: {skills.strip()} \n")
                    fl.write(f"More Info: {more_info} \n")
                    #print('')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait * 60)#allows ur program to wait for a certain amount of time before executing again; its argument is provided in the form of seconds