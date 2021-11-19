from selenium import webdriver

user = input("Enter a username: ")
pas = input("Enter a password: ")

driver = webdriver.Chrome("C:/Program Files (x86)/ChromeDriver/chromedriver.exe")
driver.get("https://pypi.org/account/login/")


class Login:
    from selenium.webdriver.common.keys import Keys

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.send_keys(user)
    password.send_keys(pas)

    password.send_keys(Keys.RETURN)


class Search:
    from selenium.webdriver.common.keys import Keys

    search = driver.find_element_by_name("q")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)


class Table:
    from bs4 import BeautifulSoup
    import requests
    import csv

    result = requests.get(driver.current_url)
    doc = BeautifulSoup(result.text, "html.parser")
    row = doc.find_all(class_="package-snippet")

    with open('results.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Version', 'Description'])

        for span in row:
            name = span.find('span', class_="package-snippet__name")
            version = span.find('span', class_="package-snippet__version")
            description = span.find('p', class_="package-snippet__description")

            writer.writerow([name.text, version.text, description.text])


driver.close()
