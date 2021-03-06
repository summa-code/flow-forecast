import unittest
import os 
import torch
import pandas as pd
from datetime import datetime
from flood_forecast.preprocessing.pytorch_loaders import CSVTestLoader

class DataLoaderTests(unittest.TestCase):
    """
    Class to test data loader functionality for the code.
    Specifically, reuturn types and indexing to make sure.
    """
    def setUp(self):
        self.test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"test_data")
        data_base_params = {"file_path":os.path.join(self.test_data_path, "keag_small.csv"), "forecast_history": 20, "forecast_length":20, "relevant_cols":["cfs", "temp", "precip"], "target_col":["cfs"], "interpolate_param": False}
        self.test_loader = CSVTestLoader(os.path.join(self.test_data_path, "keag_small.csv"), 336, **data_base_params)

    def test_loader2_get_item(self):
        src, df, forecast_start_index = self.test_loader[0]  
        self.assertEqual(type(src), torch.Tensor)
        self.assertEqual(forecast_start_index, 20)
        self.assertEqual(df.iloc[2]['cfs'], 445)
        self.assertEqual(len(df), 356)
    
    def test_loader2_get_date(self):
        src, df, forecast_start_index, = self.test_loader.get_from_start_date(datetime(2014, 6, 3, 0))
        self.assertEqual(type(src), torch.Tensor)
        self.assertEqual(forecast_start_index, 783)
        self.assertEqual(df.iloc[0]['datetime'].day, datetime(2014, 6, 2, 4).day)

if __name__ == '__main__':
    unittest.main()
    


   
    