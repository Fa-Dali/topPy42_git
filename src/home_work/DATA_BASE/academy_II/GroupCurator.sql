INSERT INTO GroupCurator (CuratorId, GroupId) VALUES
((SELECT id FROM Curator WHERE Name='Ирина'), (SELECT id FROM Groups WHERE Name='1-ИСП')),
((SELECT id FROM Curator WHERE Name='Алексей'), (SELECT id FROM Groups WHERE Name='2-МАТ')),
((SELECT id FROM Curator WHERE Name='Елена'), (SELECT id FROM Groups WHERE Name='3-ФИЗ')),
((SELECT id FROM Curator WHERE Name='Михаил'), (SELECT id FROM Groups WHERE Name='4-ЛИТ')),
((SELECT id FROM Curator WHERE Name='Ольга'), (SELECT id FROM Groups WHERE Name='5-ИСТ')),
((SELECT id FROM Curator WHERE Name='Дмитрий'), (SELECT id FROM Groups WHERE Name='6-БИОЛ')),
((SELECT id FROM Curator WHERE Name='Анна'), (SELECT id FROM Groups WHERE Name='7-ХИМ')),
((SELECT id FROM Curator WHERE Name='Максим'), (SELECT id FROM Groups WHERE Name='8-ЭКО'));