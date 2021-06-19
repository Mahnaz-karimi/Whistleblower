from django import urls
import pytest

url_data = [
    ('case:caseinfo-view', 302),
    ('case:report-login', 200),
    ('case:revisit-login', 200),
]


@pytest.mark.parametrize("url, expected", url_data)
def test_case_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)
    assert resp.status_code == expected
