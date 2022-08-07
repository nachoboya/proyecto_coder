from django.forms import Form, IntegerField, CharField, EmailField


class CursoFormulario(Form):

    nombre = CharField()
    camada = IntegerField()



class ProfesorFormulario(Form):

    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    profesion = CharField()

