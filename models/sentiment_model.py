from transformers import pipeline

# 감성 분석용 파이프라인 생성
# 'nlptown/bert-base-multilingual-uncased-sentiment'는 다국어 리뷰에 적합한 사전학습 모델
sentiment_pipeline = pipeline(
    'sentiment-analysis',
    model='nlptown/bert-base-multilingual-uncased-sentiment'
)

# 실제 감성 분석 함수 정의
def analyze_sentiment(text):
    result = sentiment_pipeline(text)  # 입력 텍스트 분석 → 예: [{'label': '4 stars', 'score': 0.7}]
    
    label = result[0]['label']         # 예: '4 stars' 라는 문자열만 추출
    score = int(label[0])              # 문자열에서 첫 글자인 숫자만 추출 → '4 stars' → 4
    return score                       # 숫자(별점)만 반환


