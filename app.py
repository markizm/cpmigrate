#!/usr/bin/python

import requests
import base64
import json
import os
import argparse
import yaml
import sys
from cpmigrate import *

## just need user to provide testid(s) on cmd line
parser = argparse.ArgumentParser(description='retrieve test_id from user input')
parser.add_argument('-t', '--testid', type=str, help='id for test in catchpoint')
parser.add_argument('-d', '--divid', type=str, help='"client" = client division, "nonprod" = non-prod division, "consumer" = consumer division')
args = parser.parse_args()

if __name__ == '__main__':

    obj = Catchpoint().get_tests(args.testid)
    f = open('conf.yml')
    conf = yaml.load(f)
    obj['id'] = 0
    if args.divid  == "adplatform":
        adp_id = conf['ad-pltfrm_div']
        adp_pr = conf['adp-stg-product']
        obj['division_id'] = adp_id 
        obj['product_id'] = adp_pr
        if 'parent_folder_id' in obj:
            del obj['parent_folder_id']
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
        else:
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
    elif args.divid == "client":
        pr_id = conf['staging_product']
        cl_id = conf['client_div']
        obj['division_id'] = cl_id
        obj['product_id'] = pr_id
        if 'parent_folder_id' in obj:
            del obj['parent_folder_id']
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
        else:
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
    elif args.divid == "nonprod":
        pr_id = conf['techops_product']
        cl_id = conf['non-prod_div']
        obj['division_id'] = cl_id
        obj['product_id'] = pr_id
        if 'parent_folder_id' in obj:
            del obj['parent_folder_id']
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
        else:
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
    elif args.divid == "addel":
        pr_id = conf['addel_product']
        cl_id = conf['ad-del_div']
        obj['division_id'] = cl_id
        obj['product_id'] = pr_id
        if 'parent_folder_id' in obj:
            del obj['parent_folder_id']
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
        else:
            json_text = json.dumps(obj)
            Catchpoint().new_test(json_text)
 
