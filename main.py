from tkinter import Tk, ttk
from tkinter import *

############ importando #########

import json
import requests
import string

#################### PIL ###############
from PIL import ImageTk, Image,ImageOps , ImageDraw



################# cores ###############
cor0 = "#FFFFFF"  # white / branca
cor1 = "#333333"  # black / preta
cor2 = "#38576b"  # dark blue / azul escuro

janela = Tk()
janela.geometry('300x320')
janela.title('Conversor')
janela.configure(bg=cor0)

style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

top = Frame(janela, width=300, height=60, pady=0,padx=0, bg=cor1,  relief="flat",)
top.grid(row=0, column=0, columnspan=2)

main = Frame(janela, width=300, height=260,bg=cor0, pady=5, padx=0, relief="flat",)
main.grid(row=1, column=0, sticky=NSEW)


def converter():
    moeda_1 = combo1.get()
    moeda_2 = combo2.get()

    response = requests.get(
        "https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=a10561193ecc59f44c35".format(moeda_1, moeda_2))

    dados = json.loads(response.text)

    res = []

    [res.extend([k, v]) for k, v in dados.items()]

    final = float(valor.get()) * float(res[1])
    
    if moeda_2 == 'USD':
        simbolo = '$'
    elif moeda_2 == 'INR':
        simbolo = '₹'
    elif moeda_2 == 'EUR':
        simbolo = '€'
    elif moeda_2 == 'BRL':
        simbolo = 'R$'
    elif moeda_2 == 'AOA':
        simbolo = 'Kz'
    
    
    amount = 123456.78
    thousands_separator = ","
    fractional_separator = "."

    currency = simbolo+" {:,.2f}".format(final)

    if thousands_separator == ".":
        main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        currency = new_main_currency + fractional_separator + fractional_currency
    
    resultado.configure(text=currency)
    


################# top frame ####################

icon = Image.open('images/icons8-money-60.png')
icon = icon.resize((40, 40), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
app_name = Label(top,image=icon, compound=LEFT, text="Conversor de moeda ", height=5, pady=30, padx=13,
               relief="raised", anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)


################ main frame #####################

resultado = Label(main, text='', width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg='#ffffff', fg=cor1)
resultado.place(x=50, y=10)

moeda = ['AOA', 'BRL', 'EUR', 'INR', 'USD']

app_ = Label(main,text='De', width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10  bold'), bg=cor0, fg=cor1)
app_.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8,  justify=CENTER,font=('Ivy 12 bold'))
combo1['values'] = (moeda)
combo1.place(x=50, y=115)

app_ = Label(main,text='Para', width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2['values'] = (moeda)
combo2.place(x=160, y=115)

valor = Entry(main, width=22,justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(main, text="Converter ", command=converter, width=19,padx=5, height=1, bg=cor2, fg=cor0,  font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
botao.place(x=50, y=210)


janela.mainloop()
