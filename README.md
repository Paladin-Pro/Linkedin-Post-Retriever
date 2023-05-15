Obtain a LinkedIn Access Token:

Go to the LinkedIn Developer Dashboard and create a new app if you haven't already done so.
Navigate to the app's "Auth" tab and note down the "Client ID" and "Client Secret".
Go to the following URL in your web browser:
    **https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=<client-id>&redirect_uri=<redirect-uri>&state=<state>&scope=r_liteprofile%20r_emailaddress%20w_member_social**

Replace <client-id> with your LinkedIn app's "Client ID".
Replace <redirect-uri> with your app's "OAuth 2.0 Redirect URLs" or any other URL that you want to redirect to after the user grants access.
Replace <state> with any random string that you want to use to validate the authenticity of the response.
Log in to your LinkedIn account and grant access to your app when prompted.
LinkedIn will redirect you to the <redirect-uri> with a code parameter in the URL. Note down this code.
Use the following code to exchange the code for an access token:
    data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
    }
    response = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data=data)
    access_token = response.json()['access_token']
    
Replace code with the code that you obtained in the previous step.
Replace redirect_uri, client_id, and client_secret with the corresponding values from your LinkedIn app.
Store the LinkedIn Access Token:

Save the access_token variable to a file or an environment variable.
If you choose to save the access token to a file, you can use the following code to read the access token from the file:

    with open('access_token.txt', 'r') as f:
        access_token = f.read().strip()

If you choose to save the access token to an environment variable, you can use the following code to read the access token from the environment variable:
    import os
access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')


