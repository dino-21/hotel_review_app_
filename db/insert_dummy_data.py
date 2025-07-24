import sys
import os

# 현재 파일의 상위 폴더 경로를 모듈 탐색 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from sqlalchemy import create_engine, text
from config import DB_URI  # DB 접속 정보 가져오기

# config.py 파일이 없으면 자동으로 생성
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.py')
if not os.path.exists(config_path):
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write("DB_URI = 'mysql+pymysql://root:1234@localhost:3306/hotel'\n")

# 샘플 리뷰 리스트
sample_reviews = [
    "객실이 매우 깨끗하고 쾌적했어요.",
    "직원들이 친절하고 도움이 많이 됐습니다.",
    "조식이 정말 맛있었어요.",
    "관광지와 가까워 위치가 최고예요.",
    "수영장이 조금 작았어요.",
    "와이파이가 빠르고 안정적이었어요.",
    "룸서비스가 다소 느렸습니다.",
    "가격 대비 만족도가 높아요.",
    "다음에도 꼭 다시 방문하고 싶어요!",
    "침대가 너무 딱딱했어요.",
    "욕실이 매우 청결했습니다.",
    "밤에 옆방 소음이 심했어요.",
    "발코니 전망이 정말 멋졌어요.",
    "에어컨이 잘 작동했어요.",
    "주차장이 비쌌어요.",
    "스파 시설이 정말 좋았어요.",
    "체크인이 빠르고 편리했어요.",
    "미니바가 비어 있었어요.",
    "수건이 부드럽고 깨끗했어요.",
    "엘리베이터가 고장나서 불편했어요.",
]

# DB 연결 엔진 생성
engine = create_engine(DB_URI)

# DB에 연결하여 더미 데이터 120개 삽입
# 아래코드는 insert되고 commit이 안되고 롤백됨
# with engine.connect() as conn:
with engine.begin() as conn:   #  insert도 되고 commit도 되게
    for i in range(120):
        review = random.choice(sample_reviews)      # 랜덤 리뷰 선택
        sentiment = random.randint(1, 5)            # 감성 점수 1~5 랜덤 지정
        conn.execute(text("""
            INSERT INTO reviews (review_text, sentiment_score) 
            VALUES (:review, :sentiment)
        """), {"review": review, "sentiment": sentiment})

print("더미 데이터 120건(한국어) 삽입 완료.")
