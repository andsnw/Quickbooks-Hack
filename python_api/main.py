from quickbooks import Oauth2SessionManager
import quickbooks
import requests
import sys
from flask import Flask, redirect, url_for, request

QUICKBOOKS_CLIENT_KEY = 'Q0bvgCHQyw0f29EhMAkxkPslRVm9UUO3snOWFUFc7w4Ko9C9b8'
QUICKBOOKS_CLIENT_SECRET = 'rRxcrmDaHvivg0GB3NH7gP6dd6lqFabztQoATiML'
QUICKBOOKS_REALM_ID = '123146067417059'

app = Flask(__name__)
session_manager = Oauth2SessionManager(
    client_id=QUICKBOOKS_REALM_ID,
    client_secret=QUICKBOOKS_CLIENT_SECRET,
    base_url='http://localhost:5000',
)

callback_url = 'http://localhost:5000'  # Quickbooks will send the response to this url
authorize_url = session_manager.get_authorize_url(callback_url)


def authorise_me():
    session_manager.get_access_tokens(['code'])
    access_token = session_manager.access_token
    print('Access: ' + access_token)

@app.route("/read")
def read_test():
    authorise_me()
    return "Test"

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)

# def main(args):
#     print (session_manager.get_access_tokens())
#
#     return

# access_token = session_manager.access_token
#
# session_manager = Oauth2SessionManager(
#     client_id=123146067417059,
#     client_secret='rRxcrmDaHvivg0GB3NH7gP6dd6lqFabztQoATiML',
#     access_token=access_token,
# )
#
# client = QuickBooks(
#      sandbox=True,
#      session_manager=session_manager,
#      company_id= 123146067417059
#  )
#
# QuickBooks.enable_global()
