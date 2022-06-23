from flask import Flask, request
from exec_scripts import dialog

app = Flask(__name__)
serverExec = dialog.serverExec()

@app.route('/', methods=['POST'])
def conversation():
        
    payload = request.json
    line = payload
 #    line = payload.get('request')
    print("name = " + str(line))
    print("name type = " + str(type(line)))

    ret = serverExec.main(line)
    print("ret =" + str(ret))
    return ret


if __name__ == "__main__":


    app.run(host='0.0.0.0')

