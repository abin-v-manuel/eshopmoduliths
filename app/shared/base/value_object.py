 
class ValueObject:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__