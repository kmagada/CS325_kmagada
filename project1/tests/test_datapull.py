from unittest.mock import patch, MagicMock
import datapull
import json

@patch("datapull.http.client.HTTPSConnection")
def test_datapull_main(mock_conn):
    mock_instance = mock_conn.return_value
    mock_instance.getresponse.return_value.read.return_value = json.dumps({
        "data": [{"job_id": "1"}]
    }).encode()

    datapull.main()

    mock_conn.assert_called_once()
