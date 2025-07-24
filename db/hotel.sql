CREATE DATABASE IF NOT EXISTS hotel DEFAULT CHARACTER SET utf8mb4;
USE hotel;

CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_text TEXT NOT NULL,
    sentiment_score INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

use hotel;

desc reviews;


INSERT INTO reviews (review_text, sentiment_score) VALUES 
('객실이 넓고 청결해서 만족스러웠습니다.', 5),
('직원들이 불친절해서 실망스러웠어요.', 2),
('조식 종류가 다양하고 맛있었어요.', 4);

DELETE FROM reviews WHERE id = 125;

select * from reviews;

SELECT VERSION();

drop DATABASE hotel;
