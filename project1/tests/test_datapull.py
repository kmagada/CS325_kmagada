from unittest.mock import patch, MagicMock
from proj import datapull
import json

@patch("proj.datapull.http.client.HTTPSConnection")
def test_datapull_main(mock_conn):
    # Create mock connection instance
    mock_instance = mock_conn.return_value

    # Mock API response
    mock_instance.getresponse.return_value.read.return_value = json.dumps({
        "data": [{"job_id": "1"}]
    }).encode()

    datapull.main()

    # Ensure HTTPSConnection was called
    mock_conn.assert_called_once()
