usuario = {}

#Esta funcion registara usuarios

def registrar_usuario():
  
  id_user = int(input("Ingrese el id"))
#usuario.update({"id":id_user})
  name_user = input("nombre")

  email_user = input("correo")

  clave = input("clave")

  usuario[id_user] = {"nombre": name_user, "correo": email_user, "clave": clave}

#Esta funcion llama un for e itera el diccionario
def ver_usuario():
  for key, value in usuario.items:
    print(key, value)



registrar_usuario();

registrar_usuario();

ver_usuario();


