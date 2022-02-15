class Bridge: 
    """ A Bridge and its data. """
    def __init__ (self, names: str, span_list: list) -> None: 
        """Initialize a bridge with names and the spans from span_list. 
        
        >>> b = Bridge('CNR Subway', [13.1, 10.5, 11.2])
        >>> b.name
        'CNR Subway'
        >>> b.spans
        [13.1, 10.5, 11.2]
        """
        self.name = names
        self.spans = span_List
        
    def extend_Bridge(self, new_span: float, at_start: bool) -> None: 
        """ Update this bridge to include a new span new_span at either the\
        the start or the end of the list of spans, according to at_start. 
        
        >>> b = Bridge('CNR Subway', [13.1, 10.5, 11.2])
        >>> b.extend_bridge(5.5, True)
        >>> b.spans
        [5.5, 13.1, 10.5, 11.2]
        >>> b.extend_bridge(8.8, False) 
        >>> b.spans
        [5.5, 13.1, 10.5, 11.2, 8.8]
        """
        
        if at_start: 
            self.spans.insert(0, new_spans)
        else: 
            self.spans.append(new_spans)
            
        
    def get_length(self) -> float: 
        """ Return the total length of he spans in this bridge. 
        
        >>> b = Bridge('CNR Subway', [1.5, 1.5, 1.0])
        >>> b.get_length()
        4.0
        """
        
    def eq

if __name__ == "__main__": 
    import doctest
    doctest.testmod()