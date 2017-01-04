import os
from paramiko.py3compat import StringIO
from paramiko import SSHConfig
import yaml


def getCompany(hostname):
    splitName = hostname.split('-')
    if len(splitName) > 1:
        return splitName[0]
    return DEFAULTCOMPANY


DEFAULTCOMPANY = "otros"
config = SSHConfig()

companys = {}

configFile = open('config', 'r')
configText = configFile.read()
config.parse(StringIO(configText))

for item in config._config:

    # if the host has config
    if item['config']:
        company = getCompany(item['host'][0])

        if company not in companys:
            companys[company] = {'hosts': {}}

        hostname = item['host'][0]
        companys[company]['hosts'][hostname] = item['config']

for company in companys:
    with open(company + '.yml', 'w') as outfile:
        yaml.dump(companys[company], outfile, default_flow_style=False)
