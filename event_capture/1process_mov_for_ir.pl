#!/usr/bin/perl -w
#
# This script uses the command line version of ffmpeg on 
# scott221 to create mp4 files with .moov atom at front for
# mov video containers in the current directory
#
# It will also create webm files, thumbnails, and 
# movie poster files.

use strict;
use File::Copy;

umask 0000;


# get the list of mov files
my @movfiles = <*.mov>;



my $file; #original filename
my $result; # result of command line

foreach $file(@movfiles)
{
   print "$file\n";
   
   #create a mp4 version
   my $mp4file = $file;
   $mp4file =~ s/\.mov$/.mp4/;
   $result = `./ffmpeg -i '$file' -vf scale=854:-1 -pass 1 -f mp4 -b:v 1200k -an -pix_fmt yuv420p -y /dev/null`;
   $result = `./ffmpeg -i '$file' -vf scale=854:-1 -pass 2 -b:v 1200k -y -pix_fmt yuv420p -strict -2 -movflags faststart '$mp4file'`;

   #create a webm version
   my $webmfile = $file;
   $webmfile =~ s/\.mov$/.webm/;
   $result = `./ffmpeg -i '$file' -vf scale=854:-1 -pass 1 -an -vcodec libvpx -f webm -b:v 1200k -y /dev/null`;
   $result = `./ffmpeg -i '$file' -vf scale=854:-1 -pass 2 -b:v 1200k -y '$webmfile'`;

   my $thumbfile = $mp4file . ".jpg";
   print "$thumbfile\n";
   $result = `./ffmpeg -itsoffset -7.05 -i '$mp4file' -vcodec mjpeg -vframes 1 -an -f rawvideo -s 100x56 '$thumbfile'`; 

   #create a webm thumbnail version
   my $webmthumbfile = $thumbfile;
   $webmthumbfile =~ s/\.mp4\.jpg$/.webm.jpg/;
   print "$webmthumbfile\n";
   copy($thumbfile,$webmthumbfile) or die "Copy failed: $!";

  # poster
  my $posterfile = $mp4file;
  $posterfile =~ s/\.mp4$/.jpg/;
  $posterfile =~ s/\.m4v$/.jpg/;
  print "$posterfile\n";
  $result = `./ffmpeg -itsoffset -7.05 -i '$mp4file' -vcodec mjpeg -vframes 1 -an -f rawvideo  '$posterfile'`; 

}
