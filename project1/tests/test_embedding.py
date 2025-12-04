from unittest.mock import patch, MagicMock
from proj import embedding
import json
import tempfile

def test_embed_resume():
    # Create a fake OpenAI client with a mock embeddings.create
    mock_client = MagicMock()
    mock_client.embeddings.create.return_value.data = [MagicMock(embedding=[0.1, 0.2, 0.3])]

    # Patch the OpenAI client inside your module to use the mock
    with patch("proj.embedding.OpenAI", return_value=mock_client):
        fake_json = {
            "basics": {"name": "Kevin", "summary": "Dev"},
            "work": [],
            "education": [],
            "skills": [],
            "interests": []
        }

        with tempfile.NamedTemporaryFile("w", delete=False) as temp:
            json.dump(fake_json, temp)
            temp_path = temp.name

        result = embedding.embed_resume(temp_path)
        assert result == [0.1, 0.2, 0.3]

        mock_client.embeddings.create.assert_called_once()


def test_embed_joblistings():
    # Create a fake OpenAI client with a mock embeddings.create
    mock_client = MagicMock()
    mock_client.embeddings.create.return_value.data = [MagicMock(embedding=[9, 9, 9])]

    # Patch the OpenAI client inside your module to use the mock
    with patch("proj.embedding.OpenAI", return_value=mock_client):
        fake = {"data": [
            {"job_id": "X", "job_title": "Dev", "job_description": "Code"}
        ]}

        with tempfile.NamedTemporaryFile("w", delete=False) as temp:
            json.dump(fake, temp)
            temp_path = temp.name

        result = embedding.embed_joblistings(temp_path)
        assert result[0]["job_id"] == "X"
        assert result[0]["vector"] == [9, 9, 9]

        mock_client.embeddings.create.assert_called_once()
