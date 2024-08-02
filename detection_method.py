from abc import ABC, abstractmethod

class detection_method(ABC):
    '''
    Make sure to implement a `weight` for each class or else there will be crashes :-<
    '''

    @abstractmethod
    def start(self):
        '''
        Used to setup your detection method.
        Use for loading models, connecting to urls, etc.
        '''
        pass

    @abstractmethod
    def compute(self, values, index):
        '''
        Use this method to do computations for calculating the value.
        Then set the `value[index] = your result`
        '''
        pass

    @abstractmethod
    def shutdown(self):
        '''
        Use this to safely shutdown your detection method. This 
        could be unloading a resource, wrting to a file, etc.
        '''
        pass