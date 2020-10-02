M=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
     "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
Edo=['AGUASCALIENTES','BAJA CALIFORNIA','BAJA CALIFORNIA SUR','CAMPECHE','COAHUILA','COLIMA',
        'CHIAPAS','CHIHUAHUA','DISTRITO FEDERAL','DURANGO','GUANAJUATO','GUERRERO','HIDALGO'
        ,'JALISCO','ESTADO DE MÉXICO','MICHOACÁN','MORELOS','NAYARIT','NUEVO LEÓN','OAXACA','PUEBLA',
        'QUERÉTARO','QUINTANA ROO','SAN LUIS POTOSÍ','SINALOA','SONORA','TABASCO','TAMAULIPAS','TLAXCALA'
        ,'VERACRUZ','YUCATÁN','ZACATECAS']
esta_lista= []
for anio in range(2017,2019):
    anio_lista=[]
    archivo=open(str(anio)+'Precip.csv','rt')
    datos=archivo.read()
    lineas=datos.split('\n')
    for estado in range(2,34):
        mes_lista=[]
        edo=lineas[estado].split(',')
        for mes in range(1,14):
            mes_lista.append(edo[mes])
        anio_lista.append(mes_lista)
    esta_lista.append(anio_lista)
def Suma(y,e):
    s=0.0
    for x in range(0,12,1):
        s+=float(esta_lista[y-2017][e-1][x])
    return s
    
estado=int(input('Que estado(1-32)?:'))
anio=int(input("año(2017-2018)?:"))
mes=int(input("mes(1-12)?:"))

print(f"En el estado de {Edo[estado-1]} Llovió un promedio de {esta_lista[anio-2017][estado-1][mes-1]}"
      +f" centímetros cúbicos en el mes de {M[mes-1]} de {anio}\n----------------------------------------------------")

print(f"En el estado de {Edo[estado-1]} Llovió un promedio Anual de {'%.2f'%(float(esta_lista[anio-2017][estado-1][12])/12)}"
      +f" centímetros cúbicos\n----------------------------------------------------")
print(f"La suma de los 12 meses del estado de {Edo[estado-1]} de {anio} es: {'%.2f'%Suma(anio,estado)} n----------------------------------------------------")
print("+++++++++++++++++++++el mes que mas llovió+++++++++++++++++++++\n\n\n")
for a in range(0,2):
    print(f"++++++++++++++++++++++++++++{a+2017}+++++++++++++++++++++++++++")
    for e in range(0,32):
        ML=[]
        for m in range(0,12,1):
            ML.append(float(esta_lista[a][e][m]))
        m=max(ML)
        i=ML.index(m)
        print(f"año: {a+2017}\nEstado: {Edo[e]}\nMes: {M[i]}\nPromedio: {m}\n-------------------------------------------\n")

print("+++++++++++++++++++++el mes que menos llovió+++++++++++++++++++++\n\n\n")
for a in range(0,2):
    print(f"++++++++++++++++++++++++++++{a+2017}+++++++++++++++++++++++++++")
    for e in range(0,32):
        ML=[]
        for m in range(0,12,1):
            ML.append(float(esta_lista[a][e][m]))
        m=min(ML)
        i=ML.index(m)
        print(f"año: {a+2017}\nEstado: {Edo[e]}\nMes: {M[i]}\nPromedio: {m}\n-------------------------------------------\n")
