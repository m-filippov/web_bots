from flask import Flask
from flask import request
import datetime
from senders import SentToSkype, SendToTelegram, SendToMail
app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    environment = request.args.get('environment', default='*')
    version = request.args.get('version', default='*')
    changelog = request.args.get('changelog', default='*')
    link = links(environment)
    mesages = create_mesage(environment, version, changelog, link)

    with open('/server_web/send_to.txt', 'r') as f:

       for destin in f:
        SendToMail(mesages, destin)

    SendToTelegram(mesages)
    SentToSkype(mesages)

    return ("work")
def create_mesage(environment, version, changelog, links):


    update_date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    mesage = (environment + ' environment was updated to ' + version + '\n'
              + "Update date:" + update_date + '\n'
              + links + '\n'
              + changelog + '\n'
              + "Click here to view more: https://gitlab.intecracy.com/nectain/ub-app/blob/develop/CHANGELOG.md")
    return mesage

def links(environment):
        return {
        'QA': 'https://app.qa.nectain.com',
        'CPC': 'https://cpc.qa.nectain.com',
        'CPC_Produktion': 'https://caepco.nectain.com/'
}[environment]

if (__name__ == "__main__"):
   app.run(host='0.0.0.0', port=4569)
