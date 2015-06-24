#!/usr/bin/env python
# coding: utf-8
#########################################################################
#Name:Model.py                                                                       
#BY                                                                       
#Discription:                                                                       
#                                                                       
#########################################################################
import json
import web
def  Proving():
    try:
        if web.config._session.logIn == 1:
            return 1
        else:
            return 0
    except:
        return 0
def returnJson (reStu=0,reDate=[]):
      web.header('Content-Type','text/json; charset=utf-8', unique=True)
      return json.dumps({'status':reStu,'data':reDate})

    
    
    