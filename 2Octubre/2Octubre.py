from adt_nodos import ListaEnlazada

M=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
     "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

edo=['AGUASCALIENTES','BAJA CALIFORNIA','BAJA CALIFORNIA SUR','CAMPECHE','COAHUILA','COLIMA',
        'CHIAPAS','CHIHUAHUA','DISTRITO FEDERAL','DURANGO','GUANAJUATO','GUERRERO','HIDALGO'
        ,'JALISCO','ESTADO DE MÉXICO','MICHOACÁN','MORELOS','NAYARIT','NUEVO LEÓN','OAXACA','PUEBLA',
        'QUERÉTARO','QUINTANA ROO','SAN LUIS POTOSÍ','SINALOA','SONORA','TABASCO','TAMAULIPAS','TLAXCALA'
        ,'VERACRUZ','YUCATÁN','ZACATECAS']
anio=str(input('Que año desea ver(2017-2018): '))
estado=int(input('Que estado(1-32)?:'))
mes=int(input("mes(1-12)?:"))
esta_lista= ListaEnlazada() 
archivo=open(anio+'Precip.csv','rt',encoding='latin')
datos=archivo.readlines()
for l in datos:
    l.strip()


