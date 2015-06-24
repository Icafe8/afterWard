#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:                                                                       
#BY                                                                       
#Discription:                                                                       
#                                                                       
##########################################################################!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:userApi.py                                                                       
#BY  yu                                                                     
#Discription: userAPI                                                                      
#                                                                       
#########################################################################
import uuid
import os
import hashlib
import web
import time
import pymongo
import model
import re
import random
######################################################singup###################################################################################
Client=pymongo.MongoClient('localhost',27017)
conn=Client.afterWard
class signUp:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        return self.render.sign_up()
    def POST(self):
        strSignUp = web.input()
        #userMobile = str_singUp.Mobile
        userEmail = strSignUp.email
        userPassword=strSignUp.password
        userKeyMd5 = hashlib.new("md5",userPassword).hexdigest()
        #userToken = str_Reg_One.Token
        #Key_Reg1= userMobile + str(Token)
        ruleEmail="[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
        #ruleMobile="^[0-9]{11}$"
        rulePassword="^[\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]{6,22}$"
        #RegexToken="^[0-9]{4}$"
        userID=str(uuid.uuid1())
        if (re.match(ruleEmail,userEmail) and re.match(rulePassword,userPassword)):
            #userC=conn.users.find_one({"Email":userEmail},{"Email":1,"_id":0})
            if conn.users.find_one({"email":userEmail},{"email":1,"_id":0}) is None:
                conn.users.insert({'password':userKeyMd5,'email':userEmail,'userId':userID,'isActive':0,'createdTime':time.strftime('%Y%m%d%H%M%S'),'sex':None,'mobile':None,'lastLoginedTime':None,'name':None,'avatar':None,'description':None})
                return model.returnJson(1)
            else:
                return model.returnJson(0)
        else:
            return model.returnJson(0)
#######################################################################################################
#            sqlsingUp='insert into User2(Password,Email) values("%s","%s")' %(userPassword,userEmail)
#            sqlEmail = 'select Mobile from User2 where Email='+"'"+userEmail +"'"
###########################SAE db######################################################################
#            conn= MySQLdb.connect(
#            host=sae.const.MYSQL_HOST,
#            port = int(sae.const.MYSQL_PORT),
#            user=sae.const.MYSQL_USER,
#            passwd=sae.const.MYSQL_PASS,
#            db =sae.const.MYSQL_DB,
#            charset='utf8'
#            )
#            cur=conn.cursor()
#            cur.execute(SqlTel)
#            rMobile=cur.fetchone()
#            cur.close()
#######################################################################################################
########################################signIn#########################################################
#######################################################################################################
class signIn:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
#        str_signIn = web.input()
#        userEmail = str_signIn.email
#        #传入参数 userID 以此判断是否登录以及是否激活
#        userActive=conn.users.find_one({"Email":userEmail},{"isActive":1,"_id":0})
#        if userActive =={}:
#            return "NOt OK"
#        if userActive["isActive"]=="1":
#            return "ok"
#        else:
#            return "NOt OK"
#        return "Not OK"
        return self.render.sign_up()
    def POST (self):
        strSignIn = web.input()
        userEmail=strSignIn.email
        dbUserDate=conn.users.find_one({"email":userEmail},{"_id":0})
        #userToken= str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        try:
            if dbUserDate["password"] == hashlib.new("md5",strSignIn.password).hexdigest():
                web.config._session.logIn=1
                web.config._session.userName=userEmail
                #web.setcookie('toKen',userToken)
                #web.ctx.session.Id=userId 
                #return dbUserDate["userID"]
                return model.returnJson(1,dbUserDate)
            else:
                return model.returnJson(0)
        except:
            return model.returnJson(0)
        
############################################logout########################################
class signOut:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        #logOutId=web.input().userId
        if model.Proving()==1:
            try:
                web.config._session.logIn=0
                web.config._session.Kill()
                conn.users.update({"userId":logOutId},{'$set':{"lastloginedTime":time.strftime('%Y%m%d%H%M%S')}})
            except:
                pass
            return model.returnJson(1)
        else:
            return model.returnJson(0)
###########################################################################################
###############################isActive####################################################
class Active:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        pass
    def POST (self):
        pass
        
class userData:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self):
        userName=web.config._session.userName
        dbUserDate=conn.users.find_one({"email":userName},{"_id":0})
        return model.returnJson(1,dbUserDate)
    def POST (self):
        strUserData = web.input(sex=None,mobile=None,name=None,avatar=None,description=None)
        edit={}
        if strUserData.sex !=None:
            edit['sex']=int(strUserData.sex)
        if strUserData.mobile !=None:
            edit['mobile']=strUserData.mobile 
        if strUserData.name !=None:
            edit['name']=strUserData.name
        if strUserData.description !=None:
            edit['description']=strUserData.description
        if strUserData.avatar !=None:
            edit['avatar']=strUserData.avatar
        #return edit
        try:
            conn.users.update({'email':web.config._session.userName},{'$set':edit})
            dbUserData=conn.users.find_one({"email":web.config._session.userName},{"_id":0})
            return model.returnJson(1,dbUserData)
        except:
            return model.returnJson(0)
        
        