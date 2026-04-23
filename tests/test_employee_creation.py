import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver import Safari
from selenium.webdriver.chrome.options import Options
"""
with open(r"../config/execution_config.json","r" ) as f:
    execution_info = json.load(f)

browser_name = execution_info["browser"]
env_name = execution_info["env"]
env_file = open(f"../config/env_info.json","r")
env_info = json.load(env_file)
env_file.close()
env_details = env_info[env_name]
"""
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def test_sample_tc1():
    options = Options()

    options.add_argument("--headless")

    driver = webdriver.Remote(

        command_executor='http://host.docker.internal:4444/wd/hub',

        options=options

    )

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    driver.quit()

"""
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--incognito")
#options.add_argument("--headless=new")
#options.add_argument("--window-size=400,274")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors=yes")

driver = Chrome(options = options)
driver.get("https://uitestingplayground.com/")
driver.maximize_window()
driver.implicitly_wait(15)

print(driver.title)
p_elems = driver.find_elements("tag name", "p")
print(f"total p elements : {len(p_elems)}")

for elem in p_elems:
    print(elem.text)
"""





