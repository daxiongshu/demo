kaggle competitions download -c amex-default-prediction -f train_labels.csv -p /raid/data/ml/kaggle/amex
kaggle datasets download -d raddar/amex-data-integer-dtypes-parquet-format -p /raid/data/ml/kaggle/amex
mkdir -p /raid/data/ml/kaggle/amex
cd /raid/data/ml/kaggle/amex
unzip *.zip
mkdir processed models
