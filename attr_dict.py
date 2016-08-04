# CRISTIAN ECHEVERRÍA RABÍ

#---------------------------------------------------------------------------------------------------

class AttrDict(dict):

    def __init__(self):
        super().__init__()
        protected = dir(dict)
        protected.append("_protected")
        super().__setattr__("_protected", protected)
    
    def __getattr__(self, key):
        return self[key]
    
    def __setattr__(self, key, value):
        if (key in self._protected):
            raise AttributeError("'%s' no se puede usar como field" % (key,))
        self[key] = value