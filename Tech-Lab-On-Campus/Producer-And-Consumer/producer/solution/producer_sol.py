from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):

    def __init__(self: mqProducerInterface, routing_key: str, exchange_name: str) -> None:
        # Save parameters to instance variable
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        

    def test(self):
        
        self.setupRMQConnection()
        self.publishOrder()

    #def bark(self: mqProducerInterface) -> None:
        # Print {name of dog} is barking!
        #print(self.name, "")