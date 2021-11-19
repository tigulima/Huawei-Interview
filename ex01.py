from selenium import webdriver

# you can use tigulima for username and Frango!123 as a password. Don't worry, I'll change it.
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

# The class search had to be made once the home page we are accessing has no interesting data to be collected.
class Search:
    from selenium.webdriver.common.keys import Keys

# It will search the word "test" on line 28. Feel free to change that :)
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
