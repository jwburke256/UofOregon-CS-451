"""
howLongToBeat_Webscraper.py: CS 451 Final Project
Author: Jacob Burke
Credit: GeeksforGeeks
This file scrapes web content from the HowLongToBeat website;
Date Modified: 06/12/2024
"""
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import mysql.connector
from mysql.connector import errorcode
import time
import sys


def clear_table(table_name):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Clear the table using TRUNCATE
        cursor.execute(f"TRUNCATE TABLE {table_name}")

        # Commit the transaction (not necessary for TRUNCATE, but good practice)
        conn.commit()
        print(f"Table {table_name} cleared successfully.")

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


def insert_game_data(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
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


def insert_publisher_data(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Insert data
        add_data = (
            "INSERT INTO publisher (pub_name, dev_name) VALUES (%s, %s)")
        cursor.executemany(add_data, data)

        # Commit the transaction
        conn.commit()
        print(
            f"Data inserted successfully: {cursor.rowcount} rows "
            f"affected.")

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


def insert_game_times(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Insert data
        add_data = ("INSERT INTO completion_times (game_num, title, main, "
                    "main_sides, completionist) VALUES (%s, %s, %s, %s, %s)")
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


def insert_speedrun_times(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Insert data
        add_data = ("INSERT INTO speed_runs (game_num, average, median, "
                    "fastest, slowest) VALUES (%s, %s, %s, %s, %s)")
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


def insert_ign_wiki(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Insert data
        add_data = ("INSERT INTO ign_wiki (game_num, title, url) VALUES (%s, "
                    "%s, %s)")
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


def insert_pc_titles(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Insert data
        add_data = ("INSERT INTO pc_titles (game_num, current_price) VALUES ("
                    "%s, %s)")
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


def insert_console_titles(data):
    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host='localhost',  # or '127.0.0.1'
            user='root',
            password='1178',
            database='how_long_to_filter'
        )

        cursor = conn.cursor()

        # Insert data
        add_data = ("INSERT INTO console_titles (game_num, platforms, "
                    "selected_platform) VALUES (%s, %s, %s)")
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
    print("Scraping initial backlog list")
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

    # set for storing unique publisher info
    publisher_tuple_set = set()

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
except TimeoutException:
    print(f"Timed out waiting for {url}")
    sys.exit(1)


# go through each game url and grab rest of data
print("Scraping generic individual game information")
for dict in gaming_dicts:
    failed = True
    for _ in range(5):  # given 3 retries
        try:
            game_page = dict["href"]
            # pull the page
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
                if element_text.__contains__("Platform:") or \
                        element_text.__contains__("Platforms:"):
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
                elif element_text.__contains__("NA:"):
                    element_index = element_text.rfind(':')
                    na_release = element_text[element_index + 2:]
                    # need to adjust for MySQL date format
                    date_obj = datetime.strptime(na_release, '%B %d, %Y')
                    formatted_na_release = date_obj.strftime('%Y-%m-%d')
                    dict['na_release'] = formatted_na_release
            # if no publisher, developer also becomes publisher
            if 'pub_name' not in dict:
                dict['pub_name'] = dict['dev_name']

            # add tuple to publisher tuple set
            publisher_tuple_set.add((dict['pub_name'], dict['dev_name']))

            # get completion times
            page_content = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'content_75_static')))
            game_times_table = page_content.find_element(By.CLASS_NAME,
                                                         'GameStats_game_times__KHrRY')
            inner_html = game_times_table.get_attribute('innerHTML')
            driver.get("data:text/html;charset=utf-8," + inner_html)
            # Find all h5 elements within li tags
            h5_elements = driver.find_elements(By.CSS_SELECTOR, 'li h5')
            # Extract text from the h5 elements
            h5_texts = [element.text for element in h5_elements]
            # some games only have one reported time (ME: Andromeda)
            if len(h5_texts) > 1:
                dict['main'] = h5_texts[0]
                dict['main_sides'] = h5_texts[1]
                dict['completionist'] = h5_texts[2]
            else:
                dict['main'] = h5_texts[0]
                dict['main_sides'] = None
                dict['completionist'] = None

            failed = False
            break  # break out of retry loop
        except TimeoutException:
            print(f"Timed out waiting for {game_page}")
        except StaleElementReferenceException:
            time.sleep(1)
    if failed:
        raise Exception("Element could not be found after several retries")

# separate loop to get speed run times, due to not all pages having speed runs
print("Scraping speed run times")
for dict in gaming_dicts:
    failed = True
    for _ in range(5):  # given 3 retries
        try:
            game_page = dict["href"]
            # pull the page
            # get speed run times if available
            driver.get(game_page)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'table')))

            # Locate the specific table that contains the 'Any%' row
            # Using XPath to locate the table and then the row containing 'Any%'
            table = driver.find_element(By.XPATH,
                                        "//table[contains(@class, "
                                        "'GameTimeTable_game_main_table__7uN3H') and thead/tr/td[contains(text(), 'Speedruns')]]")
            speed_run_row = table.find_element(By.XPATH,
                                     ".//tr[td[contains(text(), 'Any%')]]")
            td_elements = speed_run_row.find_elements(By.TAG_NAME, 'td')

            # Extract the last four <td> elements
            last_four_tds = td_elements[-4:]
            dict['average'] = last_four_tds[0].text
            dict['median'] = last_four_tds[1].text
            dict['fastest'] = last_four_tds[2].text
            dict['slowest'] = last_four_tds[3].text
            failed = False
            break  # break out of retry loop
        except TimeoutException:
            print(f"Timed out waiting for {game_page}")
        except StaleElementReferenceException:
            time.sleep(1)
        except NoSuchElementException:
            print(f"The element containing 'Any%' was not found in {game_page}.")
            failed = False
            break  # break out of retry loop
    if failed:
        raise Exception("Element could not be found after several retries")


