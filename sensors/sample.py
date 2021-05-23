from st2reactor.sensor.base import PollingSensor


class SampleSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=5):
        super(SampleSensor, self).__init__(sensor_service=sensor_service,
                                           config=config,
                                           poll_interval=poll_interval)
        self._poll_interval = 30

    def setup(self):
        pass

    def poll(self):

        # count = self.sensor_service.get_value('hello_st2.count') or 0
        # payload = {'greeting': 'Yo, StackStorm!', 'count': int(count) + 1}
        payload = {"success": "ok"}
        self.sensor_service.dispatch(
            trigger='syssignal.myevent', payload=payload)
        # self.sensor_service.set_value('hello_st2.count', payload['count'])

    def cleanup(self):
        pass
        # self._stop = True

        # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
