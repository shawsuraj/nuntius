import urllib as ul

def encData(mail) :
    mydata=[('fromemail', mail.frm),
            ('toemail', mail.to),
            ('subject', mail.sub),
            ('body', mail.body)]    #The first is the var name the second is the value
    mydata=ul.parse.urlencode(mydata)
    return mydata

def connect(url,mydata) :
    req=ul.request.Request(url+"/php/mail.php", mydata)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    return req

def send(req) :
    msg=ul.request.urlopen(req).read()
    return msg
