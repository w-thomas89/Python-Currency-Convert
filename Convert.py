"""
@Author     :       William Thomas
@File       :       Convert.py
@Email      :       wdthomas2@dmacc.edu
----------------------------------------
@Description    -   This is a simple function that takes in the dictionary, utilizes the string
                    information passed for to/from currency, and returns the correctly calculated
                    conversion amount based on input values.

@Date Modified
5/3/2022 9:26 PM
"""
# below is imported only for the needs to test with driver. otherwise this import is not necessary
from Scraper import get_exchange_list


def convert(from_currency, to_currency, names_values, amount):
    # baseline of the imported table is US Dollar, so if converting from US Dollar,
    # we just multiply amount by value in dict
    if from_currency == "US Dollar":
        return float(names_values[to_currency]) * amount
    else:
        return float((float(names_values[to_currency]) / float(names_values[from_currency])) * amount)


if __name__ == "__main__":
    datetime, x_rates = get_exchange_list()
    value = convert("Japanese Yen", "Swiss Franc", x_rates, 1)
    print(value)
