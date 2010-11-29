#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import time

import test_base

class Transaction(test_base.Transaction):
    def run(self):
        test_base.Transaction.__init__(self)
        test_base.Transaction.run(self)
        # Siguiendo el enlace para inicio de sesion
        response = self.browser.follow_link(text="Login", nr=0)

        # Formulario de inicio de sesion
        self.browser.select_form(nr=1)
        self.browser.form["user"] = self.user
        self.browser.form["password"] = self.password
        # Inicio del contador
        start_timer = time.time()
        # Enviando la solicitud
        response = self.browser.submit()
        response.read()
        # Lectura del tiempo de solicitud
        latency = time.time() - start_timer
        # Verificamos inicio de sesion
        assert(response.code == 200), 'Bad HTTP Response'
        assert('logged in as' in response.get_data()), 'Text assertion failed'

        # Registro del tiempo de la solicitud
        self.custom_timers['Login'] = latency

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
