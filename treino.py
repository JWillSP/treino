import time
from lxml import etree
from selenium.webdriver import Firefox

nav = Firefox()

nav.get('https://br.answers.yahoo.com')

barra = nav.find_element_by_name("p")

barra.send_keys('Python')

submit = nav.find_element_by_xpath('//div[@id="searchbarContainer"]//button')

submit.click()

time.sleep(3)

results = nav.find_elements_by_xpath('//div[@id="web"]/ol[2]//li')

tree = etree.HTML(nav.page_source)

results2 = tree.xpath('//div[@id="web"]/ol[2]//li')

for resultado in results: print(resultado.text)

for r in results2:
    for texto in r.itertext():
        print(texto)

nav.close()
