insert into auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) value ('password', 1, 'kirill', 'kirill', 'statsenko', 'kirill@statsenko.com', 1, 1, now());

insert into qa_question (title, text, added_at, rating, author_id) value ('Question 1', 'Hello question 1', now(), 10, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 2', 'Hello question 2', now(), 7, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 3', 'Hello question 3', now(), 10, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 4', 'Hello question 4', now(), 5, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 5', 'Hello question 5', now(), 10, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 6', 'Hello question 6', now(), 1, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 7', 'Hello question 7', now(), 4, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 8', 'Hello question 8', now(), 10, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 9', 'Hello question 9', now(), 3, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 10', 'Hello question 10', now(), 10, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 11', 'Hello question 11', now(), 6, (select id from auth_user where username = 'kirill'));
insert into qa_question (title, text, added_at, rating, author_id) value ('Question 12', 'Hello question 12', now(), 10, (select id from auth_user where username = 'kirill'));

insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 1'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 1'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 4'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 1'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 3'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 1'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 1'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 2'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 1'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 2'));
insert into qa_answer (text, added_at, author_id, question_id) value ('Cool', now(), (select id from auth_user where username = 'kirill'), (select id from qa_question where title = 'Question 3'));