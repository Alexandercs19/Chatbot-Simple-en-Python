import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Saludos Estimad/@ Diganos, ¿En que podemos ayudarlo?', ['saludos', 'buenos dias', 'buenas tardes', 'buenas noches', 'hey', 'buena', 'saludo', 'estimado', 'hola', 'buenas', 'Hola', 'Estimados'], single_response = True)
        response('Estamos ubicados en la Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica 11606.', ['Ubicacion', 'direccion', 'ubicarlos', 'lugar', 'ubicados', 'donde', 'queda'], single_response=True)
        response('Nuesto contacto es: 809-738-4852/809-793-2557', ['telefono', 'contacto', 'llamar', 'telefonos'], single_response=True)
        response('Nuestros horarios son: Lunes a Viernes 07:00 AM a 11:00 PM, Sabados 07:00 AM A 7:00 PM', ['Horarios', 'Trabajan', 'Trabajo', 'Pasar', 'abren', 'cierran', 'jornada', 'cierra'], single_response=True)
        response('Actualmente tenemos tecnologos de: Simulacion Interactivas y Videojuegos, Telecomunicaciones, Inteligencia Artificial, Informatica Forense, Energias Renovables, Redes de la Informacion, Mecatronica, Manufactura Automatizada, Manufactura de Dispositivos, Medicos, Diseño Industrial, Multimedia, Sonido, Desarrollo de Software, Analitica Y Ciencia de Datos, Seguridad Informatica.', ['carreras', 'cursos','tecnologos', 'materias'], single_response=True)
        response('Puede entregarnos los documentos de forma fisca en el edificio 1 en el primer piso como tambien de forma online subiendo las credenciales a orbi en el menu de admision', ['entregar', 'documentos', 'entrega'], single_response=True)
        response('Puedes inscribirte yendo a https://orbi.edu.do/orbi/ en la opcion de registrate ya desde ahi es solo llenar los datos.', ['inscribirme', 'registrame', 'postularme', 'proceso', 'empezar', 'admision', 'solicitar'], single_response=True)
        response('Puedes pagar a traves del orbi en la opcion de caja pagar en linea como tambien puede ir a cede en el edificion 1 piso 1', ['pagar', 'depositar'], required_words=['pagar'])
        response('¿Tienes alguna otra inquietud o duda?', ['esta bien', 'gracias', 'entiendo', 'entendido', 'ya veo', 'ok'], single_response=True)
        response('Gracias por escribirnos recuerda que siempre estaremos a tu disposicion en cuanto la necesites', ['es todo', 'solo era eso', 'duda', 'gracias', 'tengo todo', 'muchas gracias', 'muy amables'], single_response=True)


        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['¿Podrias repetirlo de nuevo?', 'No estoy seguro de lo quieres', 'Podrias ser mas especifico', 'No entiendo tu pregunta o argumento'][random.randrange(4)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))