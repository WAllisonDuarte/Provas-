
senha_cadastrada = "1234"
email_cadastrado = "teste@gmail.com"

while True:  
    email_usuario = input("Digite seu email cadastrado: ")
    senha_usuario = input("Digite sua senha cadastrado: ")

    
    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Login bem-sucedido! Bem-vindo.")
        break  
    else:
        print("Email ou senha incorretos. Tente novamente.")  
