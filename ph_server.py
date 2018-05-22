from nameko.rpc import rpc
from nameko.messaging import Publisher
from kombu import Exchange, Queue
import db
from db import Ph

exchange = Exchange("main", "direct", durable=True)
queue = Queue("ph_queue", exchange=exchange)

class PhServer():
    name = "ph_server"
    publish = Publisher(exchange=exchange, queue=queue)

    @rpc
    def receive_ph(self, ph):
        self.publish(ph)
        return ph
