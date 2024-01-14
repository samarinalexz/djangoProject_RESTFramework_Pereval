from Pereval.views import PerevalCreateViewset, PerevalUpdateViewset, PerevalListView, PerevalUserListViewset

tests = []


def test_create_pereval():
    result = PerevalCreateViewset.create('kek')
    assert isinstance(result, PerevalCreateViewset)
    assert result in tests


def test_update_pereval():
    result = PerevalUpdateViewset.pereval_update('kek')
    assert isinstance(result, PerevalUpdateViewset)
    assert result in tests


def test_find_pereval():
    to_find_one = PerevalCreateViewset.create('kek')
    not_found_pereval = PerevalCreateViewset.create('lol')
    to_find_two = PerevalCreateViewset.create('keke')
    search_result = PerevalListView.get('ke')
    assert to_find_one in search_result
    assert to_find_two in search_result
    assert not_found_pereval in search_result


def test_find_user_by_email():
    to_find_one = PerevalCreateViewset.create('kek')
    not_found_pereval = PerevalCreateViewset.create('lol')
    to_find_two = PerevalCreateViewset.create('keke')
    search_result = PerevalUserListViewset.get('ke')
    assert to_find_one in search_result
    assert to_find_two in search_result
    assert not_found_pereval in search_result



