import numpy as np

'''
Utility to pull a url list of MODIS LAI files
for given year (can be list of years) 
and tile (can be list of tiles)

Returns a dictionary of the urls

Also saves the dictionary to processed_file

'''
def modis_lai_files(year,tile,\
                    processed_file = 'files/data/processed.npz',\
                    url_base = \
                    'http://e4ftl01.cr.usgs.gov/MODIS_Composites/MOTA/MCD15A2.005'):
    import urllib2
    import numpy as np
    # generalise to suppose year and tile might be arrays
    year = np.atleast_1d(year).astype(str)
    tile = np.atleast_1d(tile).astype(str)
    
    hdf_files = []   

    response = urllib2.urlopen(url_base)
    print 'reading',url_base
    html = response.read()
    
    dirs = np.array([line.split('href="')[1].split('/">')[0] \
                     for line in html.split('\n') if line.find('[DIR]') != -1][1:])
    
    # identify years
    years = np.array([i.split('.')[0] for i in dirs])
    # year mask : better done with in1d
    # in case year is an array
    mask = np.in1d(years,year)

    sub_dirs = dirs[mask]
    
    for this_date in sub_dirs:
        url_date = url_base + '/' + this_date
        print '...',url_date
        response1 = urllib2.urlopen(url_date)
        html1 = response1.read()
        
        # generalise in case tile is an array
        hdf_lines = []
        for line in html1.split('\n'):
            if np.in1d(line,tile)[0] and line.find('.hdf"') != -1:
                hdf_lines.append(line)
        for hdf_line in hdf_lines:
            hdf_file = url_date + '/' + hdf_line.split('<a href="')[1].split('">')[0]
            hdf_files.append(hdf_file)

    hdf_files = np.array(hdf_files)
    return hdf_files

def save_hdf_files(hdf_files):
    processed = dict(zip(hdf_files,np.zeros_like(hdf_files).astype(bool)))
    np.savez(processed_file,processed=processed)
    return processed


def pull_urls(processed):
    # always puts data in files/data

    import urllib2

    processed_file = None

    if type(processed) == str:
      # processed data file npz
      processed_file = processed
      processed = np.load(processed_file)['processed']

    files = []
    for url,done in processed.items():
        files.append('files/data/' + url.split('/')[-1])
        if not done:
            response = urllib2.urlopen(url)
            ofile = 'files/data/' + url.split('/')[-1]a
            print 'pulling',url
            f = open(ofile,'w')
            f.write(response.read())
            f.close()
            print '     to',ofile
            processed[url] = True
            # update the log
            if processed_file:
                np.savez(processed_file,processed=processed)
    return files


def modis_lai_doit(year,tile):
    hdf_files = modis_lai_files(year,tile)
    processed = save_hdf_files(hdf_files)
    files = pull_urls(processed)
