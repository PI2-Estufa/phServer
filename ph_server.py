from nameko.rpc import rpc
import db
from db import Ph


class PhServer():
    name = "ph_server"

    @rpc
    def receive_ph(self, ph):
        ph = round(ph, 1)
        p = Ph()
        p.value = ph
        db.session.add(p)
        db.session.commit()
        return ph
