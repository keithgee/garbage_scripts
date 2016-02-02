#!/usr/bin/python
import csv
import os   
import sys

# To run this script:
# python split_csv_file.py filename.csv

# This script is used to split a CSV file containing VTechWorks item
# metadata into a separate CSV file for each item.
#
# The CSV files that are created for individual items are stored in
# directories named '10919_handleSuffix'
# (after the VTechWorks handle prefix, and the specific handle Suffix in DSpace).
# Each file is named 'metadata.csv'
#
# The individual item CSV files will have all header fields from the original
# CSV file, even if the item does not have values for that specific field.
#


# This function attempts to get a handle suffix
# for the specific item.
#
# Due to a quirk in DSpace, it looks in
#   - dc.identifier.uri
#   - dc.identifier.uri[]
#   - dc.identifier.uri[en_US]
#
# Sometimes, an item in DSpace does not have a handle.
# In this case "HANDLE_NOT_FOUND_FOR_ITEM_itemID" is returned
#
# Note that due to the limitations of the metadata CSV files,
# this reflects the handle stored in item metadata. While
# this should reflect the actual handle of the item,
# sometimes there is a problem with DSpace where the metadata,
# including handle metadata, is incorrect.
def getHandleSuffix(row):
    
    if ('dc.identifier.uri' in row and
        row['dc.identifier.uri'] != '' and
        'hdl.handle.net' in row['dc.identifier.uri']) :

     handleUrl = row['dc.identifier.uri']
     suffix = handleUrl.split("/")[4]

    elif ('dc.identifier.uri[]' in row and
           row['dc.identifier.uri[]'] != '' and
           'hdl.handle.net' in row['dc.identifier.uri[]']) :

        handleUrl = row['dc.identifier.uri[]']
        suffix = handleUrl.split("/")[4]
            
    elif ('dc.identifier.uri[en_US]' in row and
          row['dc.identifier.uri[en_US]'] != '' and
          'hdl.handle.net' in row['dc.identifier.uri[en_US]']) :
    
        handleUrl = row['dc.identifier.uri[en_US]']
        suffix = handleUrl.split("/")[4]

    else:
        suffix = 'HANDLE_NOT_FOUND_FOR_ITEM_' + row['id']
    
    return suffix


REPOSITORY_ID = '10919'

# Print a usage message if the filename isn't included on the command line
if len(sys.argv) < 2:
    print('Usage: python ' + sys.argv[0] + ' filename.csv')
    print('\twhere filename.csv is the name of the csv file to split')
    sys.exit(1)

# Open the complete, original csv file 
with open(sys.argv[1]) as fullcsvfile:
    metadatareader = csv.DictReader(fullcsvfile)
       
    # get the full list of field names, which will be added at the top
    # of each new file
    fullfieldnames = metadatareader.fieldnames
        
    # for every item in the original file, create a separate csv file
    # in a directory named after the item handle
    for row in metadatareader:
       
        itemDir = REPOSITORY_ID + '_' + getHandleSuffix(row)
    
        if not os.path.exists(itemDir):
            os.mkdir(itemDir)
            with open(os.path.join(itemDir, 'metadata.csv'), 'wb') \
                                                as itemmetadatafile:
                metadatawriter = csv.DictWriter(itemmetadatafile,
                                                fieldnames=fullfieldnames)
                metadatawriter.writeheader()
                metadatawriter.writerow(row)
                itemmetadatafile.close()

    fullcsvfile.close()


