from HTMLParser import HTMLParser
import urllib2
import numpy as np
import wget

'''
Bare bones of a script to get MODIS dataset
'''

# url found from reverb ordering
url = 'http://e4ftl01.cr.usgs.gov//MODV6_Cmp_A/MOTA/MCD15A2H.006/'
tile = 'h31v11'
dates = '2013.02.18'

# read htl of base url 
response = urllib2.urlopen(url + dates)
html = response.read()
tile = 'h31v11'
date = '2013.02.18'

# see https://docs.python.org/2/library/htmlparser.html#module-HTMLParser
# parse the html to get data
# check data characteristics are ok
# and form geturl to download with wget

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
      if len(data):
        sdata = data.split()
        if len(sdata) == 1:
          fdata = sdata[0].split('.')
          if (fdata[-1] == 'hdf') and (fdata[2] == tile):
            geturl = url + '/'  + dates + '/' + data
            # pull dataset
            print geturl
            filename = wget.download(geturl)

parser = MyHTMLParser()
parser.feed(html)

# ProfLewis
# GeogG1222016
