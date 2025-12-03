from unittest.mock import patch, MagicMock
import main

@patch("main.ranking.rank_top_jobs")
@patch("main.embedding.embed_resume")
@patch("main.embedding.embed_joblistings")
@patch("main.datapull.main")
def test_main_pipeline(mock_datapull, mock_embed_jobs, mock_embed_resume, mock_rank):
    mock_embed_jobs.return_value = [{"job_id": "1", "vector": [1,2,3], "metadata": {}}]
    mock_embed_resume.return_value = [1,2,3]
    mock_rank.return_value = ["top"]

    main.main()

    mock_datapull.assert_called_once()
    mock_embed_jobs.assert_called_once()
    mock_embed_resume.assert_called_once()
    mock_rank.assert_called_once()
