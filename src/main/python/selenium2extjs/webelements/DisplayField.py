'''
'''
from selenium2extjs.webelements.Field import Field


class DisplayField(Field):
    '''
    display field
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = "inputEl"
        super(Field, self).__init__(driver, query_type, query, top_element)
