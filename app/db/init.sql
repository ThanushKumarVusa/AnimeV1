CREATE DATABASE IF NOT EXISTS anime_world;
USE anime_world;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS anime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(100),
    description TEXT
);

INSERT IGNORE INTO users (username, password)
VALUES ('thanush', 'anime123');

INSERT INTO anime (title, genre, description) VALUES
('One Piece','Adventure, Fantasy','Follow Monkey D. Luffy and his crew on their journey to find the legendary One Piece.'),
('Naruto','Action, Adventure','Naruto Uzumaki dreams of becoming Hokage while overcoming challenges and growing stronger.'),
('Demon Slayer','Action, Fantasy','Tanjiro Kamado begins a dangerous journey to save his sister and fight demons.'),
('Jujutsu Kaisen','Action, Supernatural','Yuji Itadori enters the world of Jujutsu Sorcerers after becoming involved with a cursed object.'),
('Attack on Titan','Action, Dark Fantasy','Humanity fights for survival against mysterious giant Titans outside the walls.');
