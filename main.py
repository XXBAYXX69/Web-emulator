# -+-<<School Filter Bypass (Kinda)>>-+-
# -<What Is This? >-
# This is basicaly an OS with Chromium (A version Of Chrome) running using webbot. 
# You can use it for ordanary browsing and stuff and can even download stuff! 
# (Make sure to use "save as..." otherwise it wont go into the files folder!)
#
# To use this to its best:
# -Use the slider bars to...
#   -Remove The Console From View
#   -Remove The Code From View
#   -Maximize The Viewport
# -Click on the file icon to remove the Files tab.
# There You go, press run, use it however you want and have fun!

from webbot import Browser
from time import sleep
web = Browser()
print('================================')
print('Made By: YeetsaJr')
print('g = www.Google.com')
print('Use Your own URL')
print('Leave Blank For Default Website')
print('================================')
website = input('Website: ')

if website == 'g':
	web.go_to('https://www.google.com/')

elif website == '':
	web.go_to('https://pypi.org/project/webbot')

else:
	web.go_to(website)

while True:
      sleep(0.1)