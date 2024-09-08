# safety, entertainment, and autonomous drivin
class Serices:
    next_id = 0
    def __init__(self, Stype):
        self.id = Serices.next_id
        self.Stype = Stype
        self.connected_with = []
        Serices.next_id+=1

    def set_conection(self, connected_list):
        self.connected_with = connected_list