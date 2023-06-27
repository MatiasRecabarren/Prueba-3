import funciones_prueba as fn

#Lo intente, aunque fracase again
while True:
    fn.validar_menu()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.validar_rut()
        fn.validar_nombre()
        fn.validador_unico()#Este no sirve 
        fn.validar_nombre_mascota()
        fn.validar_dias()
        fn.guardar_mascota()#Incompleto
    elif opcion == 2:
        fn.buscar()#Como no sirve el arreglo dudo que este si
    elif opcion == 3:
        fn.retirarse()
    else:
        print ("Gracias por venir vuelva pronto")
    break