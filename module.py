# -*- coding: utf-8 -*-

from flask import Blueprint,request
from UseSqlite import InsertQuery,RiskQuery
from PIL import Image
from datetime import datetime

bpModule = Blueprint('bpModule',__name__)

def make_html_paragraph(s):
    if s.strip()=='':
        return ''
    lst=s.split(',')
    picture_path=lst[2].strip()
    picture_name=lst[3].strip()
    im = Image.open(picture_path)
    im.thumbnail((400, 300))
    im.save('./static/figure/'+picture_name, 'png')
    result='<p>'
    result+='<i>%s</i><br/>'%(lst[0])
    result+='<i>%s</i><br/>'%(lst[1])
    result+='<a href=".%s"><img src="../static/figure/%s"alt="风景图"></a>'%(picture_path,picture_name)
    return result+'</p>'

#通过关键字查找图片
def serach_database_photos(photoname):
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo where description like'%%%%%s%%%%'" %photoname)
    rq.do()
    record='<p>My search photo</p>'
    for r in rq.format_results().split('\n\n'):
        record+='%s'%(make_html_paragraph(r))
    return record+'</table>\n'

#在数据库中获取图片
def get_database_photos():
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    record='<p>My past photo</p>'
    for r in rq.format_results().split('\n\n'):
        record+='%s'%(make_html_paragraph(r))
    return record+'</table>\n'

#搜索蓝图
@bpModule.route("/search/<photoname>")
def search_pb(photoname):
    page=''' '''
    page+=serach_database_photos(photoname)
    return page

#上传蓝图
@bpModule.route("/upload",methods=['POST','GET'])
def upload_pb():
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
        return page

#显示图片蓝图
@bpModule.route("/show")
def show_pb():
    page=get_database_photos()
    return page