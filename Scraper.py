"""
@Author     :       William Thomas
@File       :       Scraper.py
@Email      :       wdthomas2@dmacc.edu
----------------------------------------
@Description    -   This program scrapes a website for current currency conversion rates
                    and saves it to a local txt file. If there is no internet connection, or the
                    website requested receives no response, the program will pull from the locally
                    saved file to return the most recent information

@Date Modified
5/2/2022 3:56 PM
"""
import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse
from pprint import pprint


def save_to_file(date_time, x_rates):
    # here we will take the passed values found from the scraper, and write them to the local save file.
    # new line '\n' is not necessary, but makes the txt file more readable if accessed directly
    data_to_save = str(date_time) + "\n"
    for key, value in x_rates.items():
        data_to_save += str(key) + "," + str(value) + "\n"
    # here we will open the file or create it if not present
    with open('data.txt', 'w+') as x:
        x.write(data_to_save)
    x.close()
    return data_to_save


def get_exchange_list(url="https://www.x-rates.com/table/?from=USD&amount=1"):
    # try to scrape web page to gather information about exchange rates
    try:
        content = requests.get(url).content
        soup = bs(content, "html.parser")
        # html = soup.prettify()
        # with open('html.txt', 'w+') as out:
        #     for i in range(html.__len__()):
        #         out.write(html[i])
        # out.close()
        # using dateutil, we pull the updated date from the table
        datetime = parse(soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text)
        # get the exchange rates tables
        exchange_tables = soup.find_all("table")
        # declare a dictionary of the results
        x_rates = {"US Dollar": 1.00}
        # here we will loop through the table finding the tableRow tag <tr> and then we drop into the table data <td>
        for exchange_table in exchange_tables:
            for tr in exchange_table.find_all("tr"):
                # for each row in the table
                td = tr.find_all("td")
                if td:
                    currency = td[0].text
                    # get the exchange rate
                    x_rate = float(td[1].text)
                    x_rates[currency] = x_rate
        # we want to save the file locally every time we can access the source
        save_to_file(datetime, x_rates)
    # if a connection cannot be established, the local save file is used to gather data
    except:
        lines = {}
        line_count = 0
        x_rates = {"US Dollar": 1.00}
        with open('data.txt', 'r') as d:
            lines = d.readlines()
            for line in lines:
                # first line is updated date/time value
                if line_count == 0:
                    datetime = parse(line)
                    line_count += 1
                else:
                    # split the line with the ',' delimiter, and assign first half to key, second half to value
                    key, value = line.split(",")
                    x_rates[key] = value.rstrip('\n')  # assign value stripping '\n' off
        d.close()

    return datetime, x_rates


if __name__ == "__main__":
    amount = float(1)
    datetime, x_rates = get_exchange_list('xlr')
    print("Last updated:", datetime)
    pprint(x_rates)
