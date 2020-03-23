import bs4
from selenium import webdriver
import re
path="C:\\Users\\me\\Downloads\\chromedriver.exe"
driver=webdriver.Chrome(path)
search = 'ngo near me'
driver.get("http://www.google.com/search?q="+search)
# print(driver.page_source)
name=[]
number=[]
soup = bs4.BeautifulSoup(driver.page_source,'html.parser')
content = soup.select('.dbg0pd')
for i in content:
    name.append(i.text)

content = soup.select('.rllt__details.lqhpac')
for i in content:
    # print(i.text)
    x = re.findall("\+?\d[\d -]{8,12}\d", i.text)
    number.append(x[0])

for (i,j) in zip(name,number):
    print(i+" : "+j)

# content = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[2]/div/div[4]/div[1]/div[1]/div/div/a[1]/div')
# print(content)
driver.close()
driver.quit()


