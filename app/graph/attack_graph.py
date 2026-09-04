class AttackGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_event(self, event):
        if event.event_id not in self.nodes:
            self.nodes[event.event_id] = event

    def add_relationship(self, event1, event2, probability):
        self.edges.append((event1.event_id, event2.event_id, probability))