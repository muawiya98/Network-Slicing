from configtation import services_types, communication_units_types, number_of_request, number_of_units, units_for_service, requests_for_units
from CommunicationNetwork.communication_network import CommunicationNetwork
from RequestGenerator.request_generator import RequestGenerator
from Services.services import Serices

import random

class Graph:
    next_id = 1
    def __init__(self):
        self.id = Graph.next_id
        self.communication_units, self.services, self.requests = [], [] ,[]
        self.services_generation()
        self.communication_units_generation()
        self.request_generation()
        self.services2units()
        self.units2requests()
        Graph.next_id+=1

    def services_generation(self):
        self.services = []
        for service_type in services_types:
            self.services.append(Serices(service_type))

    def communication_units_generation(self):
        self.communication_units = []
        for _ in range(number_of_units):
            communication_type = random.choice(communication_units_types)
            self.communication_units.append(CommunicationNetwork(communication_type))

    def request_generation(self):
        self.requests = []
        for request_id in range(number_of_request):
            self.requests.append(RequestGenerator(request_id))

    def services2units(self):
        tepm_communication_units = self.communication_units
        for ind, _ in enumerate(self.services):
            the_range = len(tepm_communication_units)//(len(self.services)-ind)
            self.services[ind].set_conection(random.choices(tepm_communication_units, 
                                                            k=random.randint(0, the_range)))
            tepm_communication_units = [item for item in tepm_communication_units if item not in self.services[ind].connected_with]
    
    def units2requests(self):
        tepm_rquests = self.requests
        for ind, _ in enumerate(self.communication_units):
            the_range = len(tepm_rquests)//(len(self.communication_units)-ind)
            self.communication_units[ind].set_conection(random.choices(tepm_rquests, 
                                                                       k=random.randint(0, the_range)))
            tepm_rquests = [item for item in tepm_rquests if item not in self.communication_units[ind].connected_with]



    