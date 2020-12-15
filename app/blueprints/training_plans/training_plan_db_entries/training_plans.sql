--SQL Statements to populate trianing plan index DB
INSERT INTO "public".products (race_length, race_name, difficulty, frequency, plan_length, plan)
VALUES (26.2, 'marathon', 'beginner', 4, 18, '0,3,3,3,0,6,0-
                                              0,3,3,3,0,7,0-
                                              0,3,4,3,0,5,0-
                                              0,3,4,3,0,9,0-
                                              0,3,5,3,0,10,0-
                                              0,3,5,3,0,7,0-
                                              0,3,6,3,0,12,0-
                                              0,3,6,3,0,0,13.1-
                                              0,3,7,4,0,10,0-
                                              0,3,7,4,0,15,0-
                                              0,4,8,4,0,16,0-
                                              0,4,8,5,0,12,0-
                                              0,4,9,5,0,18,0-
                                              0,5,9,5,0,14,0-
                                              0,5,10,5,0,20,0-
                                              0,5,8,4,0,12,0-
                                              0,4,6,3,0,8,0-
                                              0,3,4,2,0,0,26.2'),
       (26.2, 'marathon', 'intermediate', 5, 18, '0,3,5,3,0,5,8-
                                                  0,3,5,3,0,5,9-
                                                  0,3,5,3,0,5,6-
                                                  0,3,6,3,0,6,11-
                                                  0,3,6,3,0,6,12-
                                                  0,3,5,3,0,6,9-
                                                  0,4,7,4,0,7,14-
                                                  0,4,7,4,0,7,15-
                                                  0,4,5,4,0,0,13.1-
                                                  0,4,8,4,0,8,17-
                                                  0,5,8,5,0,8,18-
                                                  0,5,5,5,0,8,13-
                                                  0,5,8,5,0,5,20-
                                                  0,5,5,5,0,8,12-
                                                  0,5,8,5,0,5,20-
                                                  0,5,6,5,0,4,12-
                                                  0,4,5,4,0,3,8-
                                                  0,3,4,0,0,2,26.2')
        (26.2, 'marathon', 'advanced', 6, 18, '3,5,3,3xhill,0,5,10-
                                               3,5,3,4xtempo,0,5,11-
                                               3,6,3,4x800,0,6,8-
                                               3,6,3,4xhill,0,6,13-
                                               3,7,3,4xtempo,0,7,14-

                                               3,7,3,5x800,0,7,10-
                                               3,8,4,5xhill,0,8,16-
                                               3,8,4,5xtempo,0,8,17-
                                               3,9,4,6x800,0,0,13.1-
                                               3,9,4,6xhill,0,9,19-

                                               4,6,5,5xtempo,0,10,20-
                                               4,6,5,7x800,0,6,12-
                                               4,10,5,7xhill,0,10,20-
                                               5,6,5,5xtempo,0,6,12-
                                               5,10,5,8x800,0,10,20-

                                               5,8,5,6xhill,0,4,12-
                                               4,6,4,4xtempo,0,4,8-
                                               3,4x400,2,0,0,2,26.2')
