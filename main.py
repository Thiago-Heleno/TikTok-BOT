import os
import sys
import PySimpleGUI as sg
from threading import Thread
import undetected_chromedriver.v2 as uc
import pathlib, pickle
from selenium.webdriver.common.keys import Keys
from API.ChangeUserInformation import ChangeUserInformation
from API.ReadCookieData import ReadCookieData
from API.GetProxies import GetProxies
import time
import string
import random

script_dir = os.path.dirname(__file__)


#View video function
def playVideo(driver, url):
  #driver.get(url)
  driver.refresh()
  try:
    time.sleep(5)
    playBtn = driver.find_element_by_css_selector('div.tiktok-player-icon').click()
    playBtn.click()
    #time.sleep(random.randrange(80, 100))
  except:
    print("An exception occurred")
  
  

#Like Video function
def likeVideo(driver):
  print("ASDASDASDSD")
  try:
    likeBtn = driver.find_element_by_css_selector('svg.like-heart')
    likeBtn.click()
  except:
    print("No Like Button Found!")


#Share video function
def shareVideo(driver):
  try:
    shareBtn = driver.find_element_by_css_selector('div.tiktok-toolbar-share ')
    shareBtn.click()
    time.sleep(3)
    try:
      whatsappBtn = driver.find_element_by_css_selector('div.i-copylink')
      whatsappBtn.click()
      #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
      time.sleep(3)
      driver.close()
    except:
      print("No Whatsapp Btn Found!")
  except:
    print("No share Btn found")
    

#Spoof Ip
def spoofIp():
  print("What??")

def boost_video(url):
  driver = load_cookie_file(url, "dump_users/1/cookies.pkl")
  playVideo(driver, url)
  likeVideo(driver)
  shareVideo(driver)
  

def MultiThread(url, threadsAmmount):
  users = len(os.listdir("./dump_users"))
  threads = []
  for i in range(int(threadsAmmount)):
    threads.append(Thread(target=boost_video(url)))
  for thread in threads:
    thread.start()
  for thread in threads:
    thread.join()


def save_cookies_file(url):
  num = len(os.listdir("./dump_users"))
  pathAdd = "dump_users\\" + str(num + 1)
  path = os.path.join(script_dir, pathAdd)
  try:
    if not os.path.exists(path):
        os.makedirs(path, 0o666)
  except OSError:
    sys.exit('Fatal: output directory "' + path + '" does not exist and cannot be created')
  options = uc.ChromeOptions()
  
  #pres = GetProxies.BrazilHttp()
  #print(pres['curl'])
  #proxy = "--proxy-server=" + pres['curl']
  #options.add_argument(proxy)
  
  
  driver = uc.Chrome(options=options)
  driver.get(url)
  input("Press Enter to Dump Cookies...")
  patda = "cookies.pkl"
  piupiu = os.path.join(path, patda)
  pickle.dump(driver.get_cookies(), open(piupiu, "wb"))

def load_cookie_file(url, file):
  options = uc.ChromeOptions()
  options.add_argument("--user-agent=" + random.choice(mobileUserAgent))
  driver = uc.Chrome(options=options)
  driver.get(url)
  cookies = pickle.load(open(file, "rb"))
  for cookie in cookies:
    if 'sameSite' in cookie:
        if cookie['sameSite'] == 'None':
            cookie['sameSite'] = 'Strict'
    driver.add_cookie(cookie)
  return driver

def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)
def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

def main():
  data = make_table(num_rows=15, num_cols=6)
  headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]

  def InitialLayout():
    sg.theme('Reddit')
    layout = [
      [sg.Text("Type the video Url!")],
      [sg.Input("", key="url"),sg.Button('Boost Video')],
      [sg.Button('Add Account')],
      [sg.Button("Show Dump_Accounts")],
      [sg.Text("Threads Ammount"),sg.Slider(orientation ='horizontal', key='stSlider', range=(1,100))],
    ]
    return sg.Window('Initial', layout=layout, finalize=True)

  def DumpAccountsLayout():
    sg.theme('Reddit')
    layout = [
      [sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
      [sg.Text("Dump Accounts")],  
      [sg.Button("Read Cookie")],
    ]
    return sg.Window('DumpAccounts', layout=layout, finalize=True)

  window1, window2 = InitialLayout(), None
  while True:             # Event Loop
      window, event, values = sg.read_all_windows()
      if window == window1 and event == sg.WIN_CLOSED:
          break
      elif window == window2 and event == sg.WIN_CLOSED:
        window2.hide()
      elif event == 'Add Account':
        save_cookies_file("https://tiktok.com")
      elif event == 'Boost Video':
        MultiThread(values['url'], values['stSlider'])
        #boost_video(values['url'])
      elif event == "Read Cookie":
        ReadCookieData.ReadCookie(os.path.join(script_dir, "dump_users\\"+ values['-Table-'] +"\\cookies.pkl"))
      elif event == "Show Dump_Accounts":
        window2 = DumpAccountsLayout()
  window.Close()


mobileUserAgent = [
  "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
  "Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53",
  "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4",
  "Mozilla/5.0 (iPhone; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.25 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
]


if __name__ == "__main__":
  main()  