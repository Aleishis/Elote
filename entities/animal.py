class Animal:
    
    #Este comentario es de prueba
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    @classmethod
    def get_list(cls):
        animals = [
            cls("Jirada", "Amarillo"),
            cls("Cebra", "Blanco y negro"),
            cls("Xenomorfo", "Negro"),
            cls("Tortuga", "Verde"),
            cls("Hipocampo", "Rosa"),
            cls("Oso hormiguero", "Gris"),
            cls("Pantera", "Rosa"),
            cls("Pajaro Carpintero", "Azul")
        ]
        return animals