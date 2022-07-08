""""
    SOLID 
    S = single responsibility principle

    definition: 
    "a module, a class, or a method should be 
    responsible for a single functionality of a software system."
    OR
    "a class should have only one reason to change.
    reason <-> actor. eg an actor in ML may be preprocessor for data, or an evaluator

"""

class SRP_Model:
    def train(self, features):
        print("Model has been trained")
        return features

class Preprocessor:
    def preprocess(self, features):
        print("features have been preprocessed")

class SRP_Evaluator:
    def evaluate(self, model):
        print("Model has been evaluated")


if __name__ == "__main__":
    features = [
        [0, 1, 2],
        [3, 4, 5]
    ]

    model  = SRP_Model()
    preprocess = Preprocessor()
    evaluator = SRP_Evaluator()

    features = preprocess.preprocess(features)
    model.train(features)
    evaluator.evaluate(model)