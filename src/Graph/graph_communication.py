from RequestGenerator.request_generator import RequestGenerator
from configtation import number_of_request
import random

class Graph:
    next_id = 1
    def __init__(self, services, communication_units):
        self.id = Graph.next_id
        self.communication_units, self.services = communication_units, services
        self.requests = []
        self.request_generation()
        self.units2requests()
        Graph.next_id+=1

    def request_generation(self):
        self.requests = []
        for request_id in range(number_of_request):
            self.requests.append(RequestGenerator(request_id))
    
    def units2requests(self):
        for ind, _ in enumerate(self.communication_units):
            the_range = len(self.requests)//3
            self.communication_units[ind].set_conection(random.sample(self.requests, 
                                                                       k=random.randint(1, the_range)))
