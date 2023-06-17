class Car:
    color = ""

    def __init__(self, color):
        self.color = color

    def move(self):
        print(f"Car of color {self.color} is moving")

car1 = Car(color="blue")
car2 = Car(color="red")

car1.move()
car2.move()


class BasicMLModel:

    def __init__(self, name, params):
        self.name = name
        self.parameters = params

    def to_string(self):
        return f"MLModel with name = {self.name} and {len(self.parameters)} parameters"


class MLModel1(BasicMLModel):

    name = ""
    parameters = {}

    def train(self, data):
        print("We are training very hard")

    def infer(self, input):
        print("Infering something")
        return "Result"

class MLModel2(BasicMLModel):

    def train(self, data):
        print("Train method #2")

    def infer(self, input):
        print("Infering something for model 2")
        return "Result2"


model = MLModel1(name="GPT15", params={"very": "cool"})
model.train({})
model.infer("Give me all the prime numbers")
print(model)
print(model.to_string())

model2 = MLModel2(name="GPT158", params={"another": "parameter", "second": "parameter"})
model2.train({})
model2.infer("Give me all the prime numbers")
print(model2)
print(model2.to_string())