# separate loop to get ign walkthroughs, due to not all pages having one
print("Scraping ign wiki href's")
for dict in gaming_dicts:
    failed = True
    for _ in range(5):  # given 3 retries
        try:
            game_page = dict["href"]
            # pull the page
            # get speed run times if available
            driver.get(game_page)
            wiki_nav = driver.find_element(By.CLASS_NAME,
                                           'GameWikiNav_wiki_nav__D7ok3')
            walkthrough_link = wiki_nav.find_element(By.PARTIAL_LINK_TEXT,
                                                     'Walkthrough')
            walkthrough_href = walkthrough_link.get_attribute('href')
            dict['walkthrough_href'] = walkthrough_href
            failed = False
            break  # break out of retry loop
        except TimeoutException:
            print(f"Timed out waiting for {game_page}")
        except StaleElementReferenceException:
            time.sleep(1)
        except NoSuchElementException:
            print(f"The element containing 'Walkthrough' was not found in"
                  f" {game_page}.")
            failed = False
            break  # break out of retry loop
    if failed:
        raise Exception("Element could not be found after several retries")

# separate loop to get price info, due to only pc titles having it
print("Scraping price info")
for dict in gaming_dicts:
    if dict['platform'] != 'PC':
        continue
    failed = True
    for _ in range(5):  # given 3 retries
        try:
            game_page = dict["href"]
            # pull the page
            # get prices if available
            driver.get(game_page)
            # Wait for the page to load completely
            driver.implicitly_wait(10)
            store_button = driver.find_element(By.XPATH, "//a[contains(@class, 'StoreButton_steam__RJCCL') and contains(@class, 'StoreButton_store_botton__IrB3D') and contains(@href, 'https://store.steampowered.com/app/')]")
            price_element = store_button.find_element(By.CLASS_NAME,
                                                      'StoreButton_price__agxuh')
            # Extract the text from the located price element
            price = price_element.text
            # need to debug the multiple N/A prices
            if price == 'N/A':
                dict['current_price'] = None
                failed = False
                break  # break out of retry loop
            elif price == 'Free':
                dict['current_price'] = 0
                failed = False
                break  # break out of retry loop
            else:
                price = float(price.replace('$', ''))
                dict['current_price'] = price
                failed = False
                break  # break out of retry loop
        except TimeoutException:
            print(f"Timed out waiting for {game_page}")
        except StaleElementReferenceException:
            time.sleep(1)
        except NoSuchElementException:
            print(f"The element containing 'price' was not found in"
                  f" {game_page}.")
            dict['current_price'] = None
            failed = False
            break  # break out of retry loop
    if failed:
        raise Exception("Element could not be found after several retries")

print("Populating Tables")
# populate video_games table
data_to_insert = []
for dict in gaming_dicts:
    data_to_insert.append((dict['game_num'], dict['title'],
                           dict['na_release'], dict['dev_name'],
                           dict['pub_name']))
clear_table('video_games')
insert_game_data(data_to_insert)

# populate publisher table
data_to_insert = []
for tup in publisher_tuple_set:
    data_to_insert.append((tup[0], tup[1],))
clear_table('publisher')
insert_publisher_data(data_to_insert)

# populate completion_times table
data_to_insert = []
for dict in gaming_dicts:
    data_to_insert.append((dict['game_num'], dict['title'],
                           dict['main'], dict['main_sides'],
                           dict['completionist']))
clear_table('completion_times')
insert_game_times(data_to_insert)

# populate speed_runs table
data_to_insert = []
for dict in gaming_dicts:
    # need to check if speedrun time applies to game, skip if not
    if 'average' in dict:
        data_to_insert.append((dict['game_num'], dict['average'],
                               dict['median'], dict['fastest'],
                               dict['slowest']))
    else:
        pass
clear_table('speed_runs')
insert_speedrun_times(data_to_insert)

# populate ign_wiki table
data_to_insert = []
for dict in gaming_dicts:
    # need to check if walkthrough is available for game, skip if not
    if 'walkthrough_href' in dict:
        data_to_insert.append((dict['game_num'], dict['title'],
                               dict['walkthrough_href']))
    else:
        pass
clear_table('ign_wiki')
insert_ign_wiki(data_to_insert)

# populate console_titles & pc_titles tables
console_titles_to_insert = []
pc_titles_to_insert = []
for dict in gaming_dicts:
    # need to check if title is console or PC
    if dict['platform'] == 'PC':
        pc_titles_to_insert.append((dict['game_num'], dict['current_price']))

    else:
        console_titles_to_insert.append((dict['game_num'], dict['platforms'],
                               dict['platform']))

clear_table('pc_titles')
insert_pc_titles(pc_titles_to_insert)
clear_table('console_titles')
insert_console_titles(console_titles_to_insert)

driver.quit()
