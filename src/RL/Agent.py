from RL.QLearning_Algorithm.q_learning import Qlearning

class Agent:
    
    def __init__(self, state_generator, reward_calculator, number_of_action, agent_type, batch_size=32):
        self.action, self.action_index, self.reward, self.next_state, self.state = None, None, None, None, None
        self.QLearning = Qlearning(number_of_action)
        self.agent_type = agent_type
        self.batch_size = batch_size
        self.reward_calculator = reward_calculator
        self.state_generator = state_generator
        self.have_next = False
    
    def q_learning_action(self, request):
        self.next_state = self.state_generator.get_state(request)
        self.action, self.action_index = self.QLearning.fit(self.next_state)
        self.reward = self.reward_calculator.get_reward(self.agent_type, request, self.action)
        if self.have_next:
            self.QLearning.replay(self.state, self.next_state, self.action_index, self.reward)
        self.state = self.next_state
        self.have_next = True
        return self.action
    
    def get_action(self, request):
        return self.q_learning_action(request)