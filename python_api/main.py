from quickbooks import Oauth2SessionManager
import quickbooks


session_manager = Oauth2SessionManager(
    client_id=Q0bvgCHQyw0f29EhMAkxkPslRVm9UUO3snOWFUFc7w4Ko9C9b8,
    client_secret=rRxcrmDaHvivg0GB3NH7gP6dd6lqFabztQoATiML,
    base_url='http://localhost:3000',
)

callback_url = 'http://localhost:3000'  # Quickbooks will send the response to this url
authorize_url = session_manager.get_authorize_url(callback_url)

session_manager.get_access_tokens(request.GET['code'])
access_token = session_manager.access_token

session_manager = Oauth2SessionManager(
    client_id=123146067417059,
    client_secret=rRxcrmDaHvivg0GB3NH7gP6dd6lqFabztQoATiML,
    access_token=access_token,
)

client = QuickBooks(
     sandbox=True,
     session_manager=session_manager,
     company_id= 123146067417059
 )

QuickBooks.enable_global()
