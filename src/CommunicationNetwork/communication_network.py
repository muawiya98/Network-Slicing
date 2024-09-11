# Satellites, Wi-Fi, 3G, 4G, 5G
class CommunicationNetwork:
    next_id = 0
    def __init__(self, communication_type):
        self.id = CommunicationNetwork.next_id
        self.communication_type = communication_type
        self.connected_with = []
        CommunicationNetwork.next_id+=1

    def set_conection(self, connected_list):
        self.connected_with = connected_list

