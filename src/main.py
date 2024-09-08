from configtation import number_of_steps
from Graph.graph_communication import Graph

def main():
    for step in range(number_of_steps):
        graph = Graph()
        print(25*"#", step, 25*"#")
        for service in graph.services:
            print()
            print(f"-The service name: {service.Stype}, the number of connected units: {len(service.connected_with)}")
            for unit in service.connected_with:
                print(f" *    The unit id: {unit.id}, the number of connected requests: {len(unit.connected_with)}")

if __name__ == '__main__':
    main()