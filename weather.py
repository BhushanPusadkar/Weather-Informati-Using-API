#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
from urllib import request
import json
from datetime import datetime


print("Content-type: text/html")
print()

form=cgi.FieldStorage()
ct=form.getvalue("city")

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'>")
print("<center>")
print("<br><h3> <span style='font-size:70px;'>&#9925 Current Weather of City : %s</span></h3>" %ct)

try:
    response=request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ct+'&appid=5be12623aef23282dab18b6e0b963bfd')
    
    data=response.read()
    #print(data)
    info=json.loads(data)
    print("<hr>")
    print("<br>Date_time : "+datetime.now().strftime("%d %b %Y | %I:%M:%S %p"))
    print("<br> -----------------------------------------")
    print("<br>Description : "+info['weather'][0]['description'])
    k=info['main']['feels_like']
    c=k-272.15
    print("<br>Temp Feels Like : %.2f degree celsius" %c)
    print("<br>Humidity :  "+str(info['main']['humidity']))
    print("<br>Wind Speed : "+str(info['wind']['speed']))
    print("<br>Country : "+info['sys']['country'])
    
    
    print("</center>")

except:
    print("<span style='font-size:100px;'>&#128533;</span>'")
    print("<h5>City Not Found......</h5>")

print("<center><br><br><a href='index.html'>Home</a></div></center>")