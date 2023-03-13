import os

from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_frontend():
    # open a connection to a URL using urllib2
   #webUrl = urllib.request.urlopen("https://www.youtube.com/user/guru99com")
    webUrl = requests.get("https://cr-demo-backend-6mckjolnxq-el.a.run.app")
  
#get the result code and print it
    print ("result code: " + str(webUrl.status_code))
  
# read the data from the URL and print it
    data = webUrl.text
    print (data)
    return "This frontend service calling another service with message - {}!".format(data)

@app.route("/external")
def test_external():
    # open a connection to a URL using urllib2
   #webUrl = urllib.request.urlopen("https://www.youtube.com/user/guru99com")
    webUrl = requests.get("https://www.google.com/")
  
#get the result code and print it
    print ("result code: " + str(webUrl.status_code))
  
# read the data from the URL and print it
    data = webUrl.text
    print (data)
    return "external call from the frontendservice is - {}!".format(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8088)))

# def main():
# # open a connection to a URL using urllib2
#    webUrl = urllib.request.urlopen("https://www.youtube.com/user/guru99com")
  
# #get the result code and print it
#    print ("result code: " + str(webUrl.getcode())) 
  
# # read the data from the URL and print it
#    data = webUrl.read()
#    print (data)
 
# if __name__ == "__main__":
#   main()