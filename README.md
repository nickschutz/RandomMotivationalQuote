Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call. Do not advise your teammate to use your test program or require them to, your teammate must write all of their own code.

So for what I did is I used flask that exposes an endpoint ("/get-quote"). I only did it with a select few of the motivational quotes.
![image](https://github.com/user-attachments/assets/0407f914-e17f-4ac9-a049-be92f402995f)



Clear instructions for how to programmatically RECEIVE data from the microservice you implemented. Include an example call. 

To recieve the data, you would need to install a library requests. It will then be on the local port 5000. In this example, this would be the URL http://127.0.0.1:5000/get-quote
![image](https://github.com/user-attachments/assets/d1784011-da65-48e8-91ca-3ba1b20daed6)

It is simple enough to where, the request/receive will be in the same file. 

UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.
