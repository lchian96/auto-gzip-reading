# auto-gzip-reading
A mini project to download a long list of gzip files through URL and obtain data out of them automatically.

# Task: Download and Calculate no. of articles(indexes/rows) in each gzip files provided in the MASTERFILELIST.TXT

# I would personally download all those files together into my storage, then perform the data cleaning or whatever
# Just so that I missed out any steps or data I needed afterward because downloading these files take some time.
# This is a solution for: limited hardware storage, not familiar with cloud computing services like AWS.        
          
# Steps in this py:
# (1) Read the MasterList text file to get the URL
# (2) Uses selenium to open the URL
# (3) Wait for it to finish download
# (4) Close the browser after finish downloading
# (5) Read them into panda's Dataframe and get the total indexes/rows
  # you can add whatever you want to do to the dataframe here
  # since we will be deleting the file after read before continuing the next loop
# (6) Delete the files
  # note that py will remove the file from your PC permanently, not recycle bin
# (7) Continue looping
