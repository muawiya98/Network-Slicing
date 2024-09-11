from RL.RL_algorithm import RLAlgorithm
import numpy as np
import random

class Qlearning(RLAlgorithm):

    def __init__(self, number_of_action, lr=0.01, gamma=0.9, epsilon=0.99, decay=0.0001, min_epsilon=0.01):
        super().__init__(lr, gamma, epsilon, decay, min_epsilon)
        self.algorithm_name = "Q-learning"
        self.number_of_action = number_of_action
        self.q_table = {}

    def make_key(self, key):
        if not tuple(key) in self.q_table.keys():
            self.q_table[tuple(key)] = np.zeros(self.number_of_action)
    
    def epsilon_update(self):
        if self.epsilon >= self.min_epsilon:
            self.epsilon -= self.epsilon * self.decay

    def replay(self, state, next_state, action_index, reward):
        self.make_key(state)
        self.make_key(next_state)
        # Q(s, a) = (1-α)*Q(s, a) + α * (r + γ * max[Q(s', a')])
        self.q_table[tuple(state)][action_index] = ((1 - self.lr) * self.q_table[tuple(state)][action_index]) + (self.lr * (reward + self.gamma * max(self.q_table[tuple(next_state)])))

    def policy(self, state):
        rand = np.random.uniform(0, 1)
        if rand > self.epsilon:action_index = self.value_function(state)
        else:action_index = random.randint(0, self.number_of_action-1)
        action = np.zeros(self.number_of_action)
        action[action_index] = 1
        self.epsilon_update()
        return action, action_index
    
    def value_function(self, state):
        self.make_key(state)
        return np.argmax(self.q_table[tuple(state)])

    def fit(self, state):
        return self.policy(state)

    def print_q_table(self, q_table):
        print("------------------- Q LEARNING TABLE ------------------\n",
              q_table, "\n-------------------------------------------------------")