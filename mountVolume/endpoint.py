from flask import Flask, request
import sqlInterface

app = Flask(__name__)
serverExec = sqlInterface.SQLInterface()

@app.route('/select/', methods=['POST'])
def select():
    print("on select!!!")
    payload = request.json
    print("name = " + str(payload))
    print("name type = " + str(type(payload)))

    rows = serverExec.select(
        payload['target'],
        payload['table'],
        payload['where']
        )

    for row in rows:
        print(row)

    return str(rows)


@app.route('/insert/', methods=['POST'])
def insert():
        
    payload = request.json
    print("name = " + str(payload))
    print("name type = " + str(type(payload)))


    try:
        serverExec.insert(
            payload['data'],
            payload['table']
            )

        return "success to add data" + str(payload)
    except Exception as e:
        return "error:" + str(e)

    


if __name__ == "__main__":


    app.run(host='127.0.0.1')


