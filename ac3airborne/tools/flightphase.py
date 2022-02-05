import warnings
from datetime import datetime

class FlightPhaseFile(object):
    """
    The FlightPhaseFile object stores the yaml content of a flight phase file
    and offers some methods used to query specific flight segments based on
    some properties.

    Parameters
    ----------
    yaml_content : object
        The object returned by ac3airborne.get_flight_segments() after having
        specified research aircraft and research flight.
    """


    def __init__(self, yaml_content):
        super(FlightPhaseFile, self).__init__()
        self.ds = yaml_content

    def irregularities(self, segments):
        for s in segments:
            if s.get('irregularities'):
                str = 'the segment ' + s.get('segment_id') + ' contains following irregularities: '
                str += ''.join(s.get('irregularities'))
                warnings.warn(str)
        pass

    def select(self, attribute, value, invertSelection=False, strict=False):
        """
        The method select just selects all flight segments that have a specific
        value for a specific attribute in the flight phase file. It is the most
        generic method of this class, but it only works with one value for one
        attribute.

        Parameters
        ----------
        attribute : str
            A valid attribute name used in the flight phase file.
        value
            A valid value for the specified attribute. The type of this
            parameter depends on the specified attribute and must match the type
            found in the yaml file.
        invertSelection : bool, optional
            If is set to True it inverts the selection and return all flight
            segments that don't match the given value for the given attribute.
            Default is False.
        strict: bool, optional
            An argument in the flight phase file can contain a list of values
            instead of only one value. The normal behavior of this method is to
            select all segments where the given values appears, also those,
            where the value is in a list together with other values. Setting
            this parameter to True will change the default behavior and the
            method will select only those segments, where the given value is the
            only value of attribute. An example could be the attribute "level".
            The normal behavior would be to select not only the segments at the
            specified height, but also the "ascend" and "descend" segments that
            include the specified level as the starting or ending level. Setting
            this parameter to True would cause the method to return only the
            segments at constant height without "ascends" and "descends".

        Returns
        -------
        segments: list
            A list of dictionaries each containing a segment.
        """
        if strict:
            if invertSelection:
                segments = [s for s in self.ds['segments'] if s.get(attribute) != [value]]
            else:
                segments = [s for s in self.ds['segments'] if s.get(attribute) == [value]]
        else:
            if invertSelection:
                segments = [s for s in self.ds['segments'] if not(s.get(attribute) and value in s.get(attribute))]
            else:
                segments = [s for s in self.ds['segments'] if s.get(attribute) and value in s.get(attribute)]
        self.irregularities(segments)
        return segments

    def selectKind(self, kind, invertSelection=False, parts=True):
        """
        The method selectKind is designed for selecting one or more kinds. You
        can achieve the same result by using the select method, but you will end
        up calling the select method a lot of times if you need more than one
        kind at once since the select method only allows an attribute-value
        pair. The selectKind method takes a list instead.

        Parameters
        ----------
        kinds : list
            A list of values for the keyword "kinds". Please see the reference
            for the keyword "kinds" on the how_to_ac3airborne Jupyter Book.
        invertSelection : bool, optional
            If is set to True it inverts the selection and return all flight
            segments that don't match the given value for the given attribute.
            Default is False.
        parts : bool, optional
            Whether include the "parts" of a pattern in the search.
            Default is True.

        Returns
        -------
        segments: list
            A list of dictionaries each containing a segment.
        """
        if parts:
            if invertSelection:
                segments = [s for s in self.ds['segments'] if not any(item in kind for item in s.get('kinds'))]
                partslst = []
                for s in self.ds['segments']:
                    if s.get('parts') != None:
                        for p in s.get('parts'):
                            if not any(item in kind for item in s.get('kinds')):
                                partslst.append(p)
            else:
                segments = [s for s in self.ds['segments'] if any(item in kind for item in s.get('kinds'))]
                partslst = []
                for s in self.ds['segments']:
                    if s.get('parts') != None:
                        for p in s.get('parts'):
                            if any(item in kind for item in p.get('kinds')):
                                partslst.append(p)
            segments.extend(partslst)
        else:
            if invertSelection:
                segments = [s for s in self.ds['segments'] if not any(item in kind for item in s.get('kinds'))]
            else:
                segments = [s for s in self.ds['segments'] if any(item in kind for item in s.get('kinds'))]
        self.irregularities(segments)
        return segments

    def selectDropSondes(self, type):
        """
        The method selectDropSondes is used for searching for flight segments,
        which contains dropsondes of a specific type.

        Parameters
        ----------
        type : str
            Dropsondes in the flight phase file can be of the type "GOOD", "BAD"
            and "UGLY".

        Returns
        -------
        segments: list
            A list of dictionaries each containing a segment.
        """
        segments = [s for s in self.ds['segments'] if s.get('dropsondes') and s['dropsondes'][type]]
        self.irregularities(segments)
        return segments

    def findSegments(self, starttime, endtime):
        """
        The method findSegments is used for searching for flight segments,
        which are contained in a specific range of time.

        Parameters
        ----------
        starttime : str
            String containing the start time in the '%Y-%m-%d %H:%M:%S' format.
        endtime: str
            String containing the end time in the '%Y-%m-%d %H:%M:%S' format.

        Returns
        -------
        segments: list
            A list of dictionaries each containing a segment.
        """
        start_t  = datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
        end_t    = datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
        segments = [s for s in self.ds['segments'] if (s['start'] <= end_t) and (s['end'] >= start_t)]
        self.irregularities(segments)
        return segments
