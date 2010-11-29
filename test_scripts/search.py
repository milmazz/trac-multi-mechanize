#!/usr/bin/env python
# -* coding: utf-8 -*-

import mechanize
import time

import login

class Transaction(login.Transaction):
    def run(self):
        login.Transaction.__init__(self)
        login.Transaction.run(self)
        
        response = self.browser.follow_link(text="Search", nr=1)
        assert(response.code == 200), 'Bad HTTP Response'
        assert('Trac Search' in response.get_data()), 'Text Assertion Failed'

        # Formulario de busqueda
        self.browser.select_form(nr=1)
        self.browser.form["q"] = "trac"
        self.browser.form["milestone"] = False 
        self.browser.form["doxygen"] = False
        self.browser.form["ticket"] = True
        self.browser.form["changeset"] = False
        self.browser.form["wiki"] = True

        start_timer = time.time()

        response = self.browser.submit()
        response.read()
        
        latency = time.time() - start_timer

        assert(response.code == 200), 'Bad HTTP Response'
        assert('Trac' in response.get_data()), 'Text Assertion Failed'

        self.custom_timers['Search'] = latency

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
