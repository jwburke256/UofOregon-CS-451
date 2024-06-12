from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import mysql.connector
from mysql.connector import errorcode
import time
import sys


def insert_game_data(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',  # replace with your MySQL username
            password='1178',  # replace with your MySQL password
            database='how_long_to_filter'  # replace with your database name
        )

        cursor = conn.cursor()

        # Insert data
        add_data = ("INSERT INTO video_games (game_num, title, na_release, "
                    "dev_name, pub_name) VALUES (%s, %s, %s, %s, %s)")
        cursor.executemany(add_data, data)

        # Commit the transaction
        conn.commit()
        print(f"Data inserted successfully: {cursor.rowcount} rows affected.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        conn.close()


# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')
custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 " \
                    "Safari/537.36 "
options.add_argument(f'user-agent={custom_user_agent}')

url = 'https://howlongtobeat.com/user/WraithW0lf/games/backlog/1'

driver = webdriver.Chrome(options=options)

# grab titles, platform, and url's
try:
    # pull the page
    driver.get(url)

    # Wait until the table is present
    wait = WebDriverWait(driver, 10)
    backlog_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                               'in')))
    backlog_wrapper = backlog_table.find_element(By.CLASS_NAME,
                                                 'UserGameList_table_wrapper__ctpqq')
    backlog_table_dividers = backlog_wrapper.find_elements(By.CLASS_NAME,
                                                           'UserGameList_table_divider__GOZvP')
    # array of dictionaries for storing gaming info
    gaming_dicts = []

    for table_divider in backlog_table_dividers:
        tr = table_divider.find_element(By.CLASS_NAME,
                                        'UserGameList_table_row__ARuWH')

        title = tr.find_element(By.CSS_SELECTOR,
                                '.UserGameList_table_cell__1DLNr a').get_attribute(
            'title')
        platform = tr.find_element(By.CSS_SELECTOR,
                                   '.UserGameList_platform_alt__mehJr').text
        href = tr.find_element(By.CSS_SELECTOR,
                               '.UserGameList_table_cell__1DLNr a').get_attribute(
            'href')
        game_num_index = href.rfind('/')
        game_num = href[game_num_index + 1:]
        gaming_dicts.append({"game_num": game_num, "title": title, "platform":
            platform, "href": href})
        # print(title)
        # print(platform)
        # print(href)
        # inner_html = tr.get_attribute('innerHTML')
        # print(inner_html)
        # print()


except TimeoutException:
    print(f"Timed out waiting for {url}")
    sys.exit(1)
# finally:
#     # Close the browser
#     driver.quit()

# for dict in gaming_dicts:
#     print(dict["game_num"])
#     print(dict["title"])
#     print()

# go through each game url and grab rest of data

for dict in gaming_dicts:
    failed = True
    for _ in range(5):  # given 3 retries
        try:
            game_page = dict["href"]
            # pull the page
            print(dict['title'])
            driver.get(game_page)

            # Wait until the table is present
            wait = WebDriverWait(driver, 10)

            # get general game_info
            page_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                      'content_75_static')))
            game_generic_info = page_content.find_element(By.CSS_SELECTOR, "div.in.back_primary.shadow_box")
            # get platform, genre, developer, and publisher info
            game_generic_elements = game_generic_info.find_elements(By.CSS_SELECTOR,
                                                         "div.GameSummary_profile_info__HZFQu")
            for element in game_generic_elements:
                # Print the text content of each element
                element_text = element.text
                if element_text.__contains__("Platforms"):
                    element_index = element_text.rfind(':')
                    platforms = element_text[element_index + 2:]
                    dict['platforms'] = platforms
                elif element_text.__contains__("Genres"):
                    element_index = element_text.rfind(':')
                    genres = element_text[element_index + 2:]
                    dict['genres'] = genres
                elif element_text.__contains__("Developer"):
                    element_index = element_text.rfind(':')
                    developer = element_text[element_index + 2:]
                    dict['dev_name'] = developer
                elif element_text.__contains__("Publisher"):
                    element_index = element_text.rfind(':')
                    publisher = element_text[element_index + 2:]
                    dict['pub_name'] = publisher
                elif element_text.__contains__("NA"):
                    element_index = element_text.rfind(':')
                    na_release = element_text[element_index + 2:]
                    dict['na_release'] = na_release
            # if no publisher, developer also becomes publisher
            if 'pub_name' not in dict:
                dict['pub_name'] = dict['dev_name']
            failed = False
            break  # break out of retry loop
        except TimeoutException:
            print(f"Timed out waiting for {game_page}")
        except StaleElementReferenceException:
            time.sleep(1)
    if failed:
        raise Exception("Element could not be found after several retries")




        # break
        # # get completion times
        # page_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME,
        #                                                           'content_75_static')))
        # game_times_table = page_content.find_element(By.CLASS_NAME,
        #                                              'GameStats_game_times__KHrRY')
        # inner_html = game_times_table.get_attribute('innerHTML')
        # driver.get("data:text/html;charset=utf-8," + inner_html)
        # # Find all h4 and h5 elements within li tags
        # h4_elements = driver.find_elements(By.CSS_SELECTOR, 'li h4')
        # h5_elements = driver.find_elements(By.CSS_SELECTOR, 'li h5')
        #
        # # Extract text from the h4 and h5 elements
        # h4_texts = [element.text for element in h4_elements]
        # h5_texts = [element.text for element in h5_elements]
        #
        # print("h4 elements:", h4_texts)
        # print("h5 elements:", h5_texts)
        # break

    # except TimeoutException:
    #     print(f"Timed out waiting for {game_page}")

data_to_insert = []
for dict in gaming_dicts:
    print(dict['title'])
    data_to_insert.append((dict['game_num'], dict['title'],
                           dict['na_release'], dict['dev_name'],
                           dict['pub_name']))
insert_game_data(data_to_insert)
driver.quit()
