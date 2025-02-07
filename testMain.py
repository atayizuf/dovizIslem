from secondim import *
from datetime import datetime
import io
from contextlib import redirect_stdout

cevrimAdet = input('Çevrim Adedini Gir : ')

def write_to_file(output_data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{cevrimAdet}_adet_doviz_sonuclari_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output_data)
    return filename

# Capture output using string buffer
f = io.StringIO()
with redirect_stdout(f):
    print("\n*********Banka Gişeleri Büroları;\n")
    euroBankaGiseGetir("https://finans.mynet.com/doviz/bankagise/", cevrimAdet)
    print("\n*********Döviz Büroları;\n")
    euroBankaGiseGetir("https://finans.mynet.com/doviz/dovizburosufiyatlari/", cevrimAdet)
    print("\n*********Merkez Bankasi;\n")
    euroBankaGiseGetir("https://finans.mynet.com/doviz/merkezbankasi/", cevrimAdet)

output_data = f.getvalue()
filename = write_to_file(output_data)

# Also print to console
print(output_data)
print(f"\nSonuçlar '{filename}' dosyasına kaydedildi.")