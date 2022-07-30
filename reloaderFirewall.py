import os
import webbrowser
import time
import keyboard
"""
        THIS CODE IS GENERALLY USED TO SOMEHOW BYPASS THE FIREWALL OR CONTINUOUSLY REFRESH THE FIREWALL
        SO AS TO GET THE BYPASSING OF FIREWALL AND ALSO HELPING THE ACCESS TO BE DONE REMOTELY.
        THIS IS SOLELY MADE TO ELIMINATE THE PING COMMAND FROM COMMAND PROMPT BECAUSE THE PING COMMAND 
        CANNOT KEEP ON REFRESHING THE FIREWALL PAGE.
        CREDITS FOR DEVELOPMENT: HADYY XD
        P.S. - THIS IS MADE FOR FUN AND TO ENABLE THE REMOTE ACCESS OF SUPERCOMPUTER WITH MY COMPUTER
        BEING OUTSIDE OF THE INTRA-NETWORK OF COLLEGE LDCE. 
"""
print(os.getcwd())                                             #FOR CHECKNG THE DIRECTORY
print("--------->OPENING BROWSER<---------")
print("--------------------")
I = 1
while True:
    keyboard.press_and_release('ctrl+w')                       #USED TO CLOSE THE EXISTING FORTINET FIREWALL PAGE
    file = "http://10.0.2.2:1000/keepalive?0e010f0c080a0568"   #SETTING UP THE LINK
    open = webbrowser.open(file)                               #OPENING THE LINK IN BROWSER
    print("OPENED BROWSER - " + str(I))
    print("--------------------")
    I = I + 1
    time.sleep(1000)                                           #MAKING THE CRAWLER CRAWL AFTER SPECIFIED TIME
