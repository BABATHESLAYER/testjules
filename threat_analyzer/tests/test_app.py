import pytest
from threat_analyzer.app import app
import io
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Upload PDF for Threat Analysis" in rv.data

@patch('threat_analyzer.app.extract_text_from_pdf')
@patch('threat_analyzer.app.extract_information')
def test_upload_file(mock_extract_info, mock_extract_text, client):
    """Test file upload and analysis."""
    mock_extract_text.return_value = "This is a test text with critical threat."
    mock_extract_info.return_value = [{'name': 'Test Threat', 'industry': 'Financial', 'country': 'United States', 'threat_type': 'malware', 'severity': 'Critical'}]

    data = {
        'file': (io.BytesIO(b"dummy pdf content"), 'test.pdf')
    }
    rv = client.post('/upload', data=data, content_type='multipart/form-data')
    assert rv.status_code == 200
    assert rv.json == [{'name': 'Test Threat', 'industry': 'Financial', 'country': 'United States', 'threat_type': 'malware', 'severity': 'Critical'}]
