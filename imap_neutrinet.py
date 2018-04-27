#!/usr/bin/env python3

from imapclient import IMAPClient


class ImapNeutrinet:
    host = ""

    def __init__(self, host):
        self.host = host

    def move_mail(self, email, password, mails_spam):
        with IMAPClient(host=self.host, ssl=True) as client:

            client.login(email, password)
            client.select_folder('INBOX')

            for mail_spam in mails_spam:
                messages = client.search(
                    [
                        'NOT',
                        'DELETED',
                        'SUBJECT',
                        mail_spam['mail_subject'].encode('utf-8'),
                        'FROM',
                        mail_spam['mail_from'].encode('utf-8')
                    ]
                )

                response = client.fetch(messages, ['ENVELOPE'])

                for message_id, data in response.items():
                    client.move(message_id, 'Junk')
