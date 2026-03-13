import logging
import socket
import json


class LogstashHandler(logging.Handler):

    def emit(self, record):

        log_entry = self.format(record)

        data = json.dumps({
            "message": log_entry,
            "level": record.levelname
        })

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect(("logstash", 5000))
            sock.send(data.encode("utf-8"))
        except:
            pass

        sock.close()


logger = logging.getLogger("medical_ai")

handler = LogstashHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.INFO)