'''
Used to extract the raw results.csv file from Amazon MT to keep the marked email into 'xxx_body'
and the sender name into 'xxx_sender'. The generated files will be used for further processing.
'''


import os
import re
import csv
DIR = os.path.abspath(os.path.dirname(__file__))
base_dir = DIR + '/tests/fixtures/signature'
turk_csv = base_dir + '/turk1000_results.csv'
dest_folder = base_dir + '/emails/big_turk_marked/'

def extract(csv_file,folder):
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email_name = row['Input.email1']
            origin = row['Input.content1']
            sender = row['Input.sender1']
            marked = row['Answer.MarkedEmail_1']
            # flag = row['Answer.Q1Answer']
            # if flag == 'Y' or flag is None:
            #     print origin
            #     print '>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<'
            #     print marked
            # else:
            #     continue
            body_filename = re.sub('\d+\.$', change_name_body, email_name)
            f = open(folder + body_filename, 'w')
            f.write(marked)
            f.close()
            sender_filename = re.sub('\d+\.$', change_name_sender, email_name)
            f = open(folder + sender_filename, 'w')
            f.write(sender.strip())
            f.close()

def change_name_body(matchobj):
    if matchobj.group(0)[-1]=='.':
        return matchobj.group(0)[:-1] + '_body'

def change_name_sender(matchobj):
    if matchobj.group(0)[-1]=='.':
        return matchobj.group(0)[:-1] + '_sender'

extract(turk_csv,dest_folder)