from bs4 import BeautifulSoup
import re
import csv
import argparse

'''
This file reads the HTML content of the page saved in "page.html",
processes the lectures, their weeks of upload and their links (*mookit dependent*),
and finally writes them to "data.csv".
'''

#Number of latest videos to scrape.
parser = argparse.ArgumentParser()
parser.add_argument(
    "--number", type=int, default=4, help="Number of latest videos to scrape."
)
args = parser.parse_args()
n = args.number

#Reading the HTML content provided by login.py
with open("page.html", 'r', encoding='utf-8') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    lecs = soup.find_all(attrs={'class':'lectureInfoBoxText'}) #This has all the lectures uploaded as a list.
    weeks = soup.find_all(attrs={'class':'weekItem'}) #This has all the weeks as a list.
    links = soup.find_all('a', href=re.compile('#/lecture/[0-9]+')) #This has internal link of all the lectures as a list.


#Converting the Tag objects to strings
temp = []
for l in lecs:
    s = str(l)
    name = s[re.search(">[\s]*", s).end():re.search("[\s]*</div>", s).start()]
    temp.append(name)
lecs = temp

#Writing the corresponding weeks of all lecs.
temp=[]
for l in lecs:
    for w in weeks:
        lec = w.next_sibling.next_sibling
        lec = str(lec)
        if l in lec:
            s = str(w.find_all(attrs={'class':'weekWrapper'}))
            week = s[re.search(">[\s]*", s).end():re.search("[\s]*</div>", s).start()]
            temp.append(week)
            break
weeks = temp

#Writing the corresponding complete links (*mookit dependent*) of all lectures.
#I realised later that these links aren't useful for the problem statement. I am keeping them here for sake of completeness of code
temp = []
for l in links:
    s = str(l)
    tag = s[s.find("#"):s.find(">")-1]
    temp.append("https://hello.iitk.ac.in/esc201a21/"+tag)
links = temp


#Making the final .csv file.
head=["Lecture Name", "Week of upload", "Link to the lecture"]
data=[]
n = min(n, len(lecs))
for i in range(n):
    temp=[]
    temp.append(lecs[i-n])
    temp.append(weeks[i-n])
    temp.append(links[i-n])
    data.append(temp)

with open("data.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(data)