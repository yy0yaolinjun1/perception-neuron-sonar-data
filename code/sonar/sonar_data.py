from . import *
import pickle as pkl
import pandas as pd

class Sonar_Data:
    
    def __init__(self, data_file_path='', data_file_name='sonar_data.pkl'):
                
        self.data = []
        # YOUR_CODE
        self.label = []
        # self.data_file_path = data_file_path
        # self.data_file_name = data_file_name
        file = data_file_path+data_file_name
        #load the sonar data
        sonar_data = pd.read_pickle(file)
        r = list(sonar_data["r"])
        m = list(sonar_data["m"])
        #mark rock with 0 
        for i in r:
            i=list(i)
            self.label.append(0)
            self.data.append(i)
        #mark mine with 0
        for i in m:
            i=list(i)
            self.label.append(1)
            self.data.append(i)
            
            

        # self.shuffle()


    # def __iter__(self):
        
    #     return self

    # def __next__(self):
        
    #     YOUR_CODE
    def shuffle(self,seed=10):
        np.random.seed(seed)
        np.random.shuffle(self.data) 
        np.random.seed(seed)
        np.random.shuffle(self.label) 
    
    def __len__(self):
        
        return len(self.data)
