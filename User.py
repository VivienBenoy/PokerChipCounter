
class User:
    def player_info(self,name,chipCount):
        self._name=name
        self._chipCount=chipCount

    def get_name(self):
        return self._name
    def get_chipCount(self):
        return self._chipCount
    def set_name(self,name):
        self._name=name
    def set_chipCount(self,chipCount):
        self._chipCount=chipCount