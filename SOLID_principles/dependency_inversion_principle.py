"""
    SOLI>D< 
    D = dependency inversion principle.

    definition:
    "Classes should depend on abstractions not concretions." 
"""
from abc import ABC, abstractmethod


class Evaluator(ABC):

    @abstractmethod
    def evaluate(self):
        pass


class TensorFlowEvaluator(Evaluator):

    def evaluate(self):
        print("Evaluating with TensorFlow.")


class PyTorchEvaluator(Evaluator):

    def evaluate(self):
        print("Evaluating with PyTorch.")


class MLPipeline:

    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def evaluate(self):
        self.evaluator.evaluate()


if __name__ == "__main__":
    evaluator = PyTorchEvaluator()
    ml_pipeline = MLPipeline(evaluator)
    ml_pipeline.evaluate()