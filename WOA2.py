class Clan:
    cantidadMiembros = 0
    def __init__(self, nombre, fundador):
        self.miembros = []
        self.nombre = nombre
        self.fundador = fundador.nombre
        self.miembros.append(fundador)
        self.cantidadMiembros += 1
        
    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
        self.cantidadMiembros += 1
        
    def listar_miembros(self):
        print(f"El clan {self.nombre} tiene {self.cantidadMiembros} miembros")
        for miembro in self.miembros:
            print(miembro)

#***********************************************************************

class Personaje:
    def __init__(self, nombre, titulo, clan = None):
        self.nombre = nombre
        self.titulo = titulo
        self.clan = clan

    def asignar_clan(self, clan):
        self.clan = clan

    def realizar_ataque(self, objetivo):
        damage = ((self.fuerza+self.ataque) / ((self.vida_original-self.puntos_vida)+self.vida_original))/10
        objetivo.recibir_ataque(damage)

    def recibir_ataque(self, damage):
        factor_damage = (self.defensa*damage)/100
        self.fuerza = round(self.fuerza/(factor_damage+1))
        self.puntos_vida = round(self.puntos_vida/(factor_damage+1))
        self.defensa = round(self.defensa/(factor_damage+1))
        self.ataque = round(self.ataque/(factor_damage+1))

        if self.puntos_vida > 0:
            print(f"{self.nombre} ha recibido un ataque puntos de vida = {self.puntos_vida}")
        else:
            print(f"el {self.titulo} {self.nombre} ha muerto")
        

    def __str__(self):
        return (f"{self.titulo}: {self.nombre}\n"
                f"Fuerza: {self.fuerza}, Puntos de Vida: {self.puntos_vida}, "
                f"Defensa: {self.defensa}, Ataque: {self.ataque}, "
                f"Clan: {self.clan}")
        
#***********************************************************************

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, "Guerrero")
        self.fuerza = 90
        self.puntos_vida = 100
        self.defensa = 90
        self.ataque = 100
        self.vida_original = self.puntos_vida
        
#***********************************************************************

class Mago(Personaje):
    def __init__(self, nombre, titulo = "Mago"):
        super().__init__(nombre, titulo)
        self.fuerza = 80
        self.puntos_vida = 100
        self.defensa = 80
        self.ataque = 90
        self.vida_original = self.puntos_vida
        
#***********************************************************************

class Fundador(Mago):
    def __init__(self, nombre):
        super().__init__(nombre, "Fundador")
        self.fuerza = 100
        self.puntos_vida = 110
        self.defensa = 110
        self.ataque = 110
        self.vida_original = self.puntos_vida
        print(f"{self.nombre} ha fundado un clan")
        
#***********************************************************************

def crearMago(titulo):
    nombre = input(f"Nombre del {titulo} : ").upper()
    mago = Mago(nombre)
    magos.append(mago)
    return mago

def crearFundador(mago):
    fundador = Fundador(mago.nombre)
    fundadores.append(fundador)
    magos.remove(mago)
    return fundador

def crearClan(fundador):
    nombreClan = input("Nombre del clan : ").upper()
    clan = Clan(nombreClan, fundador)
    clanes.append(clan)
    fundador.asignar_clan(nombreClan)
    
def seleccionarClan(personaje):
    asignado=False
    while not asignado:
        for index, clan in enumerate(clanes):
            print(f"{index+1} : {clan.nombre}")
        print()
        nombreClan=input("Digite el nombre del clan -> ").upper()
        for clan in clanes:
            if clan.nombre==nombreClan:
                personaje.asignar_clan(nombreClan)
                clan.agregar_miembro(personaje)
                print(f"{personaje.nombre} ha sido agregado al clan {clan.nombre} <ENTER PARA CONTINUAR>")
                input()
                asignado = True
        if asignado == False:
            print(f"el clan {nombreClan} no existe")
            print()


