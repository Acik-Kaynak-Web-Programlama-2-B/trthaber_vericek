from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk

form =tk.Tk()
form.title("HABERLER")

sayfa = requests.get ("https://www.trthaber.com/haber/dunya/")

sayfa_icerik = bs (sayfa.text, "html.parser")

gerekli_kisim = sayfa_icerik.findAll("div",{"class":"standard-card"})
#print(gerekli_kisim)
haber_listesi = []
for i in gerekli_kisim:
    haberler =i.find("div",{"class":"title"})
    #print(haberler)                 
    haberler_link_ve_baslik = haberler.find("a")
    
    #print(haber_link_ve_baslık["href"])
    haber_listesi.append(
        (haberler_link_ve_baslik["href"],
        haberler_link_ve_baslik.text.strip())
        )
        
    
print(haber_listesi[0] [0])
print(haber_listesi[1] [0])
print(haber_listesi[2] [0])
print(haber_listesi[3] [0])
    
lbl_haber1 =tk.Label(text=haber_listesi[0][1]).pack()
lbl_haber1_link = tk.Label(text=haber_listesi[0][0]).pack()
    
lbl_haber2 = tk.Label(text=haber_listesi[1][1]).pack()
    
form.mainloop()