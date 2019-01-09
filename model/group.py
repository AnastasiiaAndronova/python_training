from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

# метод определяет как будут выглядеть обьекты при выводе на консоль
    def __repr__(self):
        return "id = [%s] name = [%s] header = [%s] footer = [%s]" % (self.id, self.name, self.header, self.footer)

# метод сравнения
#     def __eq__(self, other):
#
#         if self.name == other.name:
#             if self.id is None:
#                 return True
#             if other.id is None:
#                 return True
#             if self.id == other.id:
#                 return True
#         return False

    def __eq__(self, other):
        return ( self.id is None or  other.id is None or self.id== other.id) and self.name==other.name

    def id_or_max(self):
     #   if self.id:
     #       return int(self.id)
        return maxsize
