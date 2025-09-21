country_data_pipeline/
│
├── main.py                 # Entry point
├── config.py              # Configuration settings
├── logger_config.py       # Logger setup
├── requirements.txt       # Dependencies
│
├── src/                   # Source code
│   ├── __init__.py
│   ├── api_client.py      # API calls with multithreading
│   ├── data_processor.py  # Data processing/validation
│   └── data_storage.py    # Save data to files
│
├── tests/                 # Pytest files
│   ├── __init__.py
│   └── test_data_validation.py
│
├── logs/                  # Log files (created at runtime)
│   └── pipeline.log
│
└── data/                  # Output data files (created at runtime)
    └── countries.json