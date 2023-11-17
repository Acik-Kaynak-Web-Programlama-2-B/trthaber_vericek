import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

def scrapping():
    liste = []

    x = requests.get("https://www.trthaber.com/haber/dunya/")
    soup = BeautifulSoup(x.text,"html.parser")
    
    data = soup.find_all("div",{"class":"standard-card"})
    for i in data:
        div = i.find("div",{"class","title"})
        a = div.find("a")
        liste.append((a.text,a["href"]))
        
    return liste


def open(link):
    webbrowser.open(link)

window = tk.Tk()
window.geometry("600x600")
window.title("Haberler")

for i in scrapping():
    tk.Button(window,text=i[0],command = lambda link = i[1]: open(link)).pack(expand = True)

window.mainloop()
        
