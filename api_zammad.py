#!/usr/bin/env python3
import requests
from pprint import pprint


class ApiZammad:

    url = ''
    token = ''

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_list_spam(self, email):
        mails_spam = []

        list_tickets = requests.get(self.url + '/api/v1/tickets/search?query=tag: spam AND state:closed AND article.to: %s&limit=100&expand=true' % email, headers={'Authorization': 'Token token=' + self.token})

        for list_ticket in list_tickets.json():
            for article_id in list_ticket['article_ids']:

                article = requests.get(self.url + '/api/v1/ticket_articles/%s' % article_id, headers={'Authorization': 'Token token=' + self.token})
                data = article.json()
                if data['type'] == 'email':
                    mails_spam.append({'mail_from': data['created_by'], 'mail_subject': data['subject']})

        return mails_spam
