from flask import Flask, render_template, request, redirect, url_for
from models.sentiment_model import analyze_sentiment  # 감성 분석 함수 불러오기
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import DB_URI
import os

app = Flask(__name__)

# DB 연결 설정
engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 폼에서 입력된 리뷰 텍스트 추출
        review = request.form['review']
        # 감성 점수 분석
        sentiment = analyze_sentiment(review)

        # 리뷰 및 감성 점수를 DB에 저장
        with engine.begin() as conn:
            conn.execute(text("""
                INSERT INTO reviews (review_text, sentiment_score) VALUES (:review, :sentiment)
            """), {"review": review, "sentiment": sentiment})

        # 유사 감성 점수를 가진 리뷰 5개 추천
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT review_text, sentiment_score FROM reviews
                WHERE ABS(sentiment_score - :sentiment) <= 1
                ORDER BY ABS(sentiment_score - :sentiment) ASC
                LIMIT 5
            """), {"sentiment": sentiment})
            recommendations = result.fetchall()

        # 결과 페이지 렌더링
        return render_template('result.html', review=review, sentiment=sentiment, recommendations=recommendations)

    # GET 요청: 최신 리뷰 20개 조회해서 화면에 출력
    with engine.connect() as conn:
        result = conn.execute(text("SELECT review_text, sentiment_score FROM reviews ORDER BY id DESC LIMIT 20"))
        review_list = result.fetchall()

    # 메인 페이지 렌더링
    return render_template('index.html', review_list=review_list)

# 앱 실행 (개발 모드)
if __name__ == '__main__':
    app.run(debug=True)
