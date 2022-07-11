import socket

host = "localhost"
port = 5000

s_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_server.bind((host, port))

s_server.listen(1)
con, addr = s_server.accept()

while True:
    mensagem = con.recv(1024).decode()

    if not mensagem:
        break

    nome, cargo, salario = mensagem.split(' ')

    salario = float(salario)

    if cargo.lower() == "programador":
        salario = salario * 1.18
    elif cargo.lower() == "operador":
        salario = salario * 1.2

    salario = str(salario)
    print(salario)
    con.send(salario.encode())

con.close()



