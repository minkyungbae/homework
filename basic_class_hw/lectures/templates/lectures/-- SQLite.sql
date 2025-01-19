-- SQLite
-- SELECT name
-- FROM sqlite_master
-- WHERE type='table'
-- ORDER BY name;

-- INSERT INTO lectures_lecture (instructor_id, is_online, prerequisite, name)
-- VALUES (1004, TRUE, "대수학", "딥러닝");

-- SELECT * FROM lectures_lecture;

-- DELETE FROM lectures_lecture WHERE lecture_id=2;

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (82536, "패션과 이미지메이킹", FALSE, "");

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (88529, "심리학", FALSE, "");

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (2019111504, "기초영어회화II", TRUE, "");

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (2019111507, "관광학개론II", TRUE, "관광학개론I" );

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (2019111514, "소물리에", TRUE, "" );

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (59147, "관광법규", TRUE, "");

INSERT INTO lectures_lecture (instructor_id, name, is_online, prerequisite)
VALUES (0426, "호텔영어", TRUE, "");

SELECT * FROM lectures_lecture;

-- DELETE FROM lectures_lecture;

-- ALTER TABLE lectures_lecture AUTO_INCREMENT=1;

-- DROP TABLE lectures_lecture;