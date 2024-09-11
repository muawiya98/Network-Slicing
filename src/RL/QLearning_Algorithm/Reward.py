class Reward:
    def __init__(self, services, communication_units):
        self.services = services
        self.communication_units = communication_units

    def calculate_allocate_reward(self, request, action):
        for unit_ind, unit in enumerate(self.communication_units):
            if request in unit.connected_with:
                if action[unit_ind]==1:return 1
        return -1

    def calculate_assigen_reward(self, request, action):
        true_link = False
        for service_ind, service in enumerate(self.services):
            for unit in self.communication_units:
                if (unit in service.connected_with) and (request in unit.connected_with):
                    if action[service_ind]==1:
                        if request.service_required == service.service_type:return 1
                        else: true_link=True
        return 0 if true_link else -1
    
    def get_reward(self, agent_type, request, action):
        if agent_type=='allocator':
            r = self.calculate_allocate_reward(request, action)
            print(f"allocator reward {r}")
            return r
        elif agent_type=='assigner':
            r = self.calculate_assigen_reward(request, action)
            print(f"assigner reward {r}")
            return r