from flask import Flask, request, make_response, jsonify
from hieroglyph_calculator import time_hieroglyphs
from cotroller import Message
from flask_expects_json import expects_json
from jsonschema import ValidationError
import werkzeug


app = Flask(__name__)

schema = {
    "hours": {"type": "int"},
    "minutes": {"type": "int"}
}


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_internal_server_error(error):
    return 'Internal server error!\n', 500

app.register_error_handler(500, handle_internal_server_error)

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(error):
    return 'Bad request!\n', 400

app.register_error_handler(400, handle_bad_request)


@app.route('/')
def home():
    return "Hello, stranger"

@app.route('/about')
def about():
    return "Simple API webapp"


@app.post('/test')
def test():
    data = request.get_json()

    print(data)
    return data, 200

@app.post('/api/sum')
def calc_sum():
    data = request.get_json()
    x = data["x"]
    y = data["y"]
    return {"result": f"{x + y}"}, 200


@app.post("/time")
@expects_json(schema)
def time_glyphs():
    if request.is_json:
        data = request.get_json()
        hours = data["hours"]
        minutes = data["minutes"]
        hieroglyphs = time_hieroglyphs(hours=hours, minutes=minutes)
        return {"hieroglyph1":hieroglyphs[0], "hieroglyph2":hieroglyphs[1]}, 200


@app.post("/date")
def date_glyphs():
    pass

@app.post("/month")
def month_glyphs():
    pass


@app.post("/year")
def year_glyphs():
    pass


@app.post("/complete_date")
def complete_date_glyphs():
    pass

