import logging

import pandas as pd
from zenml import step

class IngestData:
    """
    Ingesting the data from the data path
    """
    
    def __init__(self, data_path: str):
        """
        Args: path to the data
        """
        self.data_path = data_path

    def get_data(self):
        """
        Ingesting the data from the data path

        Returns: The ingested data
        """
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path, index_col=0, parse_dates=True)

@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingesting the data from data_path

    Args: path to the data
    Returns: the ingested data
    """
    try:
        # Instantiate the IngestData class with the data path
        ingest_data = IngestData(data_path)
        # Call the get_data method to fetch the data
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e 