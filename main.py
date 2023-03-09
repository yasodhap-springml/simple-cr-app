import os

from flask import Flask
from google.cloud import bigquery

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")  + '. This is Backend Service'
    call_bq()
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
        print(row_name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
