
class EventBus:
    def __init__(self):
        self._listeners = {}

    def subscribe(self, event_type: str, callback):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def emit(self, event_type: str, *args, **kwargs):
        for callback in self._listeners.get(event_type, []):
            callback(*args, **kwargs)

event_bus = EventBus()