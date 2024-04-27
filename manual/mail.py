import smtplib
import imaplib
import email
import random


'''def userid():
    name = StringVar()
    sender_mail = Entry(textvariable = name ,)
    sender_mail.grid(column = 1 , row = 2 , columnspan = 2 , padx = 50 , pady = 50)
    validate = Button(text = "validate" ,command = doit)
    validate.grid(column = 1 , row = 3 , columnspan = 2 , padx = 10 , pady = 10)

def doit():
    print(f"Customers mail:{name.get()}")'''

def sendmail():
    #global random_number
    random_number = str(random.randint(1000, 9999))
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("autodbot2024@gmail.com", "trlz uqbw nkul rodl")
    # message to be sent
    message = f"Dear customer!!!\n One Time Password for your delivery is {random_number}\nReply the otp to autodbot2024@gmail.com for delivery completion"
    # sending the mail
    s.sendmail("autodbot2024@gmail.com", "prathamputhran45@gmail.com", message)
    # terminating the session
    s.quit()
    return random_number

#r = sendmail()
#print(r)



def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data




# Function to get the list of emails under this label
def get_emails(result_bytes,con):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)

    return msgs

def confirm(random_number):
    user = "autodbot2024@gmail.com"
    password = "trlz uqbw nkul rodl"
    imap_url = 'imap.gmail.com'
    # this is done to make SSL connection with GMAIL
    con = imaplib.IMAP4_SSL(imap_url)

    # logging the user in
    con.login(user, password)

    # calling function to check for email under this label
    con.select('Inbox')

    # fetching emails from this user "tu**h*****1@gmail.com"
    msgs = get_emails(search('FROM', "prathamputhran45@gmail.com", con),con)

    # Uncomment this to see what actually comes as data
    # print(msgs)


    # Finding the required content from our msgs
    # User can make custom changes in this part to
    # fetch the required content he / she needs

    # printing them by the order they are displayed in your gmail
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple:

                # encoding set as utf-8
                content = str(sent[1], 'utf-8')
                data = str(content)

                try:
                    indexstart = data.find("ltr")
                    data2 = data[indexstart + 5: len(data)]
                    indexend = data2.find("</div>")
                    if random_number in data2:
                    # printing the required content which we need
                    # to extract from our email i.e our body
                    #print(data2[0: indexend])
                        return True
                    else:
                        return False

                except UnicodeEncodeError as e:
                    pass

#   return true or false
#confirm("8334")
