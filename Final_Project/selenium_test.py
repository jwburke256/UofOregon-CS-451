from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')
custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 " \
                    "Safari/537.36 "
options.add_argument(f'user-agent={custom_user_agent}')

url = 'https://howlongtobeat.com/user/WraithW0lf/games/backlog/1'

driver = webdriver.Chrome(options=options)

try:
    # pull the page
    driver.get(url)

    # Wait until the table is present
    wait = WebDriverWait(driver, 10)
    backlog_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                               'in')))
    backlog_wrapper = backlog_table.find_element(By.CLASS_NAME, 'UserGameList_table_wrapper__ctpqq')
    backlog_table_dividers = backlog_wrapper.find_elements(By.CLASS_NAME, 'UserGameList_table_divider__GOZvP')
    for table_divider in backlog_table_dividers:
        tr = table_divider.find_element(By.CLASS_NAME, 'UserGameList_table_row__ARuWH')
        # Locate the <a> element using XPath
        a_element = table_divider.find_element(By.XPATH,
            "//div[@class='UserGameList_table_cell__1DLNr UserGameList_short__B1zyG']/a")
        title = a_element.get_attribute('title')
        print(f"Title: {title}")
        #print(a_element.get_attribute('innerHTML'))

        inner_html = tr.get_attribute('innerHTML')
        #tcell = tr.find_element(By.CSS_SELECTOR,
        # 'UserGameList_table_cell__1DLNr UserGameList_long__P0lUQ')
        #print(inner_html)
        print()
        #print('\n')

    #print(backlog_table)
    #print(backlog_wrapper)
    #print('\n')
    #for table_divider in backlog_table_dividers:
        #print(table_divider)
    #print(driver.page_source)

except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    # Close the browser
    driver.quit()
