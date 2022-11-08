import abc

class TelemetryRepository(abc.ABC):

    @abc.abstractmethod
    def create(self):
        raise NotImplementedError
    

class BigQueryTelemetry(TelemetryRepository):

    def create(self):
        pass

if __name__ == "__main__":
    b = BigQueryTelemetry()