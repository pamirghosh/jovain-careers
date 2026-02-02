from flask import Flask, render_template

app = Flask(__name__)
jobs=[
    {'id':1,
     'title': 'Data Analyst',
     'location':'Bangalore, India',
     'Salary': '10,00000'
     },
     {'id':2,
     'title': 'Backend Engineer',
     'location':'Pune, India',
     'Salary': '20,00000'
     },
     {'id':3,
     'title': 'Data Engineer',
     'location':'Bangalore, India',
     'Salary': '12,00000'
     }
]
@app.route("/")
def hello_world():
    return render_template('index.html', jobs=jobs)
if __name__=="__main__":
    app.run(debug=True)
