#!/usr/bin/python3
#
# Goes thru the m3u file, validates the file path if invalid searches 
# for a new path from the given media directory.
#
# It writes a new playlist to stdout.
#
# <uros@isotel.eu>, 29 November 2015

import sys
import glob, os


def find_music(old_file, find_file, media):
    for root, dirs, files in os.walk(media):
        for file in files:
            if file == find_file:
                new_file = os.path.join(root, file)
                sys.stderr.write("   Found: " + new_file + "\n")
                print(new_file)
                return
                
    sys.stderr.write("   Unavailable!\n")
    print(old_file)


if len(sys.argv) != 3:
    sys.stderr.write("m3u_fix <playlist> <media_dir>\n")
    sys.exit(1)

with open( sys.argv[1] ) as inf:
    music_files = [line.strip() for line in inf.readlines() if not line.startswith('#')]
    
print("#EXTM3U")

for check_file in music_files:
    sys.stderr.write("Checking [" + check_file + "]: ")
    
    if os.path.isfile(check_file):
        sys.stderr.write("VALID\n")
        print(check_file)
    else:    
        sys.stderr.write("INVALID\n")
        find_file = check_file.split('/')[-1]
        sys.stderr.write(".. Searching for: " + find_file + "\n")
        find_music(check_file, find_file, sys.argv[2])
