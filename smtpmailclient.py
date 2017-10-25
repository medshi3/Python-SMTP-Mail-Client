# Python version  - 2.7.13
# SMTP Gmail Client
# Made by Bryce Golamco

#SMTP client is defaulted to send at smtp.gmail.com with port 587


import smtplib
import socket

global serverport
global servername
serverport= 587
servername = 'smtp.gmail.com'

clientemail = 'None'
clientpassword = 'None'
destinationemail = 'None'
emailsubject = ''
emailbody = ''



emailhelp = """
Type in these codes to change the data to be sent.

!read               - prints out all the email info
!send               - sends the message
!back               - goes back to the main command line

!changeweb          - changes to a common website that has smtp support

!portnumber         - changes the server port
!servername         - changes the server name

!clientad           - changes the client's email address
!clientpass         - changes the client's email password

!emailad            - changes the email address destination
!emailsubject       - changes the email subject
!emailbody          - changes the email body

!help               - displays the instructions.
"""
def listandset():   # lists out all available website in the code
    global servername
    global serverport
    print('Type the name of the listed mailing websites to set Port number and Server name')
    print('Common websites include:')
    print('gmail')
    print('yahoomail')
    print('outlook')

    reply = raw_input()

    if (reply == 'gmail'):
        serverport = 587
        servername = 'smtp.gmail.com'
    elif(reply == 'yahoomail' or reply == 'yahoo'):
        serverport = 587
        servername = 'smtp.mail.yahoo.com'
    elif (reply == 'outlook'):
        serverport = 587
        servername = 'smtp-mail.outlook.com'
    elif(reply != '!back'):
        print('Website is not on the list')


            
def send(): #Sends the message
    try:
        conn = smtplib.SMTP(servername,serverport)
        conn.ehlo()
        conn.starttls()
        conn.login(clientemail,clientpassword)
        conn.sendmail(clientemail,destinationemail,'Subject:' + emailsubject + '\n\n' + emailbody)
        conn.quit()
        print('Success')
    except smtplib.SMTPServerDisconnected:
        print('Server disconnected unexpectedly')
    except smtplib.SMTPSenderRefused:
        print('Sender address invalid')
    except smtplib.SMTPRecipientsRefused:
        print('All recipient addresses have been refused')
    except smtplib.SMTPDataError:
        print('SMTP Server does not accept the message data')
    except smtplib.SMTPConnectError:
        print('Could not establish a connection with the server')
    except smtplib.SMTPHeloError:
        print('Server refuses the HELO message')
    except smtplib.SMTPAuthenticationError:
        print('Authentication Error, Incorrect username or password')
        print('Try allowing unsecure logins to your account')
    except:
        print('Unknown Error')




print('Type !help to start.')
while True:
    print('Currently in main command line')
    reply = raw_input()

    if(reply == '!read'):               # Prints out all the info of the message to be sent except for the password
        print('\n')
        print('Message details:')
        print('Server Port Number:' + str(serverport))
        print('Server Name: ' + str(servername))
        print('Email: ' + clientemail)
        print('Destination Email: ' + destinationemail)
        print('Subject: ' + emailsubject)
        print('Body: ' + emailbody)
        print('\n')
    elif (reply == '!send'):            # Sends the email
        print('Sending ...')
        send()
    elif (reply == '!changeweb'):        # Changes the email body of the email
        listandset()
    elif (reply == '!portnumber'):      # Changes the port number of the server to send (defaulted at 587)
        print('Write the port number of the website:')
        reply = raw_input()
        if (reply != '!back'):
            serverport = int(reply)
    elif (reply == '!servername'):      # Changes the servername (defaulted at smtp.gmail.com)
        print('Write the servername of the website:')
        reply = raw_input()
        if (reply != '!back'):
            servername = str(reply)
    elif (reply == '!clientad'):         # Changes the Client's email address
        print('Write the email address of the client:')
        reply = raw_input()
        if (reply != '!back'):
            clientemail = reply
    elif (reply == '!clientpass'):       # Changes the Client's password
        print('Write the password of the client:')
        reply = raw_input()
        if (reply != '!back'):
            clientpassword = reply
    elif (reply == '!emailad'):         # Changes destination email address
        print('Write the destination email address:')
        reply = raw_input()
        if (reply != '!back'):
            destinationemail = reply
    elif (reply == '!emailsubject'):     # Changes the email's subject
        print('Write the Subject of the email:')
        reply = raw_input()
        if (reply != '!back'):
            emailsubject = reply
    elif (reply == '!emailbody'):        # Changes the email body of the email
        print('Write the body of the email:')
        reply = raw_input()
        if(reply != '!back'):
            emailbody = reply
    else:
        print(emailhelp)




