from selenium.webdriver import Firefox

nav = Firefox()

nav.get('https://br.answers.yahoo.com')

barra = nav.find_element_by_name("p")

submit = nav.find_element_by_xpath('//div[@id="searchbarContainer"]//button')

submit.click()

results = nav.find_elements_by_xpath('//div[@id="web"]/ol[2]//li')

for resultado in results: print(resultado.text)
#fazer com lxml também
