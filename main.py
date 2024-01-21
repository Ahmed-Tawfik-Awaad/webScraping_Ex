import csv
from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
names = []
Company = []
Location = []
Jop_type = []
Skilles = []
Links = []
page_num = 0
while True:
    url = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python&start={page_num}")
    soup = BeautifulSoup(url.content, "lxml")
    page_limit = int(soup.find("strong").text)
    if page_num > page_limit // 15:
        print("page end")
        break

    jop_name = soup.find_all("h2", {"class": "css-m604qf"})
    company_name = soup.find_all("a", {"class", "css-17s97q8"})
    location = soup.find_all("span", {"class": "css-5wys0k"})
    jop_type = soup.find_all("span", {"class": "css-1ve4b75 eoyjyou0"})
    skill = soup.find_all("div", {"class": "css-y4udm8"})


    for i in range(len(jop_name)):
        names.append(jop_name[i].text)
        Links.append(jop_name[i].find("a").attrs["href"])
        Company.append(company_name[i].text)
        Location.append((location[i]).text)
        Jop_type.append(jop_type[i].text)
        Skilles.append(skill[i].text)
    page_num += 1
    print("page switched")



file_list = [names, Company, Location, Jop_type, Skilles, Links]

exported = zip_longest(*file_list)

with open("/Users/ahmed/OneDrive/Desktop/test.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Jop Titles", "Company", "Location", "Jop Type", "Skills", "Links"])
    wr.writerows(exported)
