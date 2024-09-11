# safety, entertainment, and autonomous drivin
class Service:
    next_id = 0
    def __init__(self, service_type):
        self.id = Service.next_id
        self.service_type = service_type
        self.connected_with = []
        Service.next_id+=1

    def set_conection(self, connected_list):
        self.connected_with = connected_list