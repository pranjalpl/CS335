import json
printerTab = 1
class symbolTable:
    def __init__(self):
        self.table = {}
        self.globalSymbolList = []
        self.parent = None
        self.extra = {}

    # Checks whether "name" lies in the symbol table
    def lookUp(self, name):
        return (name in self.table)

    # Inserts if already not present
    def insert(self, name, typeOf):
        if (not self.lookUp(name)):
            (self.table)[name] = {}
            self.globalSymbolList.append(name)
            (self.table)[name]["type"] = typeOf
        # else:
        #     raise NameError(name + ' is already defined')

    # Returns the argument list of the variable else returns None
    # Note that type is always a key in argument list
    def getInfo(self, name):
        if (self.lookUp(name)):
            return (self.table)[name]
        else:
            return None

    # Updates the variable of NAME name with arg list of KEY key with VALUE value
    def updateArgList(self, name, key, value):
        if (self.lookUp(name)):
            (self.table)[name][key] = value
        else:
            raise KeyError("Symbol " + name + " doesn't exists - Cant Update")

    def setParent(self, parent):
        self.parent = parent

    def updateExtra(self,key,value):
        self.extra[key]=value

    def formatToJSON(self, d):
        global printerTab
        s = ['{\n']
        for k,v in d.items():
            if isinstance(v, dict):
                printerTab = printerTab + 1
                v = self.formatToJSON(v)
                printerTab = printerTab - 1
            else:
                if k == 'child':
                    printerTab = printerTab + 1
                v = repr(v)
                if k == 'child':
                    printerTab = printerTab - 1

            s.append('%s%r: %s,\n' % ('\t'*printerTab, k, v))
        s.append('%s}' % ('\t'*(printerTab-1)))
        return ''.join(s)
    
    def __repr__(self):
        ret = {
            'table': (self.table),
            'global_symbols': self.globalSymbolList,
            'parent': self.parent,
            'extras': self.extra
        }
        return self.formatToJSON(ret)

