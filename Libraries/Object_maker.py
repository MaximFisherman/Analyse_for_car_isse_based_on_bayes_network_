


class Object_maker:
    Buffer_size = 4046

    def __init__(self, symptoms):
        if type(symptoms) == set or type(symptoms) == str:
            self.symptoms = symptoms
        else:
            print("Not right type of symptoms, expected string or set")
            raise

    def format(self):
        message = b""
        for st in self.symptoms:
            message += bytes(st, encoding='utf8') + b" "
        
        return message

    def unformat(self):
        if type(self.symptoms) == str:
            list_of_symptoms = self.symptoms.split(" ")
            return list_of_symptoms
        else:
            print("Not right type of symptoms, expected string")
            raise 