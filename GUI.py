"""
@Author     :       William Thomas
@File       :       GUI.py
@Email      :       wdthomas2@dmacc.edu
----------------------------------------
@Description    -   Simple GUI that has an input textbox for amount wishing to be converted.
                    There are 2 dropdown menus available that allow you to select which currency to
                    convert from, and which to convert to. Once you press calculate, the converted currency
                    is displayed with the currency symbol

@Date Modified
4/28/2022 6:43 PM
"""
import tkinter as tk
from tkinter import ttk

from Convert import convert
from Scraper import get_exchange_list
from currency_symbols_dict import get_currency_symbol


class MainApp(tk.Frame):

    # we want to define the initialization of the window to call setup_widgets()
    def __init__(self, window, *args, **kwargs):
        tk.Frame.__init__(self, window, *args, **kwargs)
        self.window = window
        window.title("Currency Converter")
        self.setup_widgets()

    def perform(self):
        # here we will perform the calculation on the values selected
        try:
            input_amount = float(self.textbox_amount.get("1.0", tk.END))
        except ValueError:
            self.textbox_output.config(text="INVALID INPUT AMOUNT", font=("Arial", 18))
            return
        from_currency = self.from_val.get()
        to_currency = self.to_val.get()
        output_amount = round(float(convert(from_currency, to_currency, self.names_values, input_amount)), 4)
        self.textbox_output.config(text=get_currency_symbol(to_currency) + " " + str(output_amount), font=("Arial", 32), width="45")

    # widgets setup for window GUI
    def setup_widgets(self):
        # fix the size of the window. no resizing allowed, and large values won't resize the window
        self.window.geometry("400x300")
        self.window.minsize(400, 300)
        self.window.maxsize(400, 300)
        self.date_updated, self.names_values = get_exchange_list()
        # create lists to hold the information to be displayed in GUI
        self.Names = []
        self.Values = []
        # loop through the dict, and assign keys and values to lists
        for key, value in self.names_values.items():
            self.Names.append(key)
            self.Values.append(value)
        # define and create the label that holds information about when the local file was last updated
        self.updated_label = tk.Label(self.window, text=f"Last Updated:{self.date_updated.strftime('%b %d %Y %H:%M')} UTC")
        self.amount_label = tk.Label(self.window, text="Amount")
        self.from_val_label = tk.Label(self.window, text="From")
        self.to_val_label = tk.Label(self.window, text="To")
        self.output_label = tk.Label(self.window, text="Output")

        self.textbox_amount = tk.Text(height="1", width=45)
        self.textbox_output = tk.Label(self.window, height="1", width="45")
        self.textbox_output.config(state=tk.DISABLED)

        self.from_val = ttk.Combobox(values=self.Names, takefocus=0)
        self.to_val = ttk.Combobox(values=self.Names, takefocus=0)
        self.from_val.current(0)
        self.to_val.current(1)

        self.Button_calculate = tk.Button(self.window, text="Calculate", command=self.perform)

        self.amount_label.grid(row=0, column=1, sticky=tk.W)
        self.textbox_amount.grid(row=1, column=1, stick=tk.EW)

        self.from_val_label.grid(row=2, column=1, sticky=tk.W)
        self.from_val.grid(row=3, column=1, sticky=tk.EW)

        self.to_val_label.grid(row=4, column=1, sticky=tk.W)
        self.to_val.grid(row=5, column=1, sticky=tk.EW)

        self.output_label.grid(row=5, column=1, sticky=tk.W)
        self.textbox_output.grid(row=6, column=1, sticky=tk.EW, pady='10')

        self.Button_calculate.grid(row=8, column=1, sticky=tk.N)
        self.updated_label.grid(row=10, column=1, sticky=tk.S)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=5)
        self.window.columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(0, minsize=10)
        self.window.grid_columnconfigure(2, minsize=10)
        self.window.grid_rowconfigure(9, minsize=10)


def main():
    window = tk.Tk()
    MainApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()

