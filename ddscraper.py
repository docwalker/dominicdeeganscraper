'''
Created on May 31, 2013

@author: Doc

'''


"""
The following was taken from http://stackoverflow.com/questions/257409/download-image-file-from-the-html-page-source-using-python
and then modified to my own needs.

dumpimages.py
    Downloads all the images on the supplied URL, and saves them to the
    specified output file ("/test/" by default)

Usage:
    python dumpimages.py http://example.com/ [output]
"""

from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from urllib import urlretrieve
import time
import re

def main(url, out_folder):
    """Downloads all the images at 'url' to /test/"""
    baseurl = url[:-24]
    i = 0
    while(True):
        
        soup = bs(urlopen(url))    
        comicDate = url[-10:]
        comicDate = comicDate.replace('-',"")
        
        for image in soup.findAll("img"):
            #print "Image: %(src)s" % image
            
            if comicDate in image["src"]:
                imagePath = image["src"]
                comicPath = baseurl + imagePath
                
                urlretrieve(comicPath, out_folder + str(i + 1) + ".gif")
                
                #after comic is done follow the next button to the next comic.
                #messy but it works.  Find the word "Next" 
                #findAll returns a list.  There is only one known elment so get that
                #this element is a beautful soup tag element.  Can be treated as a dictionary
                nextDate = soup.findAll(alt="Next")[0]
                url = baseurl + nextDate.previous_element['href']
                i = i + 1
                
                #artificial sleep so we don't spam the host servers too much.
                time.sleep(3)
    
def _usage():
    print "usage: python dumpimages.py http://example.com [outpath]"

if __name__ == "__main__":
    main("http://www.dominic-deegan.com/view.php?date=2002-05-21", "D:\\Comics\\Dominic-Deegan\\")
