import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.catalog.gatech.edu/courses-grad/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

school = soup.find(id='atozindex')

school_list = school.find_all('a', href=True)

school_code = []
for a in school_list:
    school_code.append(a['href'].split('/')[2])

school_urls = []
for school in school_code:
    school_urls.append("http://www.catalog.gatech.edu/courses-grad/" + school + "/")
    
data = []
for page in school_urls:
    page = requests.get(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    course_list = soup.find(class_='tab_content')
    course_list_codes = soup.find_all('strong')

    
    
    for course_list in course_list_codes:
        codes = course_list.contents[0]
        data.append((codes))
        

    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        for codes in data:
          writer.writerow([codes])


#ENV
for codes in data:
    sub = 'Env'
    if sub in codes:
        print(codes)
        with open('Env.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([codes])
        
#Sustent       
for codes in data:
    sub = 'Sust'
    if sub in codes:
        print(codes)
        with open('Sust.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([codes])
            
#Climate
for codes in data:
    sub = 'Climate'
    if sub in codes:
        print(codes)
        with open('Climate.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([codes])            
            

#Energy
for codes in data:
    sub = 'Energy'
    if sub in codes:
        print(codes)
        with open('Energy.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([codes])
            
            
            
url = "https://www.huffingtonpost.com/entry/massive-sea-star-die-off-linked-to-global-warming_us_5c553a6de4b00187b55120ad"
page = requests.get(url, headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
soup = BeautifulSoup(page.text, 'html.parser')

content = soup.find_all("div", class_="entry__text js-entry-text yr-entry-text")

paragraphs = [p.find_all('p') for p in content][0]

ref = []
for paragraph in paragraphs:
    links = paragraph.find_all('a', href=True)
    if len(links) > 0:
        ref.append(links[0])

clean_ref = []
for tagged_reference in ref:
    clean_ref.append(tagged_reference['href'])
    
file = open('ref_pjasti3.csv', 'w+', newline ='')
with file:     
    for line in clean_ref:
        file.write(line + "\n")



url = "https://www.huffpost.com/"
page = requests.get(url, headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find("section", class_="zone zone--zoneA zone--layout-layout3 zone--theme-default zone--has-title")
links = content.find_all('a', class_="card__headline card__headline--long")
links = [link['href'] for link in links]

for link in links:
    headline_page = requests.get(link, headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    new_soup = BeautifulSoup(headline_page.text, 'html.parser')
    content = new_soup.find_all("div", class_="entry__text js-entry-text yr-entry-text")
    paragraphs = [p.find_all('p') for p in content][0]
    ref = []
    for paragraph in paragraphs:
        links = paragraph.find_all('a', href=True)
        if len(links) > 0:
            ref.append(links[0])
            clean_ref = []
    for tagged_reference in ref:
        clean_ref.append(tagged_reference['href'])
    print(clean_ref)
