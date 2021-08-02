CREATE TABLE [IF NOT EXISTS] knowledge
( 
   id integer default 1 constraint knowledge_pk primary key autoincrement,
   Name text, 
   Verb text, 
   Noun text, 
   Adjective text, 
   Intransitive_Verb text, 
   Transitive_Verb text, 
   Adverb text, 
   Receiver text 
);

INSERT INTO knowledge (Name, Verb, Noun, Adjective, Intransitive_Verb, Transitive_Verb, Adverb, Receiver) VALUES 
('mary', null, 'dog', null, null, 'give', null, 'john'), 
('mary', null,'book', null, null, 'give' ,null, 'tomy'), 
('mary' , null, null, null,'run',null,'quickly',null), 
('mary', null, null,'tall',null,null,null,null), 
('mary', null, null,'slim',null,null,null,null), 
('mary', null, null,'blonde',null,null,null,null), 
('mary', 'love','book',null,null,null,null,null), 
('dog', 'need','food',null,null,null,null,null), 
('cat', 'have','food',null,null,null,null,null), 
('dog', 'hate','cat',null,null,null,null,null), 
('dog', 'chase','cat',null,null,null,null,null), 
('cat', null,null,'scary',null,null,null,null);