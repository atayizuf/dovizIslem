import requests
from datetime import date
from bs4 import BeautifulSoup
import re
import pandas as pd

def euroBankaGiseGetir(link, cevrimAdet):
    Data ={
        "Alan Kurum": [],
        "Alış": [],
        "Satis": [],
        "Fark": [],
        "Saat": []
    }
    istek = requests.get(link)
    pars = BeautifulSoup(istek.content, "html.parser")
    yazi = pars.find("tbody", {"class": "tbody-type-default"}).find_all("strong")
    kacadet = int(cevrimAdet)
    veriler = []
    for i in yazi:
        isim = i.string
        if re.search(".*Euro.*", isim):
            alis = i.parent.parent.find_all("td")[2].string
            satis = i.parent.parent.find_all("td")[3].string
            fark = i.parent.parent.find_all("td")[4].string
            saat = i.parent.parent.find_all("td")[5].string
            deger2 = alis.split(",")
            deger3 = deger2[0] + "." + deger2[1]
            sonuc = kacadet * float(deger3)
            veriler.append(deger3)
            Data["Alan Kurum"].append(isim.strip())
            Data["Alış"].append(alis)
            Data["Satis"].append(satis)
            Data["Fark"].append(fark)
            Data["Saat"].append(saat)
            # print(
            #     isim.strip() + " alis fiyatından : 1 x " + deger3,
            #     saat,
            #     "-------------",
            #     f"{sonuc:.2f}",
            # )

    def ortalamaAl(kacadet, deger3):
        toplam = 0
        for i in range(kacadet):
            toplam += float(deger3[i])
        return toplam / kacadet
    
    df=pd.DataFrame(Data)
    veri=df.sort_values(by=['Alış'], ascending=False) #Sıralama
    print(veri)
    print(f"\n--- Hesaplama için {cevrimAdet} adet döviz kullanılmıştır...")
    print(f"--- Ortalama Alış Fiyatı : {ortalamaAl(len(veriler), veriler):.2f}")

    print(f"\n--- Alış Ortalaması ------------------------> {cevrimAdet} EURO : { int(cevrimAdet) * ortalamaAl(len(veriler), veriler):.2f} TL")
    
    # print(df["Alış"].mean()) #Ortalama Pandas işleri kolaylaştırır gibi