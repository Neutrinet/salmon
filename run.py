#!/usr/bin/env python3
import json
from api_zammad import ApiZammad
from imap_neutrinet import ImapNeutrinet

config = json.load(open('config.json'))

api = ApiZammad(url=config['api_zammad']['url'], token=config['api_zammad']['token'])
imap = ImapNeutrinet('mail.neutri.net')

for mail_account in config['mail_accounts']:
    mails_spam = api.get_list_spam(mail_account['email'])
    imap.move_mail(mail_account['email'], mail_account['password'], mails_spam)
