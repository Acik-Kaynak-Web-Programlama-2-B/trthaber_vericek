import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import webbrowser

def scrapping():
    liste = []
    liste = []
    x = requests.get("https://www.trthaber.com/haber/dunya/")
    soup = BeautifulSoup(x.text,"html.parser")
    
    data = soup.find_all("div",{"class":"standard-card"})
    for i in data:
        div = i.find("div",{"class","title"})
        a = div.find("a")
        liste.append((a.text,a["href"]))
        
    return liste
    response = requests.get("https://www.trthaber.com/haber/dunya/")
    soup = BeautifulSoup(response.text,"html.parser")
    data = soup.find_all("div",{"class":"standard-card"})
    for i in data:
        div = i.find("div",{"class":"title"})
        a = div.find("a")
        link = a["href"]
        liste.append((a.text,link))
        
    return liste

def open(link):
    webbrowser.open(link)

window = tk.Tk()
window.geometry("600x600")
window.title("Haberler")

button_dic = {}

for i in scrapping():
    button_dic[i] = ttk.Button(window,text=i[0],command = lambda link = i[1]: open(link))
    button_dic[i].pack(expand = True)

window.mainloop()
        
