import json


class ModelAI:
    model_nuber = 0

    def __init__(self, name, version):
        self.name = name
        self.version = version
        ModelAI.new_model()

    @classmethod
    def new_model(cls):
        cls.model_nuber += 1

    @classmethod
    def number_of_models_created(cls):
        return cls.model_nuber

    @classmethod
    def create_model_from_file(cls, file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return cls(data["name"], data["version"])


model1 = ModelAI("face_reco", 2.0)
model2 = ModelAI.create_model_from_file("model1.json")
model3 = ModelAI.create_model_from_file("model2.json")
print("Number of models created:", ModelAI.number_of_models_created())
print(f"model1 name: {model1.name} version: {model1.version}")
print(f"model2 name: {model2.name} version: {model2.version}")
print(f"model3 name: {model3.name} version: {model3.version}")
