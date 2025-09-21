data_pipeline/
│
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── api_client.py
│   │   ├── data_fetcher.py
│   │   └── data_validator.py
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   └── data_processor.py
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   └── data_saver.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api_client.py
│   ├── test_data_fetcher.py
│   ├── test_data_validator.py
│   └── test_data_processor.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── logs/
│   └── pipeline.log
│
├── requirements.txt
├── main.py
└── README.md