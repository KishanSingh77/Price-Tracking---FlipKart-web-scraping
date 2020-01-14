import requests
from bs4 import BeautifulSoup
import smtplib


def send_mail(price):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #enter username and password to login to google smtp
    server.login('###########' ,'$$$$$$$' )

    subject = 'Prices fell!!'
    body = 'check out the product!! https://www.flipkart.com/portronics-harmonics-222-bluetooth-headset-mic/p/itm8e282b53734e0?pid=ACCFMYF7QHTZEBVX&lid=LSTACCFMYF7QHTZEBVXNDLNHY&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_3C5Q9IAFHBX2_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&fm=neo%2Fmerchandising&iid=13738078-9326-408f-a2a8-58b035fe7e16.ACCFMYF7QHTZEBVX.SEARCH&ppt=browse&ppn=browse&ssid=4ixsytndqo0000001579039067946'
    msg = f"Subject: {subject}\n\n{body}"
    print(msg)
    #enter any 2 usernames
    server.sendmail('###########','###########',msg)

    server.quit()

URL='https://www.flipkart.com/portronics-harmonics-222-bluetooth-headset-mic/p/itm8e282b53734e0?pid=ACCFMYF7QHTZEBVX&lid=LSTACCFMYF7QHTZEBVXNDLNHY&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_3C5Q9IAFHBX2_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&fm=neo%2Fmerchandising&iid=13738078-9326-408f-a2a8-58b035fe7e16.ACCFMYF7QHTZEBVX.SEARCH&ppt=browse&ppn=browse&ssid=4ixsytndqo0000001579039067946'
headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL , headers)

soup = BeautifulSoup(page.content , 'html.parser')

price = soup.findAll("div", {"class": "_1vC4OE _3qQ9m1"})[0].get_text()

print(price )
send_mail(price)





