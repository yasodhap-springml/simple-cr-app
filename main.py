import os

from flask import Flask
from google.cloud import bigquery
from google.auth.transport import requests
from google.oauth2 import id_token


app = Flask(__name__)

@app.route("/backend")
def receive_authorized_get_request(request):
    
    auth_header = request.headers.get("Authorization")
    if auth_header:
        # split the auth type and value from the header.
        auth_type, creds = auth_header.split(" ", 1)

        if auth_type.lower() == "bearer":
            claims = id_token.verify_token(creds, requests.Request())
            return f"Hello, {claims['email']}!\n"

        else:
            return f"Unhandled header format ({auth_type}).\n"
    return "Hello, anonymous user.\n"

@app.route("/callbq")
def hello_world():
    name = call_bq()  + '. This is Backend Service'
    print(name)
    return "Hello {}!".format(name) 

def call_bq():
    client = bigquery.Client()
    query = """
    SELECT * FROM `ashwani-21apr-22-scrumteam.cr_demo_dataset.cr_demo_table` LIMIT 1
        """
    query_job = client.query(query)  
    for row in query_job:
        row_name = row.name
        #row_list.append(row_name)
        return row_name

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
