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
# directories named '10919_itemId'
# (after the VTechWorks handle prefix, and the # specific item ID in DSpace).
# Each file is named 'metadata.csv'
#
# The individual item CSV files will have all header fields from the original
# CSV file, even if the item does not have values for that specific field.
#

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
    # in a directory named after the item id
    for row in metadatareader:
        itemId = row['id']
        itemDir = REPOSITORY_ID + '_' + itemId

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
