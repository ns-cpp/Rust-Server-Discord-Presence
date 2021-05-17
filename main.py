from pypresence import Presence # The simple rich presence client in pypresence
from time import time,sleep
from requests import get
from bs4 import BeautifulSoup
from pyautogui import alert


URL = 'https://www.battlemetrics.com/servers/rust/10854743'


while True:
    try:
        client_id = "840646540984057856"  # Put your Client ID in here (Discord bot)
        RPC = Presence(client_id)  # Initialize the Presence client

        RPC.connect()

        RPC.update(state="Online",
                    details="Rank : Founder",
                    large_image="1948boys",
                    small_image="rusticon",
                    party_size=[30,150],
                    large_text="1948boys.shop",
                    buttons=[{"label": "Discord", "url": "https://discord.gg/WtneGuqWrX"}]
                    )
        break
    except:
        alert(text='Discord a bağlanılamadı!', title='1948boys.com', button='Tekrar Dene')
               

while True:  # The presence will stay on as long as the program is running
    # 19:48 = 71280
    while True:
        try:

            page = get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            playerCount = soup.find_all("dd")[1].text  
            break
        
        except:
            sleep(5000)
    
    remaining = time() - 71300
    RPC.update(state="Online " + str(playerCount),
               details=soup.find("h2").text,
               large_image="1948rust",
               small_image="rusticon",
               large_text="1948boys.shop",
               buttons=[{"label": "Discord", "url": "https://discord.gg/WtneGuqWrX"},
                    {"label": "Oyna", "url": "steam://connect/185.254.29.98:10000"}],
               start=remaining)
               
               
    sleep(15) # Can only update rich presence every 15 seconds  // 
    
    
