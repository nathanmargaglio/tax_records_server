#!/usr/bin/env python

import django
import os
import sys
import csv
import time
import re
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tax_records.settings')
django.setup()

from rest_api.models import Record

if sys.argv[1] == 'delete-all':
    # Obviously a very bad function
    # Use with caution
    Record.objects.all().delete()
    exit()

with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    if headers != ['', 'city', 'link', 'owner_name', 'property_location', 'sbl', 'swis']:
        error_message = "You're headers are incorrect.  Please format data to:\n"
        error_message += ', '.join(['', 'city', 'link', 'owner_name', 'property_location', 'sbl', 'swis'])
        raise Exception(error_message)

    index = 0
    tt = time.time()
    records = []

    for row in reader:
        t0 = time.time()
        index += 1

        r = Record()
        street_regex = re.compile("(\d+)\W*\d*(.+)").match(row[4])
        try:
            r.street_number = int(street_regex.group(1).strip())
            r.route = street_regex.group(2).strip()
        except AttributeError as e:
            r.street_number = None
            r.route = row[4].strip()

        r.city = row[1]
        r.county = "Erie County"
        r.state = "NY"
        r.link = row[2]
        r.sbl = row[5]
        r.swiss = row[6]
        records.append(r)

        r.raw_name = row[3].strip()
        try:
            r.first_name = row[3].strip().split(' ')[1]
        except:
            pass
        try:
            r.last_name = row[3].strip().split(' ')[0]
        except:
            pass

        records.append(r)

        tf = time.time()

        if not index % 1000:
            print("{:6d}: Current: {}s  Total: {}s".format(index, tf - t0, t0 - tt))

    Record.objects.bulk_create(records)
