from bs4 import BeautifulSoup
import urllib2
import os
import requests

def checkurls(url,excludedlinks,checkedlinks):
    """ This function fetches the given url html and returns all links found
        (except those containing the excludedlinks string).
    """
    page=urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(),'html.parser')

    links = [ x.get('href') for x in soup.findAll('a', attrs={'href':True}) if x.get('href').find(excludedlinks) == -1]

    for l in links:
        # if it's external link
        if l not in checkedlinks['alldone'] and l.find("http://") == 0 and l.find(excludedlinks) == -1:
            print "check status code for:\n" + l
            status_code = str(get_status_code(l))
            print status_code
            checkedlinks[status_code] = checkedlinks[status_code] + [l]
            checkedlinks['alldone'] = checkedlinks['alldone'] + [l]
    return checkedlinks
    

def get_status_code(url):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        r = requests.head(url)
        return r.status_code
        # return the int of the status code.
    except requests.ConnectionError:
        return None


print "---START EXTRACTING---"

checkedlinks = {'200':[],'204':[],'300':[],'301':[],'302':[],'304':[],'307':[],'400':[],'401':[],'404':[],'405':[],'403':[],'500':[],'503':[],'504':[],'550':[],'None':[],'alldone':[]}

try:
    excludedlinks = os.environ["EXCLUDE_LINKS"]
    print "urls to ignore are based on domain: " + excludedlinks
except KeyError:
    print "all urls will be extracted."
    excludedlinks = 'dummydomainthatdoesnotexistonthisplanet.eu'


with open('data/urls-to-analyze.txt') as file:
    for line in file:
        print "\n"
        print "Extracting urls from: " + line
        urls = checkurls(line,excludedlinks,checkedlinks)

print "FINAL REPORT:"
for status in checkedlinks.keys():
    print "For status code " + status + " count is " + str(len(checkedlinks[status]))

print "Note. None stands for ConnectionError: we could not get HEAD info from server"

print "full dictionary list:"
print checkedlinks
print "---THE END---"