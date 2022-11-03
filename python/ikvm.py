#!python3
import argparse
import requests
import urllib3
import getpass
import sys
from requests.auth import HTTPBasicAuth

DEFAULT_USERNAME = 'ADMIN'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', action='store', required=True)
    parser.add_argument('--username', action='store', default=DEFAULT_USERNAME)
    parser.add_argument('--password', action='store', required=False)

    args = parser.parse_args()

    print('Authenticating with username: {}'.format(args.username))

    if args.password:
        password = args.password
    else:
        password = getpass.getpass()

    # disable insecure request warning
    # from https://techoverflow.net/2019/07/09/how-to-disable-insecurerequestwarning-unverified-https-request-is-being-made/
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    headers = {'Accept': 'application/json'}
    auth = HTTPBasicAuth(args.username, password)
    url = 'https://{}/redfish/v1/Managers/1/IKVM'.format(args.hostname)
    response = requests.get(url, headers=headers, auth=auth, verify=False)
    if response.status_code != 200:
        print(response.reason)
        sys.exit(-1)

    result = response.json()
    ikvm_url = 'https://{}{}'.format(args.hostname, result.get('URI'))
    print('iKVM URL: {}'.format(ikvm_url))
