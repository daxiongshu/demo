mkdir -p /raid/data/ml/kaggle/otto
cd /raid/data/ml/kaggle/otto
kaggle datasets download -d columbia2131/otto-chunk-data-inparquet-format
unzip otto-chunk-data-inparquet-format.zip
cd -
python data.py
