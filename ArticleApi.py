#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:ArticleApi.py                                                                       
#BY                                                                       
#Discription:                                                                       
#                                                                       
#########################################################################
import os
import hashlib
import web  
import time
import pymongo
import hashlib
import model
import json
import uuid
#import sys
#reload( sys )
#sys.setdefaultencoding('utf-8')
Client=pymongo.MongoClient('localhost',27017)
conn=Client.afterWard
class Articles:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'temp')
        self.render = web.template.render(self.templates_root)
    def GET (self,urlId):
        #conn.articlePage
        if urlId is None:
            listArticle={}
            reArticle=[]
            try:
                for x in conn.article.find():
                    listArticle['articleId']=x['articleId']
                    listArticle['title']=x['title']
                    listArticle['creator']=x['creator']
                    listArticle['cover']=x['cover']
                    listArticle['isPublic']=x['isPublic']
                    listArticle['createdTime']=x['createdTime']
                    listArticle['lastUpdateTime']=x['lastUpdateTime']
                    listArticle['like']=x['like']
                    listArticle['disLike']=x['disLike']
                    listArticle['creator']=x['creator']
                    listArticle['type']=x['type']
                    reArticle.append(listArticle)
                    #reDate={"status":1,"date":reArticle}
                    #web.header('Content-Type','text/json; charset=utf-8', unique=True)
                return model.returnJson(1,reArticle)
            except:
                listArticle['articleId']=x['articleId']
                listArticle['title']=x['title']
                listArticle['creator']=x['creator']
                listArticle['cover']=x['cover']
                listArticle['isPublic']=x['isPublic']
                listArticle['createdTime']=x['createdTime']
                listArticle['lastUpdateTime']=x['lastUpdateTime']
                listArticle['like']=x['like']
                listArticle['disLike']=x['disLike']
                listArticle['creator']=x['creator']
                listArticle['type']=x['type']
                return model.returnJson(1,listArticle)
        else:
            reSignleArticle={}
            s=conn.article.find_one({'articleId':urlId})
            reSignleArticle['articleId']=s['articleId']
            reSignleArticle['title']=s['title']
            reSignleArticle['creator']=s['creator']
            reSignleArticle['cover']=s['cover']
            reSignleArticle['isPublic']=s['isPublic']
            reSignleArticle['createdTime']=s['createdTime']
            reSignleArticle['lastUpdateTime']=s['lastUpdateTime']
            reSignleArticle['like']=s['like']
            reSignleArticle['disLike']=s['disLike']
            reSignleArticle['creator']=s['creator']
            reSignleArticle['type']=s['type']
            #reDateS={"status":1,"date":reSignleArticle}
            #return reSignleArticle[2] 
            return model.returnJson(1,reSignleArticle)
    def POST (self):
        #conn.Article.save({'ArticleID':web.config._session.userName+time.strftime('%Y%m%d%H%M%S'),'Title':articleStr.Title,'Cover':articleStr.Cover,'Creator':web.config._session.userName,'isPubilc':articleStr.isPubilc,'Content':articleStr.Content,'createdTime':time.strftime('%Y%m%d%H%M%S'),'lastUpdateTime':time.strftime('%Y%m%d%H%M%S'),'Like':0,'disLike':0,'Type':'1'})
        #return '1'
        #return articleStr.Title
        if model.Proving()==1:
            articleStr=web.input(cover=None,section=None,title=None,content=None,isPublic=None)
            #conn.Article.save({'articleId':web.config._session.userName+time.strftime('%Y%m%d%H%M%S'),'title':articleStr.title,'content':articleStr.content,'section':articleStr.section,'cover':articleStr.cover,'creator':web.config._session.userName,'isPublic':articleStr.isPubilc,'createdTime':time.strftime('%Y%m%d%H%M%S'),'lastUpdateTime':time.strftime('%Y%m%d%H%M%S'),'like':0,'disLike':0,'type':None,'authors':None})
            #return model.returnJson(0)
            try:
                articleId=str(uuid.uuid1())
                conn.article.save({'articleId':articleId,'title':articleStr.title,'section':articleStr.section,'cover':articleStr.cover,'creator':web.config._session.userName,'isPublic':articleStr.isPublic,'createdTime':time.strftime('%Y%m%d%H%M%S'),'lastUpdateTime':time.strftime('%Y%m%d%H%M%S'),'like':0,'disLike':0,'type':None,'authors':None})
                conn.section.save({'sectionId':str(uuid.uuid1()),'creator':web.config._session.userName,'content':articleStr.content,'createdTime':time.strftime('%Y%m%d%H%M%S'),'lastUpdateTime':time.strftime('%Y%m%d%H%M%S'),'like':0,'dislike':0})
                return model.returnJson(1,{'articleId':articleId})
            except:
                return model.returnJson(0,"DatabaseErro")
        else:
            return model.returnJson(0,'Not Log')

    
