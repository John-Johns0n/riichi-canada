import pandas as pd
from sqlalchemy import create_engine


def import_event_results_data(csv_path: str, db_path: str) -> None:
    event_df = pd.read_csv(csv_path)
    engine = create_engine(db_path)
    event_df.to_sql('event_results', engine, if_exists='append', index=False)