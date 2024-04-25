from profesor import Profesor
from alumno import Alumno


profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabi", "gabi@um.edu.ar")

alumno_juan = Alumno("Juancito")
alumno_jose = Alumno("Jose")

for i in range(0,6,1):
    alumno_juan.falta()

print(alumno_juan.esta_libre())

alumno_jose.elegir_dieta("veggie")
alumno_juan.es_vegano()

print("La jose es " + alumno_jose.__dieta__)
print(alumno_juan.__dieta__)

alumno_juan.mentoria(profe_elio)
print(alumno_juan.__mentor__.__nombre__)