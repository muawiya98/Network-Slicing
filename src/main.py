from configtation import services_types, communication_units_types, number_of_units, number_of_steps
from CommunicationNetwork.communication_network import CommunicationNetwork
from Graph.graph_communication import Graph
from Services.services import Serices
from RL.QLearning_Algorithm.State import State
import random

class Environmente:
    def __init__(self):
        self.services = []
        self.communication_units = []

    def services_generation(self):
        for service_type in services_types:
            self.services.append(Serices(service_type))

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
        self.state_generator = State(self.services, self.communication_units)
        for step in range(number_of_steps):
            graph = Graph(self.services, self.communication_units)
            for request in graph.requests:
                print(self.state_generator.get_state(request))

if __name__ == '__main__':
    environmente = Environmente()
    environmente.services_generation()
    environmente.communication_units_generation()
    environmente.services2units()
    environmente.main()