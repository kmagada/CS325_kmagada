from unittest.mock import patch, MagicMock
from proj import embedding

@patch("proj.embedding.OpenAI.embeddings.create")
def test_embed_resume(mock_embed):
    mock_embed.return_value.data = [MagicMock(embedding=[0.1, 0.2, 0.3])]

    fake_json = {
        "basics": {"name": "Kevin", "summary": "Dev"},
        "work": [],
        "education": [],
        "skills": [],
        "interests": []
    }

    import json, tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    with open(temp.name, "w") as f:
        json.dump(fake_json, f)

    result = embedding.embed_resume(temp.name)
    assert result == [0.1, 0.2, 0.3]

    mock_embed.assert_called_once()

    
@patch("proj.embedding.OpenAI.embeddings.create")
def test_embed_joblistings(mock_embed):
    mock_embed.return_value.data = [MagicMock(embedding=[9,9,9])]

    fake = {"data": [
        {"job_id": "X", "job_title": "Dev", "job_description": "Code"}
    ]}

    import json, tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    with open(temp.name, "w") as f:
        json.dump(fake, f)

    result = embedding.embed_joblistings(temp.name)

    assert result[0]["job_id"] == "X"
    assert result[0]["vector"] == [9,9,9]
