#file = open("/home/ccarreterop/Desktop/SNPs/archivo_para_Rocio/sanos/genotiposanocolumna") Aqui es donde me abro el archivo el cual quiero codificar lo he cambiado de sitio a dentro del bucle porque parece como si n me lo leyera las veces que quiero que lo haga
claves = open("clave")#Este es el archivo donde tengo las claves para hacer la codificacion los que estan en la primera columna quiero que se codifiquen en mi archivo file en 1 los de la segunda en 2 y los de la tercera en 3.
archivo = open("rs2", "w")#este es el archivo de salida
clavelineas = []

for clave in claves:
	clavelineas.append(clave.rstrip("\n").split("\t"))#aqui me transformo la clave que tengo en un array donde pueda seleccionar la casilla que me interesa
n = -1 #mi contador
rs = 0 # la clave esla misma cada 192 veces . Es decir la primera fila de la clave es la codificacion para la fila 1 193 385 etc
rs2 = 192# vale para lo mismo que la anterior
newline = ""
for todo in range(1,192):#Esto e slo que no sale aqui intento que me lea el archivo 168 veces una por cada linea que tiene el archivo clave
   file = open("genotiposanocolumna")
   for line in file:
      n = n + 1
      linea = line.rstrip("\n") #aqnaui me lee el archivo me lo separa en lineas y me quita el salto de pagi
  
      if n == rs or (n -rs) % 192 == 0: # la condicion para que pase en este caso solo pasaria la primera columna (el n lo empecé en menos 1) la 193 la 385 etc que coincide que necesitan codificarse con la primera linea del archivo clave

         if linea == clavelineas[rs][0]:
            newline = newline + "1" + "\n" 
         if linea == clavelineas [rs][1]:
            newline = newline + "2" + "\n"
         if linea == clavelineas [rs][2]:
            newline = newline + "3" + "\n" # aqui es cuando le digo que si lo que aparece en el archivo es igual a la primera columna ponga 1 si es igual a la segunda pornga 2 y si es igual a la tercera ponga 3

#archivo.write(newline)      
           
      else:
         rs = rs + 1 # aqui intento aumentar ls paramentros en uno de modo que cuando vuelva a hacerme el archivo me codifique la fila 2 194 etc
         rs2 = rs2 + 1
         
print(newline)# para comprobar que me gnera la variable con todo codificado pero nooooooooooo   
#file.seek(0,0)esto lo probe para que me fuera al principio del archivo otra vez pero nada





