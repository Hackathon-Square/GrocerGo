
import smtplib
import asyncio
from email.mime.text import MIMEText

import os
from square.client import Client

from giftcards import create_gift_card, activate_gift_card

# 发件人信息
sender_email = "square_bob@163.com"
password = "URINSGYNAPANROVB"



def send_an_email_to_customer(user_query, customer_email):

    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
    smtp.login(sender_email,password)

    # 邮件正文
    message = MIMEText("You don't have permission to do this!😭😭😭\n" + user_query + "\nThis is an automated email." + "\nDo not reply!", "plain", "utf-8")

    message["Subject"] = "An email from square administrator"
    message["From"] = sender_email
    message["To"] = customer_email

    smtp.sendmail(sender_email,[customer_email],message.as_string())
    smtp.close()

    print("The email was successfully sent!")


# TODO

def give_gift_card_to_customer(customer_email):

    client = Client(access_token=os.environ["SQUARE_ACCESS_TOKEN"], environment="sandbox")
    result = create_gift_card(client)
    result = activate_gift_card(client)


async def send_message_and_wait_administrator_confirm(user_query, customer_email):

    # Simulating sending message
    print(f"Sending user query: {user_query} to administrator...")
    await asyncio.sleep(2)

    # Simulating wait for confirmation
    print("Waiting for administrator confirmation...")
    await asyncio.sleep(3)

    administrator_confirmed = False

    if administrator_confirmed:

        give_gift_card_to_customer(customer_email)

        return 1

    else:
        return 0



if __name__ == "__main__":

    send_an_email_to_customer()