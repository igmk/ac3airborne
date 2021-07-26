class FlightPhaseFile(object):
    """docstring for FlightPhaseFile."""

    def __init__(self, yaml_content):
        super(FlightPhaseFile, self).__init__()
        self.ds = yaml_content

    def select(self, attribute, value, invertSelection=False, strict=False):
        if strict:
            if invertSelection:
                return [s for s in self.ds['segments'] if s.get(attribute) != [value]]
            else:
                return [s for s in self.ds['segments'] if s.get(attribute) == [value]]
        else:
            if invertSelection:
                #
                return [s for s in self.ds['segments'] if not(s.get(attribute) and value in s.get(attribute))]
            else:
                return [s for s in self.ds['segments'] if s.get(attribute) and value in s.get(attribute)]

    def selectKind(self, kind, invertSelection=False):
        if invertSelection:
            return [s for s in self.ds['segments'] if not any(item in kind for item in s.get('kinds'))]
        else:
            return [s for s in self.ds['segments'] if any(item in kind for item in s.get('kinds'))]

    def selectDropSondes(self, type):
        return [s for s in self.ds['segments'] if s.get('dropsondes') and s['dropsondes'][type]]
