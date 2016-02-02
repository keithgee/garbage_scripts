#!/usr/bin/perl
use strict;
use warnings;

use File::Find;

# This script can be used to create
# a map file for a DSpace collection
# when it is missing.
#
# This is useful when automated
# and well-defined updates are needed
# to a collection, for example with
# the ItemImport tool.
# 
# Use the dspace export command to
# export the collection.
# 
# Place this script in the exported
# collection directory.
#
# Run this script to output a mapfile
# to stdout.

my $handlefile = "handle";
my $dir = '.';

find(\&add_mapfile_entry, $dir);

sub add_mapfile_entry 
{
  if (-d && ($_ ne '.') )  {
   
    if (-e "$_/$handlefile")  {
      open(my $fh, '<:encoding(UTF-8)', "$_/$handlefile")
        or die "Could not open '$handlefile' $!";
      my $handle =  <$fh>;
      print "$_ $handle";
    }
  }
}
