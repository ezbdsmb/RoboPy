from robopy import configs
from flask import Flask, json, request, Response


app = Flask(__name__)


@app.route('/init', methods=['POST'])
def entitiesNames():
    """
    Receives request 'POST/init',
    """

    resp_dict = dict()
    resp_dict['init'] = 'ok'

    resp = Response(json.dumps(resp_dict), status=200)

    return resp


@app.route('/kick', methods=['POST'])
def sentiment():
    """
    Receives request 'POST/sentiment', executes NLP pipeline with mode 'sa',
    responses back with result
    """

    request_json = request.json
    power = request_json['power']
    angle = request_json['angle']

    print(power, angle)

    resp_dict = dict()
    resp_dict['kick'] = 'ok'

    resp = Response(json.dumps(resp_dict), status=200)

    return resp


if __name__ == '__main__':
    app.run(host=configs.DEFAULT_HOST,
            port=configs.DEFAULT_PORT,
            debug=True,
            threaded=True)

