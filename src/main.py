from configtation import services_types, communication_units_types, number_of_units, number_of_steps
from CommunicationNetwork.communication_network import CommunicationNetwork
from RL.QLearning_Algorithm.state import State
from RL.QLearning_Algorithm.reward import Reward
from Graph.graph_communication import Graph
from Service.service import Service
from RL.agent import Agent
import numpy as np
import random

class Environmente:
    def __init__(self):
        self.services = []
        self.communication_units = []

    def services_generation(self):
        for service_type in services_types:
            self.services.append(Service(service_type))

    def communication_units_generation(self):
        for _ in range(number_of_units):
            communication_type = random.choice(communication_units_types)
            self.communication_units.append(CommunicationNetwork(communication_type))

    def services2units(self):
        for ind, _ in enumerate(self.services):
            the_range = len(self.communication_units)//3
            self.services[ind].set_conection(random.sample(self.communication_units, 
                                                            k=random.randint(1, the_range)))
    def main(self):
        state_generator = State(self.services, self.communication_units)
        reward_calculator = Reward(self.services, self.communication_units)
        allocator_agent = Agent(state_generator, reward_calculator, len(self.communication_units)+len(self.services), 'allocator')
        assigner_agnet = Agent(state_generator, reward_calculator, len(self.services), 'assigner')
        for step in range(number_of_steps):
            print(20*"*", f"{step}", 20*"*")
            graph = Graph(self.services, self.communication_units)
            for request in graph.requests:
                print(20*"-")
                allocator_action = allocator_agent.get_action(request)
                assigner = assigner_agnet.get_action(request)



if __name__ == '__main__':
    environmente = Environmente()
    environmente.services_generation()
    environmente.communication_units_generation()
    environmente.services2units()
    environmente.main()