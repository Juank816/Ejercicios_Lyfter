#TEMA: Funciones (PARAMETROS Y RETORNOS)
#NOMBRAMIENTOS
#El uso principal de las funciones es seguir el principio DRY del código limpio: Don’t Repeat Yourself.

# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = (juan_scores["spanish_score"] + juan_scores["science_score"] + juan_scores["history_score"]) / 3
sofia_scores["average_score"] = (sofia_scores["spanish_score"] + sofia_scores["science_score"] + sofia_scores["history_score"]) / 3
paul_scores["average_score"] = (paul_scores["spanish_score"] + paul_scores["science_score"] + paul_scores["history_score"]) / 3

juan_scores["is_exempted"] = juan_scores["average_score"] > 70
sofia_scores["is_exempted"] = sofia_scores["average_score"] > 70
paul_scores["is_exempted"] = paul_scores["average_score"] > 70



#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#  Podemos notar que ese calculo de (spanish_score + science_score + history_score) / 3 se repite para cada 
#  estudiante.
#  Tambien estamos repitiendo la validación de si el average_score > 70.
#  Además puede ser confuso y repetitivo de leer ya que estamos haciendo varias cosas a la vez.
#  Lo mejor dado estas circunstancias es dividir esto en funciones reutilizables más pequeñas.

def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
juan_scores = {
  "spanish_score": 75,
	"science_score": 95,
  "history_score": 54,
}
sofia_scores = {
  "spanish_score": 64,
	"science_score": 56,
  "history_score": 98,
}
paul_scores = {
  "spanish_score": 72,
	"science_score": 75,
  "history_score": 79,
}

# Averages
juan_scores["average_score"] = get_average_score(juan_scores)
sofia_scores["average_score"] = get_average_score(sofia_scores)
paul_scores["average_score"] = get_average_score(paul_scores)

juan_scores["is_exempted"] = is_student_exempted(juan_scores)
sofia_scores["is_exempted"] = is_student_exempted(sofia_scores)
paul_scores["is_exempted"] = is_student_exempted(paul_scores)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#Incluso podemos hacer este código aun mejor convirtiendo estos diccionarios en una lista y haciendo un 
#ciclo que haga lo mismo para todos:
def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
students = [
  {
    "name": "Juan",
		"spanish_score": 75,
		"science_score": 95,
		"history_score": 54,
	},
  {
    "name": "Sofia",
		"spanish_score": 64,
		"science_score": 56,
		"history_score": 98,
	},
  {
    "name": "Paul",
		"spanish_score": 72,
		"science_score": 75,
		"history_score": 79,
	}
]

# Averages
for student in students:
  student["average_score"] = get_average_score(student)
  student["is_exempted"] = is_student_exempted(student)
  print(student["name"], " is_exempted is ", student["is_exempted"])
