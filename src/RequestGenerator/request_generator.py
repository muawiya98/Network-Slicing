from configtation import services_types
import random
class RequestGenerator:
    # next_id = 0
    def __init__(self, request_id):
        self.request_id = request_id # RequestGenerator.next_id
        self.service_required = random.choice(services_types)
        # RequestGenerator.next_id+=1