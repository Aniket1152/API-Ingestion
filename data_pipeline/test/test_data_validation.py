import pytest
from src.data_processor import validate_country_data, process_countries_data

def test_valid_country_data():
    """Test validation with valid data"""
    valid_country = {
        "name": {"common": "Test Country", "official": "Official Test Country"},
        "population": 1000000,
        "region": "Test Region",
        "capital": ["Test Capital"]
    }
    assert validate_country_data(valid_country) == True

def test_invalid_country_data_missing_fields():
    """Test validation with missing fields"""
    invalid_country = {
        "name": {"common": "Test Country"},
        # missing population
    }
    assert validate_country_data(invalid_country) == False

def test_invalid_country_data_wrong_type():
    """Test validation with wrong data type"""
    invalid_country = {
        "name": {"common": "Test Country"},
        "population": "not_a_number"
    }
    assert validate_country_data(invalid_country) == False

def test_process_countries_data():
    """Test processing function"""
    test_data = [
        {
            "name": {"common": "Country A", "official": "Official A"},
            "population": 1000000,
            "region": "Region A",
            "capital": ["Capital A"]
        },
        {
            "name": {"common": "Country B"},
            "population": 2000000
            # missing some fields but still valid
        }
    ]
    
    result = process_countries_data(test_data)
    assert len(result) == 2
    assert 'name' in result[0]
    assert 'population' in result[0]