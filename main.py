from tkinter import *
from Getreq import *

class Mainbody:
    def __init__(self):
        self.window = Tk()
        self.window.title("Currency Convertor")
        self.get_index_list1 = None
        self.get_index_list2 = None
        self.window.geometry("400x300")
        self.selected_currency = StringVar()
        self.selected_currency.set("Select Currency")
        self.list_box1 = Listbox(self.window,height=5)
        self.list_box2 = Listbox(self.window,height=5)
        self.Enter_amount = Label(self.window,text='Enter Amount')
        self.Enter_amount.place(x=20,y=30)
        self.Enter_amount2 = Label(self.window,text="Total Amount")
        self.Enter_amount2.place(x=20,y=200)
        self.enter_currency1=Entry(self.window,width=20)
        self.enter_currency1.place(x=120,y=32)
        self.box = Text(self.window,height=1,width=15)
        self.Convert = Button(self.window,text="Convert",command=self.printConvertedCurrency)
        self.Convert.place(x=150,y = 250)
        self.box.place(x=120,y=202)
        self.select_currency1 = Button(self.window,text="Select Currency",command=self.if_SelectCurrency1Clicked)
        self.select_currency1.place(x=270,y=29)
        self.select_currency2 = Button(self.window,text="Select Currency",command=self.if_SelectCurrency2Clicked)
        self.select_currency2.place(x=270,y=199)


        self.window.mainloop()
    def list_data(self, lb, val1, val2):
        options = [
            'INR', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN',
            'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP',
            'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD',
            'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
            'HUF', 'IDR', 'ILS', 'IMP', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID',
            'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
            'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR',
            'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR',
            'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB',
            'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES',
            'VND', 'V', 'UV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'
        ]
        for item in options:
            lb.insert(END, item)
        lb.place(x=val1,y=val2)
    def if_SelectCurrency1Clicked(self):
        self.list_data(self.list_box1, 260, 60)
        self.list_box1.bind('<<ListboxSelect>>', self.value_from_listBox1)


    def if_SelectCurrency2Clicked(self):
        self.list_data(self.list_box2, 260, 230)
        self.list_box2.bind('<<ListboxSelect>>', self.value_from_listBox2)


    def value_from_listBox1(self,event):
        val1 = self.list_box1.curselection()
        if val1:
            self.get_index_list1 = self.list_box1.get(val1[0])
            self.select_currency1.config(text=self.get_index_list1)
            self.list_box1.place_forget()
    def value_from_listBox2(self,event):
        val2 = self.list_box2.curselection()
        if val2:
            self.get_index_list2 = self.list_box2.get(val2[0])
            self.select_currency2.config(text=self.get_index_list2)
            self.list_box2.place_forget()

    def printConvertedCurrency(self):
        self.box.delete('1.0',END)
        self.obj = ExchangeCurrency(self.get_index_list1,self.get_index_list2)
        self.amnt_val = self.enter_currency1.get()
        self.new_amnt_val = int(self.amnt_val)
        self.box.insert('1.0',self.obj.give_value(self.new_amnt_val))




obj = Mainbody()




