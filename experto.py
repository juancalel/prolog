from pyswip import Prolog #importar la clase Prolog que se encuentra en pyswip

prolog = Prolog()       #instanciar por la creación de un objeto
prolog.consult("hechos.pl")

X = input("¿Qué le gusta a ...?")

for valor in prolog.query("le_gusta(" + X + ", Y)"):
    print(X, "le gusta ", valor["Y"])
    


prolog.consult('animales.pl')
X = input("¿Es un animal ...?")

result = bool(list(prolog.query("animal("+ X +")")))
print(result)