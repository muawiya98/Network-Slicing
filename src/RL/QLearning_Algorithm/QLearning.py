from src.RL.RLAlgorithm import RLAlgorithm
# from src.Configuration import NUMBER_OF_ACTION, fully_exploration
import numpy as np

class Qlearning(RLAlgorithm):

    def __init__(self, lr=0.01, gamma=0.9, epsilon=0.99, decay=0.0001, min_epsilon=0.01):
        super().__init__(lr, gamma, epsilon, decay, min_epsilon)
        self.algorithm_name = "Q-learning"
        self.q_table = {}
        self.epsilon_list = []

    def replay(self, state, next_state, action, reward):
        action -=1
        if not tuple(state) in self.q_table.keys():
            self.q_table[tuple(state)] = np.zeros(NUMBER_OF_ACTION)
        if not tuple(next_state) in self.q_table.keys():
            self.q_table[tuple(next_state)] = np.zeros(NUMBER_OF_ACTION)
        # Q(s, a) = (1-α)*Q(s, a) + α * (r + γ * max[Q(s', a')])
        self.q_table[tuple(state)][action] = ((1 - self.lr) * self.q_table[tuple(state)][action]) + \
                                             (self.lr * (reward + self.gamma * max(self.q_table[tuple(next_state)])))

    def policy(self, state, episode_number):
        if not tuple(state) in self.q_table.keys():
            self.q_table[tuple(state)] = np.zeros(NUMBER_OF_ACTION)
        rand = np.random.uniform(0, 1)
        if rand > self.epsilon and episode_number>fully_exploration:
            q_value, action = self.value_function(state)
        else:
            q_value, action = self.q_table[tuple(state)], np.random.choice([*range(1,NUMBER_OF_ACTION+1)]) 
        if self.epsilon >= self.min_epsilon:
            self.epsilon -= self.epsilon * self.decay
        self.epsilon_list.append(self.epsilon)
        return q_value, action
    
    def value_function(self, state):
        if not tuple(state) in self.q_table.keys():
            self.q_table[tuple(state)] = np.zeros(NUMBER_OF_ACTION)
        return self.q_table[tuple(state)], np.argmax(self.q_table[tuple(state)])+1

    def fit(self, state, episode_number):
        return self.policy(state, episode_number)

    def print_q_table(self, q_table):
        print("------------------- Q LEARNING TABLE ------------------\n",
              q_table, "\n-------------------------------------------------------")