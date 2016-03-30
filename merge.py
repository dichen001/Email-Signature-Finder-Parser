#!/usr/bin/env python
#
######### DO NOT USE UNTIL RESULTS ARE SAVED #########
#

import os
import sys

START_MARKER = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
END_MARKER = "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

def main():
    dir_of_data_files = "./data/body/"
    mergeFile = "emails_merged.txt"
    try:
        fout = open(mergeFile, 'w')
        for file in os.listdir(dir_of_data_files):
            fp = open(dir_of_data_files.strip('\/') + '/' + file, 'r')
            fout.write(START_MARKER + file + '\n')
            for line in fp:
                fout.write(line)
            fp.close()
            fout.write(END_MARKER + '\n')
        fout.close()
    except IOError:
        print "Files fail to open"
        sys.exit(-1)

if __name__ == "__main__":
    main()