Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call. Do not advise your teammate to use your test program or require them to, your teammate must write all of their own code.

The service is hosted on http://127.0.0.1:5000
The endpoint to request random quote is /get-quote


To request the data make a GET request. Response will be in JSON format. 
Use the library requests in Python to send the GET request.
![image](https://github.com/user-attachments/assets/83d2e702-33fa-47ec-8504-5352446140da)



Clear instructions for how to programmatically RECEIVE data from the microservice you implemented. Include an example call. 

Recieving data will be in JSON format. The key for the quote in the JSON is "quote"
Once the HTTP request is recieved, you will recieve the data as part of the HTTP response. 

![image](https://github.com/user-attachments/assets/39f92d82-972f-4863-aa9b-1494e52afaaa)


UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.


          +---------------------+      +-------------------+        +------------------+
          |      Client         |      |    Microservice    |        |   Quote File     |
          +---------------------+      +-------------------+        +------------------+
                    |                          |                          |
                    |----(1) GET /get-quote -->|                          |
                    |                          |                          |
                    |                          |----(2) Read from file -->|
                    |                          |                          |
                    |                          |<---(3) Return Quote -----|
                    |<---(4) Return JSON ------|                          |
                    |                          |                          |
                    |----(5) Print Quote ------|                          |
                    |                          |                          |

