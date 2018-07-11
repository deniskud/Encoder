from encoder.DataEncoder import DataEncoder

class AbstractCommunication(object):
    def load(self):
        raise RuntimeError('No implementation')

    def save(self, data):
        raise RuntimeError('No implementation')

class File(AbstractCommunication):
    def __init__(self, filepath):
        self._path = filepath
        self._encoder = DataEncoder()

    def load(self):
        with open(self._path, 'r') as f:
            data = self._encoder.decode(f.read())
            return data

    def save(self, data):
        with open(self._path, 'rw') as f:
            raw = self._encoder.encode(data)
            f.write(raw)
            return True
