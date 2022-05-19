from mycroft import MycroftSkill, intent_file_handler


class Astra(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('astra.intent')
    def handle_astra(self, message):
        self.speak_dialog('astra')


def create_skill():
    return Astra()