def seleccionarObjetivo(clanes, fundadores, magos, guerreros):
    print("Modo de selección :")
    print("1. Por clan")
    print("2. Listar todos los personajes")
    print("3. Atacar por titulo")
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        print("lista de clanes")
        for index, clan in enumerate(clanes):
            print(f"{index+1} {clan.nombre}")
        indexClan = int(input("Selecciona el número del clan")) - 1
        if 0 <= indexClan < len(clanes):# es igual que indexClan >= 0 or indexClan < len(clanes)
            clan = clanes[indexClan]
            print(f"Miembros del clan {clan.nombre}")
            clan.listar_miembros()
            nombreObjetivo = input("Escriba el nombre de su objetivo").upper()
            for miembro in clan.miembros:
                if nombreObjetivo == miembro.nombre:
                    return miembro
            return None
        else:
            print("Clan no válido")

    if opcion == 2:
        listaPersonajes = fundadores + magos + guerreros
        print("lista de todos los personajes")
        for miembro in listaPersonajes:
            print(miembro)
        nombreObjetivo = input("Escriba el nombre de su objetivo").upper()
        for miembro in listaPersonajes:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    if opcion == 3:
        print("Titulo a listar")    
        print("1. Fundadores")
        print("2. Magos")
        print("3. Guerreros")
        tipo = int(input("Digite su opción: "))
        if tipo ==1:
            listaObjetivos = fundadores
        elif tipo == 2:
            listaObjetivos = magos
        elif tipo == 3:
            listaObjetivos = guerreros
        print("Personajes :")
        for personaje in listaObjetivos:
            print(personaje)
        nombreObjetivo = input("Escriba el nombre de su objetivo").upper()
        for miembro in listaObjetivos:
            if nombreObjetivo == miembro.nombre:
                return miembro
        return None

    print("Opción no válida")
    return None

guerreros = []
magos = []
fundadores = []
clanes = []

cantidadJugadores = int(input("Cantidad de jugadores : "))
for i in range(cantidadJugadores):
    if i==0:
        mago = crearMago("Fundador")
        fundador = crearFundador(mago)
        crearClan(fundador)
    else:
        opcionPersonaje = int(input("1. Guerrero\n2. Mago\n Opcion : "))
        if opcionPersonaje ==1:
            nombre = input(f"nombre del Guerrero (jugador({i+1}/{cantidadJugadores})) : ").upper()
            guerrero = Guerrero(nombre)
            seleccionarClan(guerrero)
            guerreros.append(guerrero)
        else:
            mago = crearMago("Mago")
            opcionCrearClan=int(input("Desea crear su propio clan?\n1. SI\n2. NO\nOpcion : "))
            if opcionCrearClan==1:
                fundador=crearFundador(mago)
                crearClan(fundador)
            else:
                seleccionarClan(mago)


# for clan in clanes:
#     clan.listar_miembros()


for mago in magos:
    print(mago.nombre)

for guerrero in guerreros:
    print(guerrero.nombre)

for fundador in fundadores:
    print(fundador.nombre)

personajeTurno = guerreros[0]
objetivo = seleccionarObjetivo(clanes, fundadores, magos, guerreros)
print("*****************")
print("*****************")
print("*****************")
print("ANTES DEL ATAQUE")
print(objetivo)
personajeTurno.realizar_ataque(objetivo)
print("DESPUES DEL ATAQUE")
print(objetivo)





# nombreObjetivo = input("Nombre del objetivo : ")
# personaje=buscarObjetivo(nombreObjetivo)
# print(personaje)


# guerrero = Guerrero("g1")
# print (guerrero)
# guerreros.append(guerrero)
# # print(guerreros[0])

# guerrero2 = Guerrero("g1")
# print (guerrero2)
# guerreros.append(guerrero2)
# # print(guerreros[1])

# for guerrero in guerreros:
#     print(guerrero)
# mago = Mago("m1")
# mago2 = Mago("m2")
# fundador = Fundador(mago)


# print(guerrero)
# print(mago2)
# print(fundador)



# for guerrero in guerreros:
#     print(guerrero)
# for mago in magos:
#     print(mago)
# for fundador in fundadores:
#     print(fundador)
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    