import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api): 
    repo = github_api.search_repo('become-qa-auto')  
    assert repo['total_count'] == 42

@pytest.mark.api
def test_repo_cannot_be_found(github_api):    
    repo = github_api.search_repo('vyshyvana_repo')
    assert repo['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api): 
    repo = github_api.search_repo('v')
    assert repo['total_count'] != 0

@pytest.mark.api
def test_project_id_not_exists(github_api):
    r = github_api.get_project_id('111')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_commits_exist(github_api):
    commits = github_api.get_commit('viktoriavysh','vyshyvanaqaauto')
    assert len(commits) > 0

@pytest.mark.api
def test_commit_exists(github_api):
    commit = github_api.get_commit('viktoriavysh','vyshyvanaqaauto')
    assert commit[0]['sha'] == '2ba767de895f4f108b014f3c24f1ca346abf46bf'