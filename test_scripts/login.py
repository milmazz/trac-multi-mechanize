#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import time

class Transaction():
    def __init__(self):
        self.custom_timers = {}
        # URL del sitio
        self.site = "http://trac.example.com/project"
        self.user = "username"
        self.password = "password"
        # Creando una instancia de navegacion
        self.browser = mechanize.Browser()
        # Ignorando robots.txt
        self.browser.set_handle_robots(False)
        # Agregando una cabecera particular para evitar problemas
        # en las solicitudes
        self.browser.addhandlers = [('User-agent', 'Mozilla/5.0 Compatible')]

    def run(self):
        # Iniciando nuestra primera solicitud
        # Iniciando el contador
        start_timer = time.time()
        # Enviando la solicitud
        response = self.browser.open(self.site)
        response.read()
        # Lectura del tiempo de la solicitud
        latency = time.time() - start_timer
        # Almacenamiento del tiempo
        self.custom_timers['Carga_Sitio'] = latency
        # Verificamos si la respuesta es correcta
        assert(response.code == 200), 'Bad HTTP Response'
        assert('Trac Powered' in response.get_data()), 'Text Assertion Failed'

        time.sleep(2) # Pensamos que hacer

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
