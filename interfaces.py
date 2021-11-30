import tkinter as tk
from tkinter import ttk
import calculate


def format_coins(coins):
    text = ''
    for coin in coins:
        text += coin[0] + " - " + str(coin[1]) + " , "

    text = text.removesuffix(', ')
    return text


def get_coins(entry, label):
    cont = 0
    list = []
    for ent in entry:

        # This will ignore letters, unfilled entries, negative numbers, and floats.
        # This will return a formatted string ready to be used by the coin_to_value function
        try:
            amount = int(ent.get())
            coin = label[cont]['text']
            list.append([coin, amount])

            cont += 1

        except (ValueError, TypeError):

            amount = 0
            coin = label[cont]['text']
            list.append([coin, amount])

            cont += 1
            pass

    return list


def get_value(pound_entry, shilling_entry, pence_entry):
    try:
        pounds = int(pound_entry.get())
    except (ValueError, TypeError):
        pounds = 0

    try:
        shillings = int(shilling_entry.get())
    except (ValueError, TypeError):
        shillings = 0

    try:
        pence = int(pence_entry.get())
    except (ValueError, TypeError):
        pence = 0

    return pounds, shillings, pence


def clutch(root, frame, height, width):
    root.geometry(f"{width}x{height}")
    frame.configure(width=width, height=height)
    frame.tkraise()


class ConvertValueToCoin(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)

        self.pound_label = ttk.Label(self, text='Pounds:')
        self.shilling_label = ttk.Label(self, text='Shillings:')
        self.pence_label = ttk.Label(self, text='Pence:')

        self.pound_entry = ttk.Entry(self)
        self.shilling_entry = ttk.Entry(self)
        self.pence_entry = ttk.Entry(self)

        # pound block
        self.pound_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)
        self.pound_entry.grid(column=0, row=1, sticky=tk.W, padx=10)

        # shilling block
        self.shilling_label.grid(column=1, row=0, sticky=tk.W, padx=10, pady=5)
        self.shilling_entry.grid(column=1, row=1, sticky=tk.W, padx=10)

        # pence block
        self.pence_label.grid(column=2, row=0, sticky=tk.W, padx=10, pady=5)
        self.pence_entry.grid(column=2, row=1, sticky=tk.W, padx=10)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(column=0, row=3, columnspan=2, pady=10, sticky=tk.W)

        # conversion button
        self.button = ttk.Button(self, text='Convert', command=self.display)
        self.button.grid(column=1, row=2, pady=20, ipadx=5, ipady=5)

    def display(self):
        pounds, shillings, pence = get_value(self.pound_entry, self.shilling_entry, self.pence_entry)
        farthings = calculate.lowest_denomination(pounds, shillings, pence)
        result = calculate.value_to_coins(farthings)

        text = format_coins(result)
        self.result_label['text'] = text


