#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:codeMain.py                                                                                  
#BY yu                                                                       
#Discription:OPen                                                                       
#                                                                       
######################################################################### 
import web
import os
import userApi
import pymongo
import MongodbApi
import ArticleApi
import SectionApi
#import dbMongoApi
#import sys 
#default_encoding = 'utf-8' 
#if sys.getdefaultencoding() != default_encoding: 
#    reload(sys) 
#    sys.setdefaultencoding(default_encoding)
Client=pymongo.MongoClient('localhost',27017)
conn=Client.afterWard
#web.config.debug = False
urls = (
    '/','index',
    '/mars/signup', 'userApi.signUp',
    '/mars/signin', 'userApi.signIn',
    '/mars/signout','userApi.signOut',
    '/mars/datebase','MongodbApi.mongoDate',
    '/mars/article/(.+)','ArticleApi.Articles',
    '/mars/section'  , 'SectionAPi.Sections',
    "/set", "CookieSet",
    "/get", "CookieGet",
    "/session","sessions",
    "/mars","index",
    "/mars/user","userApi.userData"
)
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'temp')
render = web.template.render(templates_root)
class CookieSet:
        def GET(self):
                web.setcookie("age", "23", 10)
                return "Your cookie is create"

class CookieGet:
        def GET(self):
                try:
                        return "Your age is : " + web.cookies().age
                except:
                        return "Your cookie doesn't exists"
class index:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        return self.render.test1()
    def POST(self):
        dic=web.input()
        #dic.pop("action")
        
        return dic
class sessions:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        return web.config._session.logIn

#    session = web.session.Session(app, web.session.DiskStore('sessions'))
    
#    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
#    def session_hook():
#        web.ctx.session = session
#    app.add_processor(web.loadhook(session_hook))##print web.ctx.session.xxx
app = web.application(urls, globals())
if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'logIn':'False','userName':None})
    web.config._session = session
else:
    session = web.config._session
if __name__ == "__main__":
    
    app.run()
    