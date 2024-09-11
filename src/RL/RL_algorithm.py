from abc import abstractmethod, ABC
# import matplotlib.pyplot as plt

class RLAlgorithm(ABC):
    def __init__(self, lr=0.5, gamma=0.9, epsilon=0.9, decay=0.99, min_epsilon=0.1):
        self.min_epsilon = min_epsilon
        self.algorithm_name = ""
        self.epsilon = epsilon
        self.gamma = gamma
        self.decay = decay
        self.rewards = []
        self.lr = lr

    @abstractmethod
    def fit(self, *args, **kwargs):
        pass

    @abstractmethod
    def policy(self, *args, **kwargs):
        pass

    @abstractmethod
    def value_function(self, state: int, *args, **kwargs):
        pass