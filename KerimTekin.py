from tkinter import *
import webbrowser
import requests
from bs4 import BeautifulSoup

adres = "https://www.trthaber.com/haber/dunya/"

window = Tk()
window.geometry("600x600")
window.configure(bg="white")

def haber_cek():
    header ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/80.0.3987.163 Safari/ 537.36 "}
    url = adres
    
    request= requests.get(url, headers=header)
    
    tumVeriler = BeautifulSoup(request.content, "html.parser")
    haberler = tumVeriler.find("div", {"class": "bottom"}).findAll("div", {"class": "standard-card"})
    
    # başlıkların linki
    titles = [haber.find("div", {"class": "title"}).text for haber in haberler]
    urls = [haber.find("a")["href"] for haber in haberler]
    
    # düğmelerin metni ve komutu
    haber1.configure(text=titles[0], command=lambda: open_url(urls[0]))
    haber2.configure(text=titles[1], command=lambda: open_url(urls[1]))
    haber3.configure(text=titles[2], command=lambda: open_url(urls[2]))
    haber4.configure(text=titles[3], command=lambda: open_url(urls[3]))

def open_url(url):
    webbrowser.open(url)

haber1 = Button(window)
haber1.grid(row=0, column=0)

haber2 = Button(window)
haber2.grid(row=1, column=0)

haber3 = Button(window)
haber3.grid(row=2, column=0)

haber4 = Button(window)
haber4.grid(row=3, column=0)

CekButton = Button(window, text="haber", command=haber_cek)
CekButton.grid(row=4, column=3)

window.mainloop()