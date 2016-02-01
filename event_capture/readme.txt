This directory contains a set of scripts that can be used to prepare
mov files for deposit into the repository as presentation suitable
webm and mp4 files, with thumbnail and poster images.

The mov files must be in the exact format specified in the Event Capture Group
Workflow document, available on Google Drive at
https://docs.google.com/a/vt.edu/document/d/1k64YRRvRobi8-_VoDd4lAXZeMDJBKLeyZ-ANOrMMEbQ/edit?usp=sharing

Usage instructions:

1. Download these scripts onto a large storage device with suitable room
   for processing video files. The included ffmpeg binary is intended to work
   on your Macintosh
 
2. Copy the ".mov" video files to be processed into the "event_capture" folder

3. Rename the .mov files to eliminate any characters that might be problematic.
   For example, quotes....
   
3. From the event_capture directory, run the command 
   "perl ./1process_mov_for_ir.pl"
    Lots and lots of output will display in your console.
    
4. Check back, usually in several hours. For each .mov file in the directory,
   there should be a .mp4 file, a .webm file, two .jpg thumbnails, and a .jpg
   movie poster image.
   
5. If desired, run "perl ./2mov_mov.pl" to move the videos and generated 
   artifacts into their own separate directories. This allows other video files
   to be processed using the scripts, and prevents the scripts from trying to 
   process previous work a second time.

6. Deposit the generated files into VTechWorks. The .mp4 and .webm files
   go into the ORIGINAL/CONTENT bundle. Thumbnails go into the THUMBNAIL
   bundle. The movie poster goes into the MOVIEPOSTER bundle. The original
   .mov file should not go into VTechWorks; it is instead slated to go into
   the dark archive.
   
7. Inline video playback should now be enabled (automatically) on the item.


Problems:

1. ALWAYS KEEP COPIES OF THE ORIGINAL FILES BEFORE RUNNING THIS SCRIPT.
This script does not perform sufficient error checking, and has been known
to result in accidental deletion of files if the format is not correct.

2. These scripts have problems with certain characters in filenames, for example,
   single quotes. 

3. The script is only intended to work on videos in the format specified in 
   the Google Drive document at
   https://docs.google.com/a/vt.edu/document/d/1k64YRRvRobi8-_VoDd4lAXZeMDJBKLeyZ-ANOrMMEbQ/edit?usp=sharing

4. There are two scripts; these should be made into one single script after 
error-handling is added.

etc.