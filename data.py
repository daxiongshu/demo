from dask_utils import get_cluster
import dask_cudf
PATH = '/raid/data/ml/kaggle/otto'

def sort_ts(df):
    return df.sort_values(['session','ts']).reset_index(drop=True)

def combine_parquets(tag):
    df = dask_cudf.read_parquet(f'{PATH}/{tag}_parquet/*.parquet')
    df = df.compute()
    df = sort_ts(df)
    for col in ['session','aid']:
        df[col] = df[col].astype('int32')
    df.to_parquet(f'{PATH}/{tag}.parquet')

def combine_all_parquets():
    client = get_cluster()
    for tag in ['train','test']:
        combine_parquets(tag)

if __name__ == '__main__':
    combine_all_parquets()

