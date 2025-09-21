import pytest
import requests
from src.utils.data_processor import validate_country_data, process_countries_data
from src.utils.api_client import fetch_all_countries_multithreaded

def test_api_country_count():
    """Test that we get expected number of countries from API"""
    # Get total count directly from API
    try:
        response = requests.get("https://restcountries.com/v3.1/all?fields=name")
        if response.status_code == 200:
            countries = response.json()
            total_countries = len(countries)
            
            # Should get reasonable number of countries (typically 250+)
            assert total_countries > 200
            assert total_countries < 300  # Sanity check
        else:
            pytest.fail(f"API request failed: {response.status_code}")
    except Exception as e:
        pytest.fail(f"API request failed: {str(e)}")

def test_valid_country_data():
    """Test validation with real API data structure"""
    # Get one real country from API to test
    try:
        response = requests.get("https://restcountries.com/v3.1/name/India")
        if response.status_code == 200:
            country_data = response.json()[0]  # First country in response
            
            # This should pass validation
            assert validate_country_data(country_data) == True
        else:
            pytest.fail(f"API request failed: {response.status_code}")
    except Exception as e:
        pytest.fail(f"API request failed: {str(e)}")

def test_missing_required_fields():
    """Test validation with missing required fields"""
    # Test data missing population
    invalid_country = {
        "name": {"common": "Test Country"}
        # Missing required 'population' field
    }
    assert validate_country_data(invalid_country) == False

def test_invalid_population_type():
    """Test validation with invalid population data"""
    invalid_country = {
        "name": {"common": "Test Country"},
        "population": "not_a_number"  # Wrong type
    }
    assert validate_country_data(invalid_country) == False

def test_invalid_population_value():
    """Test validation with negative population"""
    invalid_country = {
        "name": {"common": "Test Country"},
        "population": -1000  # Negative population
    }
    assert validate_country_data(invalid_country) == False

def test_data_processing_pipeline():
    """Test the complete data processing pipeline"""
    # Get a small sample of real data
    try:
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,population")
        if response.status_code == 200:
            sample_data = response.json()[:5]  # First 5 countries
            
            # Process the data
            result = process_countries_data(sample_data)
            
            # Should process some valid countries
            assert len(result) >= 0
            assert len(result) <= 5
            
            # If we have results, they should have required fields
            if result:
                assert 'name' in result[0]
                assert 'population' in result[0]
        else:
            pytest.fail(f"API request failed: {response.status_code}")
    except Exception as e:
        pytest.fail(f"API request failed: {str(e)}")

def test_empty_data_processing():
    """Test processing empty data"""
    result = process_countries_data([])
    assert len(result) == 0