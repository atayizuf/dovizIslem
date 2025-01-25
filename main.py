from secondim import *

cevrimAdet=input('Çevrim Adedini Gir : ')
print("\n*********Banka Gişeleri Büroları;\n")
euroBankaGiseGetir("https://finans.mynet.com/doviz/bankagise/",cevrimAdet)
print("\n*********Döviz Büroları;\n")
euroBankaGiseGetir("https://finans.mynet.com/doviz/dovizburosufiyatlari/",cevrimAdet)
print("\n*********Merkez Bankasi;\n")
euroBankaGiseGetir("https://finans.mynet.com/doviz/merkezbankasi/",cevrimAdet)