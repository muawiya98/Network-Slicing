import numpy as np

class State:
    def __init__(self, services, communication_units):
        self.services = services
        self.communication_units = communication_units

    def get_state(self, request):
        request_links = []
        unit_links = [0] * len(self.services)
        for unit in self.communication_units:
            if request in unit.connected_with:
                request_links.append(1)
                for ind, service in enumerate(self.services):
                    if unit in service.connected_with:unit_links[ind] = 1
            else:request_links.append(0)
        return np.concatenate([request_links, unit_links])