import socket 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_input = raw_input('Enter url: ')
web_site = user_input.split('/')[2]# можно просто сразу срез от www до com
mysock.connect((web_site, 80))
mysock.send('GET ' + user_input + ' HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data)

mysock.close()
