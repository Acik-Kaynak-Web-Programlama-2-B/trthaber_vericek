from tkinter import *
from bs4 import BeautifulSoup
import requests
import webbrowser

window = Tk()
window.geometry("700x700")
window.configure(bg='lightblue')

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/80.0.3987.163 Safari/537.36 "}
def haber_cek():
    
    url ="https://www.trthaber.com/haber/dunya/"
    request=requests.get(url, headers=header)
    tumVeriler = BeautifulSoup(request.content, "html.parser")
    haberler= tumVeriler.find("div",{"class":"bottom"}).findAll("div",{"class":"standard-card"}) 
    haber1.configure(text=haberler[0].find("div", {"class":"title"}).text)
    haber2.configure(text=haberler[1].find("div", {"class":"title"}).text)
    haber3.configure(text=haberler[2].find("div", {"class":"title"}).text)
    haber4.configure(text=haberler[3].find("div", {"class":"title"}).text)
def get_link1():
    url ="https://www.trthaber.com/haber/dunya/"
    request=requests.get(url, headers=header)
    tumVeriler = BeautifulSoup(request.content, "html.parser")
    haberler= tumVeriler.find("div",{"class":"bottom"}).findAll("div",{"class":"standard-card"})
    link= [haber.find("a")["href"] for haber in haberler]
    webbrowser.open(link[0])
def get_link2():
    url ="https://www.trthaber.com/haber/dunya/"
    request=requests.get(url, headers=header)
    tumVeriler = BeautifulSoup(request.content, "html.parser")
    haberler= tumVeriler.find("div",{"class":"bottom"}).findAll("div",{"class":"standard-card"})
    link= [haber.find("a")["href"] for haber in haberler]
    webbrowser.open(link[1])
def get_link3():
    url ="https://www.trthaber.com/haber/dunya/"
    request=requests.get(url, headers=header)
    tumVeriler = BeautifulSoup(request.content, "html.parser")
    haberler= tumVeriler.find("div",{"class":"bottom"}).findAll("div",{"class":"standard-card"})
    link= [haber.find("a")["href"] for haber in haberler]
    webbrowser.open(link[2])
def get_link4():
    url ="https://www.trthaber.com/haber/dunya/"
    request=requests.get(url, headers=header)
    tumVeriler = BeautifulSoup(request.content, "html.parser")
    haberler= tumVeriler.find("div",{"class":"bottom"}).findAll("div",{"class":"standard-card"})
    link= [haber.find("a")["href"] for haber in haberler]
    webbrowser.open(link[3])
        


haber1 = Button(window,command=get_link1)
haber1.grid(row=0,column=0)

haber2 = Button(window,command=get_link2)
haber2.grid(row=1,column=0)


haber3 = Button(window,command=get_link3)
haber3.grid(row=2,column=0)

haber4 = Button(window,command=get_link4)
haber4.grid(row=3,column=0)

CekButton = Button(window,text="Haber çek",command=haber_cek)
CekButton.grid(row=8,column=0)
window.mainloop()