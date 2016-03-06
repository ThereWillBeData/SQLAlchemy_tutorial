# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:45:20 2016

@author: adam
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
res = session.query(Artist).filter(Artist.name=="MXPX").first()
 
session.delete(res)
session.commit()
res = session.query(Artist).filter(Artist.name=="MXPX").first()
 
session.delete(res)
session.commit()