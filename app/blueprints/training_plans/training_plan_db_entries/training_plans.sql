--SQL Statements to populate trianing plan index DB
INSERT INTO "public".training_plans (race_length, race_name, difficulty, frequency, plan_length, plan)
VALUES (26.2, 'Marathon', 'Beginner', 4, 18, '0,3,3,3,0,6,0-0,3,3,3,0,7,0-0,3,4,3,0,5,0-0,3,4,3,0,9,0-0,3,5,3,0,10,0-0,3,5,3,0,7,0-0,3,6,3,0,12,0-0,3,6,3,0,0,13.1-0,3,7,4,0,10,0-0,3,7,4,0,15,0-0,4,8,4,0,16,0-0,4,8,5,0,12,0-0,4,9,5,0,18,0-0,5,9,5,0,14,0-0,5,10,5,0,20,0-0,5,8,4,0,12,0-0,4,6,3,0,8,0-0,3,4,2,0,0,26.2'),
       (26.2, 'Marathon', 'Intermediate', 5, 18, '0,3,5,3,0,5,8-0,3,5,3,0,5,9-0,3,5,3,0,5,6-0,3,6,3,0,6,11-0,3,6,3,0,6,12-0,3,5,3,0,6,9-0,4,7,4,0,7,14-0,4,7,4,0,7,15-0,4,5,4,0,0,13.1-0,4,8,4,0,8,17-0,5,8,5,0,8,18-0,5,5,5,0,8,13-0,5,8,5,0,5,20-0,5,5,5,0,8,12-0,5,8,5,0,5,20-0,5,6,5,0,4,12-0,4,5,4,0,3,8-0,3,4,0,0,2,26.2'),
       (13.1, 'Half-Marathon', 'Beginner', 4, 12, '0,3,2,3,0,0,4-0,3,2,3,0,0,4-0,3.5,2,3.5,0,0,5-0,3.5,2,3.5,0,0,5-0,4,2,4,0,0,6-0,4,2,4,0,0,3.13-0,4.5,3,4.5,0,0,7-0,4.5,3,4.5,0,0,8-0,5,3,5,0,0,6.26-0,5,3,5,0,0,9-0,5,3,5,0,0,10-0,4,3,2,0,0,13.1'),
       (3.13, '5k', 'Beginner', 4, 8, '0,1.5,0,1.5,0,1.5,0-0,1.75,0,1.5,0,1.75,0-0,2,0,1.5,0,2,0-0,2.25,0,1.5,0,2.25,0-0,2.5,0,2,0,2.5,0-0,2.75,0,2,0,2.75,0-0,3,0,2,0,3,0-0,3,0,2,0,0,3.13'),
       (3.13, '5k', 'Intermediate', 5, 8, '0,3,3,3,0,3,5-0,3,4,3,0,3,5-0,3,3.5,3,0,4,6-0,3,4.5,3,0,0,3.13-0,3,4,3,0,4,6-0,3,5,3,0,5,7-0,3,4,3,0,5,7-0,3,3,2,0,0,3.13'),
       (6.26, '10k', 'Beginner', 4, 8, '0,2.5,0,2,0,2,3-0,2.5,0,2,0,2,3.5-0,2.5,0,2,0,2,4-0,3,0,2,0,2,4-0,3,0,2,0,2,4.5-0,3,0,2,0,2,5-0,3,0,2,0,2,5.5-0,3,0,2,0,0,6.26'),
       (6.26,  '10k', 'Intermediate', 5, 8, '3,3,4,3,0,0,4-3,3.5,4,4,0,0,5-3,4,4.5,3,0,0,6-3,4.5,4.5,4,0,0,3.13-3,5,5,3,0,0,6-3,5.5,5,4,0,0,7-3,6,5.5,4,0,0,8-3,3,3,2,0,0,6.26'),
       (13.1, 'Half-Marathon', 'Intermediate', 5, 12, '0,3,4,3,0,3,4-0,3,4,3,0,3,5-0,3.5,5,3.5,0,0,6-0,3.5,5,3.5,0,3,7-0,4,6,4,0,3,8-0,4,6,4,0,0,3.13-0,4.5,7,4.5,0,4,9-0,4.5,7,4.5,0,5,10-0,5,8,5,0,5,11-0,5,6,4,0,3,12-0,4,4,2,0,0,13.1'),
       (6.0, 'Base Training', 'Beginner', 4, 12, '0,1.5,3,1.5,0,0,3-0,1.5,3,1.5,0,0,3.5-0,1.5,3,1.5,0,0,3-0,2,3,1.5,0,0,4-0,2,3,2,0,0,3-0,2,3,2,0,0,4.5-0,2,3,2,0,0,3-0,2.5,3,2,0,0,5-0,2.5,3,2.5,0,0,3-0,2.5,3,2.5,0,0,5.5-0,3,3,3,0,0,3-0,3,3,3,0,0,6'),
       (3.13, '5k', 'Advanced', 5, 8, '3,3,0,5,0,4,6-3,3,0,5,0,4,6.5-3,3,0,5.5,0,5,7-3,3,0,5.5,0,0,3.13-3,4,0,6,0,5,7.5-3,5,0,6,0,6,8-3,6,0,6.5,0,0,3.13'),
       (6.26, '10k', 'Advanced', 6, 8, '3,4,4,3,0,5,6-3,5,4,4,0,5,7-3,6,5,5,0,5,8-3,4,5.5,3,0,0,3.13-3,7,5.5,6,0,6,8-3,4,6,3,0,0,5-3,8,6,6,0,6,10-3,4,4,3,0,0,6.26'),
       (13.1, 'Half-Marathon', 'Advanced', 6, 12, '3,4,3,6,0,3,12-3,4,3,7,0,3,12-3,4.5,3,5,0,0,3.13-3,4.5,3,6,0,3,12-3,5,3,7,0,3,12-3,5,3,5,0,0,6.26-3,5,3,7,0,4,14-3,6,3,8,0,5,14-3,7,3,5,0,0,10-3,6,3,9,0,5,16-3,8,3,10,0,3,16-3,4,3,5,0,0,13.1'),
       (26.2, 'Marathon', 'Advanced', 6, 18, '3,5,3,4,0,5,10-3,5,3,5,0,5,11-3,6,3,4,0,6,8-3,6,3,4,0,6,13-3,7,3,6,0,7,14-3,7,3,5,0,7,10-3,8,4,5,0,8,16-3,8,4,7,0,8,17-3,9,4,5,0,0,13.1-3,9,4,5,0,9,19-4,10,5,8,0,10,20-4,6,5,6,0,6,12-4,10,5,6,0,10,20-5,6,5,8,0,6,12-5,10,5,7,0,10,20-5,8,5,4,0,4,12-4,6,4,4,0,4,8-3,4,2,0,0,2,26.2'),
       (8.0, 'Base Training', 'Intermediate', 6, 12, '3,3,3,3,0,4,6-3,3,3,3,0,5,7-3,4,4,3,0,5,6-3,4,4,3,0,5,73,5,5,3,0,5,8-3,5,5,3,0,0,3.13-3,4,5,3,0,6,7-3,5,5,3,0,6,8-3,6,5,3,0,0,5-3,4,4,3,0,7,7-3,5,4,3,0,7,8-3,6,4,3,0,0,6.26')
