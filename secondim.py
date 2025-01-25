import requests
from datetime import date
from bs4 import BeautifulSoup
import re
import pandas as pd


def euroBankaGiseGetir(link, cevrimAdet):
    istek = requests.get(link)
    pars = BeautifulSoup(istek.content, "html.parser")
    yazi = pars.find("tbody", {"class": "tbody-type-default"}).find_all("strong")
    kacadet = int(cevrimAdet)
    # veriler = []
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
            # veriler.append(deger3)
            print(
                isim.strip() + " alis fiyatından : 1 x " + deger3,
                saat,
                "-------------",
                f"{sonuc:.2f}",
            )

    def ortalamaAl():
        toplam = 0
        for i in range(kacadet):
            toplam += float(deger3)
        return toplam / kacadet
    # ms = pd.DataFrame(veriler)
    # print(ms)
    # print("bursa")
    # print(float(ms.iloc[2, 0]) * 2)
    return print(f"--- Hesaplama için {cevrimAdet} adet döviz kullanılmıştır...")
