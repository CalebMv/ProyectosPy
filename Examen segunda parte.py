contador_de_intentos=0
while contador_de_intentos<=2:
 print("digite su usuario")
 usuario=input()
 print("digite su contraseña")
 contraseña=input()
 if usuario.upper() == "CALEBMURILLO" and contraseña.upper() == "MURILLO77":
        print("los datos son correctos")
        contador_de_intentos=3
        respuesta="si"
        saldo_bancario=0
        operacion=0
        saldo_nuevo=0
        while (respuesta.upper()=="SI"):
          print("Bienvenido al banco Mugiwara :D a continuación el menú de opciones")
          Depositar_dinero_a_la_cuenta="A"
          print("Depositar dinero a la cuenta es la opción A")
          Sacar_dinero_de_la_cuenta="B"
          print("Sacar dinero de la cuenta es la opción B")
          Ver_saldo="C"
          print("Ver saldo es la opción C")
          Salir="D"
          print("Salir es la opción D")
          correcto = False;
          opciones = [Depositar_dinero_a_la_cuenta,Sacar_dinero_de_la_cuenta,Ver_saldo,Salir]
          while (not correcto):
             print("Qué opción desea realizar¿?")
             opción=input()
             if opción.upper() in opciones and opción.upper()==Depositar_dinero_a_la_cuenta:
              print("Usted ha escogido la opción de deposito")
              correcto=True
              correcto5=False;
              correcto2=False;
              while (not correcto5):
                     print("Cuanto dinero desea ingresar¿?")
                     operacion=input()
                     verifict=operacion.isdigit()
                     if verifict==True:
                         operacion=int(operacion)
                         deposito=operacion
                         while (not correcto2):
                               if deposito % 1000 == 0:
                                  saldo_nuevo=deposito+saldo_bancario
                                  saldo_bancario=saldo_nuevo
                                  print("Usted ha ingresado un total de", deposito)
                                  print("Ahora su saldo es de ", saldo_nuevo)
                                  correcto2=True
                               else:
                                    print("El numero debe ser un multiplo de mil")
                                    break
                         correcto5=True
                     else:
                          print("Debe ingresar numeros, no letras")
             elif opción.upper() in opciones and opción.upper()==Sacar_dinero_de_la_cuenta:
              print("Usted ha escogido la opcion de sacar dinero")
              correcto=True
              correcto3=False;
              correcto4=False;
              while (not correcto3): 
                     print("Cuanto dinero desea retirar¿?")
                     operacion=input()
                     verifict2=operacion.isdigit()
                     if verifict2==True:
                         operacion=int(operacion)
                         retiro=operacion
                         while (not correcto4):
                             if retiro % 1000 == 0:
                                 if retiro<saldo_nuevo:
                                     saldo_nuevo=saldo_nuevo-operacion
                                     saldo_bancario=saldo_nuevo
                                     print("Ahora su saldo es de ", saldo_nuevo)
                                 else:
                                     print("No tiene los suficientes fondos para realizar la transacción")
                                 correcto4=True
                             else:
                                 print("El numero debe ser un multiplo de mil")
                                 break
                             correcto3=True
                     else:
                         print("Debe ingresar un numero, no una letra")
             elif opción.upper() in opciones and opción.upper()==Ver_saldo:
                print("Usted ha escogido la opcion de ver saldo")
                correcto=True
                print("Su saldo es un total de",saldo_nuevo)
             elif opción.upper() in opciones and opción.upper()==Salir:
              print("Usted ha escogido la opción de salir, muchas gracias por preferirnos :D")
              correcto=True
              exit()
             else:
              print("Esa opción no está en el menú") 
          print("Desea hacer algo más¿?")
          respuesta=input()
          if respuesta.upper()== "NO":
              print("Muchas gracias por su preferencia :D")
              exit()
 else:
  print("Los datos son incorrectos, vuelva a intentarlo")
  if contador_de_intentos==2:
   print("Limite de intentos alcanzado, bloqueo de seguirdad")
  contador_de_intentos=contador_de_intentos+1