#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:                                                                       
#BY                                                                       
#Discription:                                                                       
#                                                                       
#########################################################################
import pymongo
import aweb
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

