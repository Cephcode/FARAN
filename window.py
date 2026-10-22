from event_detector import EventDetector
class Window():

    def __init__(self,event_detector:EventDetector) -> None:
        self.list=[]
        self.event_detector=event_detector

    def push(self,power:float):
        self.list.append(power)

        if len(self.list)>=26:
            self.list.pop()
        self.event_detector.push_power(self.list)
        