class ConvertCoinsToValue(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # This makes an indeterminate amount of labels and entries for an indeterminate amount of enabled coins.
        # All the entries have a specific number that refers to them.
        self.inner_frames = []
        count, enabled = 0, 0
        self.entry = []
        self.label = []
        for coin in calculate.denomination:
            if coin[2]:  # If the coin is enabled
                self.inner_frame = ttk.Frame(self)
                self.label.append(ttk.Label(self.inner_frame, text=coin[0]))
                self.entry.append(ttk.Entry(self.inner_frame))
                self.label[enabled].pack()
                self.entry[enabled].pack()

                self.inner_frames.append(self.inner_frame)
                enabled += 1

            count += 1

        count = 0
        column_count = 0
        for block in self.inner_frames:
            block.grid(column=column_count, row=count, padx=5, pady=5, sticky=tk.W)
            count += 1

            if count == 6:
                column_count += 1
                count = 0

        self.result_label = ttk.Label(self)
        self.result_label.grid(column=2, row=1001, pady=5)

        self.button = ttk.Button(self, text='Convert', command=self.display)
        self.button.grid(column=2, row=1000, padx=10)

    def display(self):

        list = get_coins(self.entry, self.label)
        value = calculate.coins_to_value(list)
        readable = calculate.farthings_to_readable(value)

        self.result_label['text'] = readable


class SimplifyCoin(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)

        # This makes an indeterminate amount of labels and entries for an indeterminate amount of enabled coins.
        # All the entries have a specific number that refers to them.

        self.fake_frame = ttk.Frame(self)
        self.inner_frames = []
        count, enabled = 0, 0
        self.entry = []
        self.label = []
        for coin in calculate.denomination:
            if coin[2]:
                inner_frame = ttk.Frame(self.fake_frame)
                self.label.append(ttk.Label(inner_frame, text=calculate.denomination[count][0]))
                self.entry.append(ttk.Entry(inner_frame))
                self.label[enabled].pack()
                self.entry[enabled].pack()

                self.inner_frames.append(inner_frame)
                enabled += 1

            count += 1

        count = 0
        column_count = 0
        for block in self.inner_frames:
            block.grid(column=column_count, row=count, padx=5, pady=5, sticky=tk.W)
            count += 1

            if count == 6:
                column_count += 1
                count = 0

        self.fake_frame.grid(column=0, row=0)

        self.result_label = ttk.Label(self)
        self.result_label.grid(column=0, row=2, padx=5, pady=5)

        self.button = ttk.Button(self, text='Simplify', command=self.simplify)
        self.button.grid(column=0, row=1, padx=5, pady=5)

    def simplify(self):
        coins = get_coins(self.entry, self.label)
        value = calculate.coins_to_value(coins)
        new_coins = calculate.value_to_coins(value)
        result = format_coins(new_coins)

        self.result_label['text'] = result


class SimplifyValue(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)

        self.pound_label = ttk.Label(self, text='Pounds')
        self.shilling_label = ttk.Label(self, text='Shillings')
        self.pence_label = ttk.Label(self, text='Pence')

        self.pound_entry = ttk.Entry(self)
        self.shilling_entry = ttk.Entry(self)
        self.pence_entry = ttk.Entry(self)

        # pounds
        self.pound_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)
        self.pound_entry.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

        # shillings
        self.shilling_label.grid(column=1, row=0, sticky=tk.W, padx=10, pady=5)
        self.shilling_entry.grid(column=1, row=1, sticky=tk.W, padx=10, pady=5)

        # pence
        self.pence_label.grid(column=2, row=0, sticky=tk.W, padx=10, pady=5)
        self.pence_entry.grid(column=2, row=1, sticky=tk.W, padx=10, pady=5)

        self.result_label = ttk.Label(self)
        self.result_label.grid(column=1, row=3, padx=5, pady=5)

        self.button = ttk.Button(self, text='Simplify', command=self.simplify)
        self.button.grid(column=1, row=2, padx=5, pady=5)

    def simplify(self):
        pounds, shillings, pence = get_value(self.pound_entry, self.shilling_entry, self.pence_entry)
        farthings = calculate.lowest_denomination(pounds, shillings, pence)
        readable = calculate.farthings_to_readable(farthings)

        self.result_label['text'] = readable


class Settings(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.button = []
        count, row_count, column_count = 0, 0, 0
        for coin in calculate.denomination:

            if coin[2]:
                self.button.append(ttk.Button(self, text=f"Disable {coin[0]}",
                                         command=lambda a=coin: self.toggle(a)))
                self.button[count].grid(row=row_count, column=column_count, padx=5, pady=5, sticky=tk.W)
            else:
                self.button.append(ttk.Button(self, text=f"Enable {coin[0]}",
                                         command=lambda a=coin: self.toggle(a)))
                self.button[count].grid(row=row_count, column=column_count, padx=5, pady=5, sticky=tk.W)

            count += 1
            row_count += 1
            if row_count == 6:
                row_count = 0
                column_count += 1

    def toggle(self, coin):
        count = 0

        for match in calculate.denomination:
            if coin[0] == match[0]:
                calculate.denomination[count][2] = not calculate.denomination[count][2]
                break

            count += 1

        if calculate.denomination[count][2]:
            self.button[count]['text'] = f"Disable {calculate.denomination[count][0]}"
        else:
            self.button[count]['text'] = f"Enable {calculate.denomination[count][0]}"
