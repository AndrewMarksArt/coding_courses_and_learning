import time
from weakref import proxy

class Producer:
    """Defin the 'resource-intensive' object to instantiate!"""

    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now")


class Proxy:
    """Define the 'relatively less resource-intensive' proxy"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if the producer is available"""
        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            # if the producer is available create producer object
            self.producer = Producer()
            time.sleep(2)

            # make the producer meet the guest
            self.producer.meet()

        else:
            # dont istantiate the producer
            time.sleep(2)
            print("Producer is busy")


# instantiate proxy
p = Proxy()

# make the proxy
p.produce()

# change the state to 'occupied'
p.occupied = "Yes"

# make the producer produce
p.produce()

