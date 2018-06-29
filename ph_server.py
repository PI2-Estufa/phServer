from nameko.rpc import rpc
import db
from db import Ph
from psycopg2 import OperationalError


class PhServer():
    name = "ph_server"

    @rpc
    def receive_ph(self, ph):
        ph = round(ph, 1)
        p = Ph()
        p.value = ph
        try:
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return ph
