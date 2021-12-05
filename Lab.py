# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:42:51 2019

@author: Administrator
"""

from flask import Flask, request
from UseSqlite import InsertQuery, RiskQuery
from datetime import datetime
from PIL import Image
from module import bpModule
from module import make_html_paragraph,get_database_photos

app=Flask(__name__)
app.register_blueprint(bpModule,ure_prefix='/bpModule')


@app.route('/',methods=['POST','GET'])
def main():
    if request.method=='POST':
        uploaded_file=request.files['file']
        time_str=datetime.now().strftime('%Y%m%d%H%M%S')
        new_filename=time_str+'.jpg'
        uploaded_file.save('./static/upload/'+new_filename)
        time_info=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        description=request.form['description']
        path='./static/upload/'+new_filename
        iq=InsertQuery('./static/RiskDB.db')
        iq.instructions("INSERT INTO photo Values('%s','%s','%s','%s')"%(time_info,description,path,new_filename))
        iq.do()
        return '<p>You have uploaded %s.<br/> <a href="/">Return</a>.'%(uploaded_file.filename)
    else:
        page='''<form action="/"method="post"enctype="multipart/form-data">
        <input type="file"name="file"><input name="description"><input type="submit"value="Upload"></form>'''
        page+=get_database_photos()
        return page
    
if __name__=='__main__':
    app.run(debug=True)