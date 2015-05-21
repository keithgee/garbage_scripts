#!/usr/bin/perl -w
#
# This script moves the mov files from incoming_mov directory to
# ready_for_deposit directory
# It will also move webm files, thumbnails, and 
# movie poster files.

use strict;
use File::Copy;

umask 0000;

# get the list of mov files
my @movfiles = <*.mov>;



my $file; #original filename
my $dirname;
my $result; # result of command line

foreach $file(@movfiles)
{
   $dirname = $file;
   $dirname =~ s/\.mov$//;
   $dirname = "../ready_for_deposit/" . $dirname;
   mkdir $dirname;

   print "$file\n";
   move($file, $dirname . "/" . $file); 
   
   #create a mp4 version
   my $mp4file = $file;
   $mp4file =~ s/\.mov$/.mp4/;
   move($mp4file, $dirname . "/" . $mp4file);

   #create a webm version
   my $webmfile = $file;
   $webmfile =~ s/\.mov$/.webm/;
    move($webmfile, $dirname . "/" . $webmfile);
  
   my $thumbfile = $mp4file . ".jpg";
   print "$thumbfile\n";
   move($thumbfile, $dirname . "/" . $thumbfile);

  my $webmthumbfile = $webmfile . ".jpg";
  print "$webmthumbfile\n";
  move($webmthumbfile, $dirname . "/" . $webmthumbfile);
 
  # poster
  my $posterfile = $mp4file;
  $posterfile =~ s/\.mp4$/.jpg/;
  $posterfile =~ s/\.m4v$/.jpg/;
  print "$posterfile\n";
  move($posterfile, $dirname . "/"  . $posterfile);

}
