from Codes.RLUnit.QLearning_Algorithm.QLearning import Qlearning
from Codes.RLUnit.QLearning_Algorithm.State import State
from Codes.Configuration import traffic_light_period
from collections import deque

class Agent:
    
    def __init__(self, agent_id, graph, reward, batch_size=32, max_len_queue=10000):
        self.action, self.reward, self.next_state, self.state = None, None, None, None
        self.agent_id = agent_id
        self.Q_Reward = reward
        self.graph = graph
        self.Q_State = State(self.graph, self.Q_Reward.information)
        self.QLearning = Qlearning()
        self.batch_size = batch_size
        self.memory = deque(maxlen=max_len_queue)
    
    def remember(self):
        self.memory.append((self.state, self.action, self.reward, self.next_state))
    
    def DQN_action(self):
        pass
    
    def Save(self, q_value, w_p):
        if not self.agent_id in self.graph.results_history.state_history.keys():
            self.graph.results_history.state_history[self.agent_id] = [self.next_state]
            self.graph.results_history.Action_history[self.agent_id] = [self.action]
            self.graph.results_history.Q_history[self.agent_id] = [q_value]
            self.graph.results_history.waiting_time_history_for_edge[self.agent_id] = [w_p]
            self.graph.results_history.epsilon_history[self.agent_id] = [self.QLearning.epsilon]
            self.graph.results_history.Q_Table_history[self.agent_id] = [self.QLearning.q_table]
        else:
            self.graph.results_history.state_history[self.agent_id].append(self.next_state)
            self.graph.results_history.Action_history[self.agent_id].append(self.action)
            self.graph.results_history.Q_history[self.agent_id].append(q_value)
            self.graph.results_history.waiting_time_history_for_edge[self.agent_id].append(w_p)
            self.graph.results_history.epsilon_history[self.agent_id].append(self.QLearning.epsilon)
            self.graph.results_history.Q_Table_history[self.agent_id].append(self.QLearning.q_table)
    
    def QLearning_action(self, step, scenario_type, method_name, episode_number):
        self.next_state, w_p = self.Q_State.get_state(self.agent_id, method_name)
        if scenario_type=="train":q_value, self.action = self.QLearning.fit(self.next_state, episode_number)
        else:q_value, self.action = self.QLearning.value_function(self.next_state)
        self.Save(q_value, w_p)
        self.reward = self.Q_Reward.Reward_Function(self.agent_id, method_name)
        if step > traffic_light_period:
            self.QLearning.replay(self.state, self.next_state, self.action, self.reward)
        self.state = self.next_state
        return self.action
    
    def get_action(self, step, scenario_type, method_name, episode_number):
        return self.QLearning_action(step, scenario_type, method_name, episode_number)
    
    def replay_bufer(self, callbacks_list, model_info_path, model_name):
        self.remember()
        if len(self.memory) > self.batch_size:
            self.dqnAlgo.replay(self.memory, callbacks_list, model_info_path, model_name)