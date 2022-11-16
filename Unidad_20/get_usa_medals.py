import pandas as pd

def get_usa_medals() -> pd.core.frame.DataFrame:
    """Get subset with all gold medals, USA from the year 1950 onwards.

    Returns:
        Dataframe: Gold medals of USA from 1950.
    """
    url = 'http://winterolympicsmedals.com/medals.csv'
    df = pd.read_csv(url)
    US_Gold = df[(df.Year >= 1950) & (df.Medal=='Gold') & (df.NOC == 'USA')]
    return US_Gold
