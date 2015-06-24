#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name: MongodbApi.py                                                                      
#BY                                                                       
#Discription:                                                                       
#                                                                       
#########################################################################
import os
import hashlib
import web
import time
import pymongo
import math
import string
import hashlib
import random
Client=pymongo.MongoClient('localhost',27017)
dbMongo=Client.afterWard
class mongoDate():
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        Gather=web.input().Gather
        Action=web.input().Action
        State=web.input().State
        if web.ctx.session.longIn==False:
        
            if Gather=="users":#user 
                if Action=="1":#save
                    mongoS="dbMongo.users.save(%s)" %State
                    eval(mongoS)
                    return 1
                elif Action=="2":#del
                    mongoD="dbMongo.users.remove(%s)" %State
                    eval(mongoD)
                    return 1
                elif Action=="3":#update
                    mongoU="dbMongo.users.update(%s)" %State
                    eval(mongoU)
                    return 1
                elif Action=="4":#Find
                    result=[]
                    mongoF="dbMongo.users.find(%s)" %State
                    for x in eval(mongoF) :
                        result.append(x)
                    return result
                else:
                    return -1
                        
            elif Gather=="article":#save
                if Action=="1":#save
                    mongoS="dbMongo.user.save(%s)" %State
                    eval(mongoS)
                    return 1
                elif Action=="2":#del
                    mongoD="dbMongo.user.remove(%s)" %State
                    eval(mongoD)
                    return 1
                elif Action=="3":#update
                    mongoU="dbMongo.user.update(%s)" %State
                    eval(mongoU)
                    return 1
                elif Action=="4":
                    result=[]
                    mongoF="dbMongo.user.find(%s)" %State
                    for x in eval(mongoF):
                        result.append(x)
                    return result
                else:
                    return -1
        else:
            return "NOt log"
                

            
        