#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:                                                                       
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
class articleUpdate:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        str_dateUpdate = web.input(articleId=None,creator=None,createdTime=None,lastUpdatedTime=None,like=None,dislike=None,title=None,typeA=None,sectionsA=None,isPubilc,)
        dicUpdate={}
        userId=str_dateUpdate.userId
        userName=str_dateUpdate.Name
        userPassword=str_dateUpdate.Password
        userEmail=str_dateUpdate.Email
        userRegTime=str_dateUpdate.regTime
        userlastLog=str_dateUpdate.lastLog
        if userId !=None:
           dicUpdate['userId']=userId
        if username!=None:
           dicUpdate['Name']=userName
        if userPassword !=None:
            dicUpdate['Password']=userPassword
        if userEmail!=None:
            dicUpdate['Email']=userEmail
        if userRegTime !=None:
            dicUpdate['regTime']=userRegTime
        if userlastlog !=None:
            dicUpdate['lastLog']= userlastLog
        dbMongo.users.update({"userId":userId},{"$set":dicUpdate})
class articleSave:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        str_dateSave = web.input(userId=None,userName=None,userPassword=None,userEmail=None,userRegTime=None,userlastLog=None)
        dicSave={}
        userId=str_dateSave.userId
        userName=str_dateSave.Name
        userPassword=str_dateSave.Password
        userEmail=str_dateSave.Email
        userRegTime=str_dateSave.regTime
        userlastLog=str_dateSave.lastLog
        if userId !=None:
           dicUpdate['userId']=userId
        if username!=None:
           dicUpdate['Name']=userName
        if userPassword !=None:
            dicUpdate['Password']=userPassword
        if userEmail!=None:
            dicUpdate['Email']=userEmail
        if userRegTime !=None:
            dicUpdate['regTime']=userRegTime
        if userlastlog !=None:
            dicUpdate['lastLog']= userlastLog
        dbMongo.users.Save({dicSave})
class articleDel:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        str_dateDel = web.input(userId=None,userName=None,userPassword=None,userEmail=None,userRegTime=None,userlastLog=None)
        dicDel={}
        userId=str_dateDel.userId
        userName=str_dateDel.Name
        userPassword=str_dateDel.Password
        userEmail=str_dateDel.Email
        userRegTime=str_dateDel.regTime
        userlastLog=str_dateDel.lastLog
        if userId !=None:
           dicUpdate['userId']=userId
        if username!=None:
           dicUpdate['Name']=userName
        if userPassword !=None:
            dicUpdate['Password']=userPassword
        if userEmail!=None:
            dicUpdate['Email']=userEmail
        if userRegTime !=None:
            dicUpdate['regTime']=userRegTime
        if userlastlog !=None:
            dicUpdate['lastLog']= userlastLog
        dbMongo.users.remove({dicDel})
class articleFind:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        str_dateFind = web.input(userId=None,userName=None,userPassword=None,userEmail=None,userRegTime=None,userlastLog=None)
        dicFind={}
        userId=str_dateFind.userId
        userName=str_dateFind.Name
        userPassword=str_dateFInd.Password
        userEmail=str_dateFind.Email
        userRegTime=str_dateFind.regTime
        userlastLog=str_dateFind.lastLog
        if userId !=None:
           dicUpdate['userId']=userId
        if username!=None:
           dicUpdate['Name']=userName
        if userPassword !=None:
            dicUpdate['Password']=userPassword
        if userEmail!=None:
            dicUpdate['Email']=userEmail
        if userRegTime !=None:
            dicUpdate['regTime']=userRegTime
        if userlastlog !=None:
            dicUpdate['lastLog']= userlastLog
        dbMongo.users.Find({dicFind})