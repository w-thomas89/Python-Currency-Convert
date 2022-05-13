"""
@Author     :       William Thomas
@File       :       currency_symbols_dict.py
@Email      :       wdthomas2@dmacc.edu
----------------------------------------
@Description    -   Here we have designated a dictionary based on the values found on x-rates.com tables.
                    This simple function will just take the string value from data.txt and search through
                    the dict for a matching key and returns the value. If no key is found, it simply returns
                    an empty string.

@Date Modified
5/3/2022 10:39 PM
"""


def get_currency_symbol(input_currency):
    symbol_set = {
        'US Dollar': '$',
        'Euro': '€',
        'British Pound': '£',
        'Indian Rupee': '₹',
        'Australian Dollar': '$',
        'Canadian Dollar': '$',
        'Singapore Dollar': '$',
        'Swiss Franc': 'CHF',
        'Malaysian Ringgit': 'RM',
        'Japanese Yen': '¥',
        'Chinese Yuan Renminbi': '¥',
        'Argentine Peso': '$',
        'Bahraini Dinar': 'Дин',
        'Botswana Pula': 'P',
        'Brazilian Real': 'R$',
        'Bruneian Dollar': '$',
        'Bulgarian Lev': 'лв',
        'Chilean Peso': '$',
        'Colombian Peso': '$',
        'Croatian Kuna': 'kn',
        'Czech Koruna': 'Kč',
        'Danish Krone': 'kr',
        'Hong Kong Dollar': '$',
        'Hungarian Forint': 'Ft',
        'Icelandic Krona': 'kr',
        'Indonesian Rupiah': 'Rp',
        'Iranian Rial': '﷼',
        'Israeli Shekel': '₪',
        'Kazakhstani Tenge': 'лв',
        'South Korean Won': '₩',
        'Kuwaiti Dinar': 'د.ك',
        'Libyan Dinar': 'ل.د',
        'Mauritian Rupee': '₨',
        'Mexican Peso': '$',
        'Nepalese Rupee': '₨',
        'New Zealand Dollar': '$',
        'Norwegian Krone': 'kr',
        'Omani Rial': '﷼',
        'Pakistani Rupee': '₨',
        'Philippine Peso': '₱',
        'Polish Zloty': 'zł',
        'Qatari Riyal': '﷼',
        'Romanian New Leu': 'lei',
        'Russian Ruble': '₽',
        'Saudi Arabian Riyal': '﷼',
        'South African Rand': 'R',
        'Sri Lankan Rupee': '₨',
        'Swedish Krona': 'kr',
        'Taiwan New Dollar': 'NT$',
        'Thai Baht': '฿',
        'Trinidadian Dollar': 'TT$',
        'Turkish Lira': '₺',
        'Emirati Dirham': ' د.إ',
        'Venezuelan Bolivar': 'Bs'
    }
    try:
        return symbol_set[input_currency]
    except:
        return ""


if __name__ == "__main__":
    print(get_currency_symbol("Sri Lankan Rupee"))
    print(get_currency_symbol("Polish Zloty"))
