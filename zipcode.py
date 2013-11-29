import urllib
import urllib2
from bs4 import BeautifulSoup
from operator import itemgetter
import sys

def zipinfo(zipcode):

    url = "http://zipwho.com/?zip=" + zipcode  + "&city=&filters=--_--_--_--&state=&mode=zip"

    request = urllib2.Request(url, headers={'User-Agent':"Magic Browser"})
    result = urllib2.urlopen(request)

    page = BeautifulSoup(result)

    x = page.find("script").get_text().split("\"")[1].split(",");
    return x



if __name__ == "__main__":
    print(zipinfo("1011215"))
