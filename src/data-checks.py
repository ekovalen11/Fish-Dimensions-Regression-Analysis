import pandas as pd

def check_data_quality(df: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает сводную таблицу качества данных: типы, пропуски, уникальные значения.
    """
    quality = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing": df.isna().sum(),
        "unique": df.nunique(dropna=False),
    })
    return quality

def count_duplicates(df: pd.DataFrame) -> int:
    """
    Возвращает количество полных дубликатов строк.
    """
    return len(df) - len(df.drop_duplicates())

def find_zero_weight(df: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает строки, где вес равен 0 (физическая аномалия).
    """
    return df[df['Weight'] == 0]