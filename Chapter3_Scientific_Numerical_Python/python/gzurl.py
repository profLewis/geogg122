import urllib2, io, gzip, tempfile
from sys import exit

class gzurl(object):
    '''
    Download gzipped url to a local file or string

    Prof. P. Lewis, UCL, 
    Thu 10 Oct 2013 12:01:00 BST
    p.lewis@ucl.ac.uk

    '''
    def __init__(self,url,\
		filename=None,\
		store=False,file=True):
        ''' initialise class instance
       
            Parameters:
            
            url   : url of gzipped file
 
            Options:
           
            filename:
                    specify a filename explicitly, rather than
                    a temporary file (default None) 
            store : boolean flag to store the uncompressed
                    data in self.data (default false)
            file  : boolean flag to store data to a file
                    (default True)
                    
        '''
        self.filename = filename
        self.store = store
        self.file = file
        self.url = url
        self.read(self.url)
        
    def read(self,url):
        '''
        read gzipped data from url
        and uncompress
        '''
        # open URL
        try:
            f = urllib2.urlopen(url)
        except:
            print "Error opening %s"%url
            exit(1)
            
        # read and uncompress data
        try:
            data=gzip.GzipFile(fileobj=io.BytesIO(f.read())).read()
        except:
            print "Error reading gzipped file from %s"%url
            exit(1)
            
        if self.file:
            try:
              if self.filename != None:
                f = open(self.filename,'w')
                f.write(data)
                f.close()
              else:
                # use tempfile to create a temporary file
                self.tf = tempfile.NamedTemporaryFile(delete=False)  
                self.tf.write(data)
                self.filename = self.tf.name
            except:
              print "Error writing to %s"%self.filename
              exit(1)
        if self.store:
          self.data = data
 
    def close(self):  
        '''
        Tidy up
        '''
        if self.file:
	  try:
            self.tf.unlink(self.tf.name)
            del self.tf
          except:
            pass

    def __del__(self):
        '''
        Destriuctor

        Tidy up
        '''
        try:
            self.close()
        except:
            pass

