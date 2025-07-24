import sys
import os

# 상위 디렉토리(=프로젝트 루트)를 모듈 검색 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app  # Flask 앱(app.py) 불러오기

# 테스트용 클라이언트 설정 (Flask의 테스트 모드 활성화)
@pytest.fixture
def client():
    app.config['TESTING'] = True  # 테스트 모드 ON
    with app.test_client() as client:
        yield client  # 클라이언트를 호출하는 쪽에 넘겨줌

# 첫 번째 테스트: index 페이지 정상 동작 확인
def test_index_page(client):
    rv = client.get('/')  # GET 요청으로 메인 페이지 접속
    assert rv.status_code == 200  # HTTP 상태 코드가 200인지 확인
    assert '리뷰를 입력하세요' in rv.get_data(as_text=True)  # HTML에 해당 문구 포함되는지 확인

# 두 번째 테스트: 감성 분석 POST 요청 결과 확인
def test_sentiment_analysis(client):
    # POST 요청으로 리뷰 입력
    rv = client.post('/', data={'review': '객실이 매우 깨끗하고 쾌적했어요.'})
    assert rv.status_code == 200  # 응답 상태 코드 확인
    assert '감성 분석 결과' in rv.get_data(as_text=True)  # 결과 문구 포함되는지 확인

