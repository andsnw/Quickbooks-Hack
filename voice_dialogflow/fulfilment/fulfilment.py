from flask import Flask, request, redirect, url_for,jsonify
import sys
import os
import json
import re
import requests
app = Flask(__name__)

json_response = {
    "fulfillmentText": "Hello world response",
}

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/f', methods=["GET", "POST"])
def fulfilme():
    if request.method == "POST" and request.headers['Content-Type'] == 'application/json':
        request_data = request.json
        if "action" in request_data["queryResult"].keys():
            if request_data["queryResult"]["action"] == "request_permission":
                print "recieved request for permission"
                return jsonify(request_location())
        params = request_data["queryResult"]["parameters"]
        print json.dumps(request_data, indent=4)
        return 'Hi'
    return "Hello World!"

def request_location():
    location_req =  {
        'payload': {
        'google': {
            'expect_user_response': True,
            'is_ssml': False,
            'no_input_prompts': [],
            'richResponse': {
                'items': [
                    {
                    'simpleResponse': {
                        'textToSpeech': 'hello',
                        'displayText': 'hi'
                    }
                    }
                ],
                'suggestions': [
                    {
                    'title': 'Say this'
                    },
                    {
                    'title': 'or this'
                    }
                ]
            },
            'system_intent': {
                'intent': 'actions.intent.PERMISSION',
                'data': {
                    "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
                    "optContext": "For better a better accounting experience",
                    "permissions": [
                        "NAME",
                        "DEVICE_PRECISE_LOCATION"
                    ]
                }
            }
        }
    },

    }
    return location_req

# TODO: This, we forward the params iteratively i.e. after every dialogue
#       that is parsed from df
def forward_params(fufillment_params):
    json_payload = jsonify(fufillment_params)
    pass

if __name__ == "__main__":
    app.run(debug=True)
