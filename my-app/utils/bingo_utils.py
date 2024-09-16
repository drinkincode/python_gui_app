import flet as ft
from utils.csv_utils import write_csv, read_csv

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
