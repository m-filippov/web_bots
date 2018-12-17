import os
import re
import requests

test = 'test'
version = 'version'


def get_chandgelog_version(patch_to_changelog, patch_to_json):
    with open(patch_to_changelog, 'r') as file:
         filedata = file.read(3000)

    filedata = filedata.replace('\n', '%0a')
    changelog = re.sub('[#*]', '', filedata)
    w = 'version'
    with open(patch_to_json, 'r') as f:
        for line in f:
            if w in line:
                reg = re.compile('[^0-9v.-]')
                version = reg.sub('', line)
    send_to = ("'m_tech@ex.ua', 'xmelayx@gmail.com', 'maksym.fillipov@softengi.com'")
   # targets = send_to.split(",")
    return changelog, version



def send_http():
    changelog, my_version = get_chandgelog_version(test, version)
    r = requests.get('http://localhost:4569/test?environment=CPC_Produktion&version=' + my_version + '&changelog=' + changelog)
    r.status_code
    print r


send_http()
