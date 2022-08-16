#change directory to deposit files
import os
os.chdir('C:\\Users\\(change here)\\files')

#libraries
import pandas as pd
import requests # important to access APIs
from contextlib import closing
import csv
from codecs import iterdecode


node_ids = pd.DataFrame({'id':[6886,6919)], #add as required the PRTG ids
                         'name':['node_id1','node_id2']}) #introduce meaningful node names to you
for x in range(0,1): # as many PRTGs ids you want
    api_url = "https:// (PRTG IP) /api/historicdata.csv?id={}&avg=300&sdate=2022-07-01-00-00-00&edate=2022-08-01-00-00-00&username= (username) &passhash= (passhash)".format(node_ids['id'][x])
    req = requests.get(api_url, verify= False)
    url_content = req.content
    csv_file = open('{}.csv'.format(node_ids['name'][x]), 'wb')
    csv_file.write(url_content)
    csv_file.close()
    print("{}".format(node_ids['id'][x]))


