#!/usr/bin/python2.7

# http://toast.bottombutton.net/api?activity=on&key=5TKM3A9I44YRV6UMR0ZS
# http://toast.bottombutton.net/api?activity=off&key=5TKM3A9I44YRV6UMR0ZS
# http://toast.bottombutton.net/api?activity=reset&key=5TKM3A9I44YRV6UMR0ZS

import cherrypy
from models import *
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('/toast/views'))

class Toast(object):
    def __init__(self):
        self.service = service.service('count.txt')

    @cherrypy.expose
    def index(self):
        template = env.get_template('template.html')
        data = page.page(self.service)
        return template.render(color=data.color(), answer=data.answer(), count=data.count(), started=data.date())

    @cherrypy.expose
    def api(self, activity=None, key=None):
        if activity.lower() == 'get':
            return self.service.get()
        elif activity.lower() == 'on':
            return self.service.on(key=key)
        elif activity.lower() == 'off':
            return self.service.off(key=key)
        elif activity.lower() == 'reset':
            return self.service.reset(key=key)
        else:
            return response.response(response.ERROR, 'Invalid activity.').json()

if __name__ == '__main__':
    cherrypy.config.update('global.config')
    cherrypy.quickstart(Toast(), '/', config='resources.config')
