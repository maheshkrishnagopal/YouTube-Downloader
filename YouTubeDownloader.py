'''
YouTube Downloader v.0.0.2
--------------------------

Name of the Program: YouTube Downloader
Scope: This program has been created with best module available in Python. But, this can also be optimized and can get better structure.
Author: Maheshkrishna A G
Module Used: Pafy
Version: 0.0.2
Description: This Python program downloads Youtube videos in mp4 format, by default, (in best available resolution), to your local directory, when the URL is given.
Input: Youtube video URL.
Date: 26-04-2017
'''
from pafy import *;

def status(total, recvd, ratio, rate, eta):
    print(recvd, ratio, eta);
    

url=input("Enter the YouTube url to download: ");
video=pafy.new(url);
print("Ready to download, " + video.title + "? (y/n)");
action=input();
if (action=='y'):
    try:
        print ("Downloading !!! " + video.title);
        best=video.getbest(preftype="mp4");
        filename=best.download(quiet=True, callback=status, filepath="LOCAL_SYSTEM FILE_PATH");
        print("Download Completed!!! Please check in this path - LOCAL_SYSTEM FILE_PATH");
        exit=input("Press any key to Exit!");
    except:
        print ("Unexpected Error Occured, hence download failed!");
        exit=input("Enter any key to Exit:");
else:
    print("Exiting the program:");
    print("Press any key to exit");
    exit();

    
    

