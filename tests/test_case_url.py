from django import urls
import pytest


url_data = [
    ('case:caseinfo-view', 302),
    ('case:report-login', 200),
    ('case:revisit-login', 200),
]


@pytest.mark.parametrize("u, expected", url_data)
def test_logged_views(client, u, expected, user_data1):
    temp_url = urls.reverse(u)
    resp = client.get(temp_url)
    assert resp.status_code == expected
