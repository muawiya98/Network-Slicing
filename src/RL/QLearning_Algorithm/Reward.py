from Codes.Configuration import Weighting_Factor, Methods
import numpy as np
from math import log
class Reward:
    def __init__(self, information, graph, Agent_ids):
        self.information = information
        self.graph = graph
        self.previous_waiting_time = {key: 0 for key in Agent_ids}

    def Save(self, agent_id, waiting_time, std_waiting_time, reward):
        density = self.information.Average_Density_Vehicles(agent_id)
        if not agent_id in self.graph.results_history.waiting_time_history.keys():
            self.graph.results_history.waiting_time_history[agent_id] = [waiting_time]
            self.graph.results_history.std_waiting_time_history[agent_id] = [std_waiting_time]
            self.graph.results_history.reward_history[agent_id] = [reward]
            self.graph.results_history.density_history[agent_id] = [density]
        else:
            self.graph.results_history.waiting_time_history[agent_id].append(waiting_time)
            self.graph.results_history.std_waiting_time_history[agent_id].append(std_waiting_time)
            self.graph.results_history.reward_history[agent_id].append(reward)
            self.graph.results_history.density_history[agent_id].append(density)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def Reward_Function_1(self, agent_id, method_name):
        edges = self.graph.Junction_controlledEdge[agent_id]
        waiting_time, std_waiting_time = self.information.Reward_Info(edges, method_name)
        reward = log((Weighting_Factor*std_waiting_time) + ((1-Weighting_Factor)*(0.9**waiting_time)), 0.5)
        self.Save(agent_id, waiting_time, std_waiting_time, reward)
        return reward
    
    def Reward_Function_2(self, agent_id, method_name):
        edges = self.graph.Junction_controlledEdge[agent_id]
        waiting_time, std_waiting_time = self.information.Reward_Info(edges, method_name)
        waiting_time_, std_waiting_time_ = -waiting_time, -std_waiting_time
        reward = (Weighting_Factor*np.tanh(std_waiting_time_)) + ((1-Weighting_Factor)*np.tanh(waiting_time_))
        self.Save(agent_id, waiting_time, std_waiting_time, reward)
        return reward
    
    def Reward_Function_3(self, agent_id, method_name):
        edges = self.graph.Junction_controlledEdge[agent_id]
        waiting_time, std_waiting_time = self.information.Reward_Info(edges, method_name)
        waiting_time_, std_waiting_time_ = -waiting_time, -std_waiting_time
        reward = self.sigmoid(Weighting_Factor*std_waiting_time_) + self.sigmoid((1-Weighting_Factor)*waiting_time_)
        self.Save(agent_id, waiting_time, std_waiting_time, reward)
        return reward

    def Reward_Function_4(self, agent_id, method_name):
        if not agent_id in self.graph.results_history.waiting_time_history.keys():
            p_waiting_time = self.previous_waiting_time[agent_id]
        else:
            p_waiting_time = self.graph.results_history.waiting_time_history[agent_id][-1]
        edges = self.graph.Junction_controlledEdge[agent_id]
        waiting_time, std_waiting_time = self.information.Reward_Info(edges, method_name)
        reward = np.tanh(p_waiting_time - waiting_time)
        self.previous_waiting_time[agent_id] = waiting_time
        self.Save(agent_id, waiting_time, std_waiting_time, reward)
        return reward
    
    def Reward_Function(self, agent_id, method_name):
        return self.Reward_Function_1(agent_id, method_name)
        # if method_name in [Methods.Max_Log, Methods.Avg_Log]:return self.Reward_Function_1(agent_id, method_name)
        # elif method_name in [Methods.Max_Tanh, Methods.Avg_Tanh, Methods.Fixed, Methods.Maximum_Based, Methods.Random]:return self.Reward_Function_2(agent_id, method_name)
        # elif method_name in [Methods.Max_Sigmoid, Methods.Avg_Sigmoid]:return self.Reward_Function_3(agent_id, method_name)
        # elif method_name in [Methods.Max_Derivative_of_waiting_time, Methods.Avg_Derivative_of_waiting_time, Methods.Fixed, Methods.Maximum_Based, Methods.Communication, Methods.Emergency]:return self.Reward_Function_4(agent_id, method_name)
