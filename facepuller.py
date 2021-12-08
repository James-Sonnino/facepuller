import time
import urllib.request
import os
import concurrent.futures

url = "https://thispersondoesnotexist.com/image"

#setting up the headers
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

while True:
    try:
        n = int(input("How many faces do you want to download?\n"))
        break
    except:
        print("\nPlease enter an integer!\n")

try:
    os.mkdir("faces")
except FileExistsError:
    pass
except:
    print("Couldn't create folder. Exiting now...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(n):
        f = executor.submit(urllib.request.urlretrieve, url, f"faces\\face{i+1}.jpg")
        #without the sleep we would download many duplicate images
        time.sleep(1.2)


        


