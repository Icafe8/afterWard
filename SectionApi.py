#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:                                                                       
#BY                                                                       
#Discription:                                                                       
#                                                                       
#########################################################################
import uuid
import os
import hashlib
import web
import time
import pymongo
import math
import string
import re
import hashlib
import random
Client=pymongo.MongoClient('localhost',27017)
conn=Client.afterWard
class Sections:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        if model.Proving()==1:
            sectionStr=web.input(cover=None)
            conn.section.save({'sectionId':web.config._session.userName+time.strftime('%Y%m%d%H%M%S'),'creator':web.config._session.userName,'content':sectionStr.content,'createdTime':time.strftime('%Y%m%d%H%M%S'),'lastUpdateTime':time.strftime('%Y%m%d%H%M%S'),'like':0,'disLike':0})
            return model.returnJson(1)
        else:
            return(0)
    
    