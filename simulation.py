from client import Client
class Simulation:
    def __init__(self, model, dataset, num_clients, aggregator, network=None, plotter=None):
        self.model = model
        self.dataset = dataset
        self.aggregator = aggregator
        self.network = network
        self.plotter = plotter
        
        self.clients = [Client(model, dataset.get_data_shard(i)) for i in range(num_clients)]
        
    def run(self):
        # Execute the simulation and intermediate results saving here.
        pass