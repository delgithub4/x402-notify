class AuditLogger:

    def __init__(self):

        self.records = []

    def record(
        self,
        event,
    ):

        self.records.append(event)
