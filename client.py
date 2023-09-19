class Client:
    def __init__(self, model, data_shard):
        self.model = model
        self.data = data_shard

    def local_training(self):
        # Local training of model with client's data
        pass

    def local_inference(self):
        # Perform inference using client's model
        pass
