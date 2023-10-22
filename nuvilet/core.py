from datetime import datetime

class Massage:
    
    def send(self, name, msg):
        with open('massages.txt', 'a'):
            time = datetime.now().strftime("%X")
            data = f'{time}|{name}|{msg}\n'