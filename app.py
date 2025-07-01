from flask import Flask, render_template, request
app = Flask(__name__)

kinoko_count=3
takenoko_count=5
message=['kinoko is wonderfull', 'Takenoko is awesome!']

@app.route('/')
def top():
    return render_template('index.html', **vars())

import re
@app.route('/vote', methods=['POST'])
def answer():
    global kinoko_count, takenoko_count, messages
    if request.form.get("item")=='kinoko':
        kinoko_count +=1
    elif request.form.get("item")=='takenoko':
        takenoko_count +=1

    message.append(request.form.get("message"))
    if len(message) > 3:
        message=message[-3:]
        
    kinoko_percent=kinoko_count / (kinoko_count + takenoko_count) *100
    takenoko_percent=takenoko_count / (kinoko_count + takenoko_count) *100
    message_html=''
    for i in range(len(message)):
        message=message[i]
        message=re.sub(r'&', r'&amp;', message)
        message=re.sub(r'<', r'&It;', message)
        message=re.sub(r'>', r'&gt;', message)
        message_html +='<div class="alert {1}" role="alert">{0}</div>\n'.format(message, 'alert-warning ms-5' if i % 2==0 else 'alert-sucess me-5')
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
