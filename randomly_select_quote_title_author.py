import csv 
import logging 
from datetime import datetime 
import random

def randomly_select_quote_title_author() -> tuple[str, str, str]:

    # Figure out the current time
    now = datetime.now()
    now_str = f"{now.hour:02}:{now.minute:02}"
    logging.debug(f"Selected time: {now_str}")
    
    # Load the file containing the relevant quotes
    with open(f"data/quotes/{now_str}.csv", newline='') as f:
        reader = csv.reader(f)
        csv_rows = list(reader)

    # Randomly select one row
    selected_row_idx = random.randint(0, len(csv_rows)-1)
    selected_csv_row = ''.join(csv_rows[selected_row_idx])   
    
    _, quote, title, author = selected_csv_row.split('|')
    
    # Fix endlines
    quote = quote.replace('<br/>', '\n')
    
    return quote, title, author
