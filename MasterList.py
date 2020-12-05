import pandas as pd
import re
from selenium import webdriver
import time
import os.path

# import gzip

directory = (r'C:\Users\athlc\Desktop\Count\MASTERFILELIST.TXT')
dl_folder_path = (r'C:\Users\athlc\Downloads')

main_df = pd.DataFrame({'Zip File Name': [], 'Total Headlines': [], 'Keywords': []})

def open_url(gzip_url):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(gzip_url)
    dl_x_start = True
    while dl_x_start:
        for fname in os.listdir(dl_folder_path):
            if fname.endswith('.crdownload'):
                dl_x_start = False
                
    downloading_file = download_wait()
    if not downloading_file:
        driver.close()
        

def download_wait():
    dl_wait = True
    while dl_wait:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(dl_folder_path):
            if fname.endswith('.crdownload'):
                dl_wait = True
    return dl_wait


def what2do_gzip(gzipFile_url, read_condition):
    gzipFile_name = gzipFile_url.split('/')[-1]
    gzipFile_path = os.path.join(dl_folder_path, gzipFile_name)      
    if read_condition:
        gzip_df = pd.read_csv(gzipFile_path, compression='gzip', header=0, \
                              sep=',', quotechar='"', error_bad_lines=False)
        return gzip_df
    else:
        os.remove(gzipFile_path)


with open(directory) as f:
    lines = [line.rstrip() for line in f]
    # print(lines)
    main_df['Zip File Name'] = lines
    print(main_df)

    for row, gzipFile in enumerate(lines):
        pattern = r'[0-9]*[-]*[0-9]*[-]*[.csv.gz]*'
        keywords = re.sub(pattern, '', gzipFile)
        keywords = keywords.split('/')[-1]
        # print(keywords)
        main_df.iloc[row, (2)] = keywords

        open_url(gzipFile)
        url_df = what2do_gzip(gzipFile, True)
        
        no_of_rows = len(url_df.index)
        main_df.iloc[row, (1)] = no_of_rows

        what2do_gzip(gzipFile, False)
        url_df = None
