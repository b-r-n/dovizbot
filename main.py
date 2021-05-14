import requests
from bs4 import BeautifulSoup
import time
import threading
class Doviz:
    dolarhook = "https://discord.com/api/webhooks/842759257459130388/hS4tkYL16WLs3p3lWeqUulkMKhWm9TPpu-dIGpy0X6KQmmJOSCMEOo1RhQs9SCnKXiac"
    eurohook = "https://discord.com/api/webhooks/842759259720253450/3aIfdDecPKHO_G5tue7lvQZb_Od_XgDcgmjuBrbklWJUNVw7BUfJ_XXvI3-WB6Nmtfj9"
    altinhook = "https://discord.com/api/webhooks/842759281136762961/ZTLWx2QNSuVPCd3mUHMIjMoR7xwe9glU0f78SsiI34I1nXPIAO_iNX1usqudEt79OEmC"


    @classmethod
    def dollar(cls):
        r = requests.get("https://bloomberght.com/")
        soup = BeautifulSoup(r.content,'html.parser')
        veri = soup.find_all('small',attrs={'class':'value LastPrice'})
        dolar = veri[1].text
        return dolar

    @classmethod
    def euro(cls):
        r = requests.get("https://bloomberght.com/")
        soup = BeautifulSoup(r.content, 'html.parser')
        veri = soup.find_all('small', attrs={'class': 'value LastPrice'})
        meuro = veri[2].text
        return meuro

    @classmethod
    def altin(cls):
        r = requests.get("https://bloomberght.com/")
        soup = BeautifulSoup(r.content, 'html.parser')
        veri = soup.find_all('small', attrs={'class': 'value LastPrice'})
        gold = veri[5].text
        return gold

    @classmethod
    def discord(cls,message,hook):
        response = True
        result = requests.post(hook,data={'content':message})

        if str(result) != '<Response [204]>':
            response = False
        return response



def dolar():
   param = 0
   while True:

    kur = Doviz.dollar()
    kur = kur.replace(',','.')
    kur = float(kur)
    if param > kur:
        mesaj = f'🔴 Güncel Dolar Fiyatı {kur:.4f} | {kur - param:.5f} kadar düşüşte.'
    elif param == kur:
        mesaj = f'🟡 Güncel Dolar Fiyatı {kur:.4f} | Aynı fiyatta.'
    else:
        mesaj = f'🟢 Güncel Dolar Fiyatı {kur:.4f} | {kur - param:.5f} kadar yükselişte.'

    param = float(f'{kur:.4f}')

    Doviz.discord(mesaj,Doviz.dolarhook)

    time.sleep(60)
def euro():
   param = 0
   while True:

    kur = Doviz.euro()
    kur = kur.replace(',','.')
    kur = float(kur)
    if param > kur:
        mesaj = f'🔴 Güncel Euro Fiyatı {kur:.4f} | {kur - param:.5f} kadar düşüşte.'
    elif param == kur:
        mesaj = f'🟡 Güncel Euro Fiyatı {kur:.4f} | Aynı fiyatta.'
    else:
        mesaj = f'🟢 Güncel Euro Fiyatı {kur:.4f} | {kur - param:.5f} kadar yükselişte.'

    param = float(f'{kur:.4f}')
    Doviz.discord(mesaj, Doviz.eurohook)
    time.sleep(60)

def altin():
  param = 0
  while True:

    kur = Doviz.altin()
    kur = kur.replace('.','').replace(',','.')
    kur = float(kur)
    if param > kur:
        mesaj = f'🔴 Güncel Altın/Ons Fiyatı {kur:.2f} | {kur - param:.4f} kadar düşüşte.'
    elif param == kur:
        mesaj = f'🟡 Güncel Altın/Ons Fiyatı {kur:.2f} | Aynı fiyatta.'
    else:
        mesaj = f'🟢 Güncel Altın/Ons Fiyatı {kur:.2f} | {kur - param:.4f} kadar yükselişte.'

    param = float(f'{kur:.2f}')
    Doviz.discord(mesaj, Doviz.altinhook)
    time.sleep(60)


x = threading.Thread(target=dolar,args=())
x.start()
y = threading.Thread(target=euro,args=())
y.start()
z = threading.Thread(target=altin,args=())
z.start()



