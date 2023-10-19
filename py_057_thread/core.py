from datetime import datetime

class Message:

    def send(self, name, msg):
        with open("messages.txt", 'a', encoding='utf-8') as f:
            time = datetime.now().strftime("%X")
            data = f'{time}|{name}|{msg}\n'
            f.write(data)


    def getAll(self):
        with open("messages.txt", "r", encoding='utf-8') as f:
            data = f.read().split('\n')[:-1]
            data = list(map(lambda item : item.split('|'), data))
            data = list(map(lambda item : {'time': item[0], 'name' : item[1], 'msg' : item[2]}, data))
            return data
            

