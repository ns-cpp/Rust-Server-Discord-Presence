from pypresence import Presence # The simple rich presence client in pypresence
from time import sleep,time
from requests import get
from bs4 import BeautifulSoup
from pyautogui import alert

username = "cmyS"
URL = 'https://dlive.tv/' + username

i = 5

client_id = "842413598734549032"  # Put your Client ID in here (Discord bot)
RPC = Presence(client_id)  # Initialize the Presence client

while True:     #bağlantı döngüsü
    try:
        RPC.connect()
        break
    except:
        alert(text='Discord a bağlanılamadı!', title='1948boys.com', button='Tekrar Dene')
        


remaining = time()



while True:     # The presence will stay on as long as the program is running
                # 19:48 = 71280

    try:

        while True:
            try:
                page = get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')
                izleyici = soup.find("div",attrs={"class":"marginl-4 text-12-medium text-white text-nowrap"}).text
                oyun = soup.find("span",attrs={"class":"overflow-ellipsis tag-box"}).text
                baslik = soup.find("div",attrs={"class":"tooltip text-14-medium text-white stacking-context overflow-hidden"}).text
                break
            except:
                sleep(5000)
        

        RPC.update(
                    state=izleyici,
                    details=baslik + " " + oyun + " oynuyor",
                    large_image="cmys",
                    small_image="dlive",
                    large_text="cemyS",
                    buttons=[{"label": "Discord", "url": "https://discord.gg/5MjdnUZyV8"},
                        {"label": "İzle", "url": "https://dlive.tv/"+ username}],
                    start=remaining)
                    
                    
        sleep(15) # Can only update rich presence every 15 seconds  // 
    except:
        while i >= 1:
            alert(text='Sanırım yayının kapalı? \n ' + str(i) + ' denemeden sonra program kapanacak!', title='1948boys.com', button='Tekrar dene')
            i = i - 1
        exit()
    
