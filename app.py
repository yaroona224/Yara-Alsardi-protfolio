from flask import Flask,render_template
app=Flask(__name__)
projects = [
{'id':1,
 'project' : 'Web Scrapping',
'skills' : 'urllib python, python requests, selenium'
},
{'id':2,
 'project' : 'AI model for flare mointoring',
'skills' : 'pthyon pandas, microsft azure, python, pychatgpt'},
{'id':3,
 'project' : 'Energy innovation',
'skills' : 'python, flask, html, css, javascript, bootstrap'}
]

@app.route('/')
def hello_world():
  return render_template('home.html', myskills = projects,
                        myname = 'Yara')
  
if __name__=='__main__':
  app.run(host="0.0.0.0",port=True)#run flask server