INSERT INTO teams (name, created_at) VALUES
('Team Alpha', '2024-04-01 10:00:00'),
('Team Beta', '2024-04-02 11:00:00'),
('Team Gamma', '2024-04-03 12:00:00');

-- Membros do Team Alpha
INSERT INTO members (team_id, name, email, password, role, created_at) VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'PO', '2024-04-01 10:00:00'),
(1, 'Bob Smith', 'bob.smith@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'SM', '2024-04-02 10:00:00'),
(1, 'Charlie Davis', 'charlie.davis@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-03 10:00:00'),
(1, 'David Evans', 'david.evans@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-04 10:00:00'),
(1, 'Eve Foster', 'eve.foster@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-05 10:00:00');

-- Membros do Team Beta
INSERT INTO members (team_id, name, email, password, role, created_at) VALUES
(2, 'Fiona Green', 'fiona.green@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'PO', '2024-04-06 10:00:00'),
(2, 'George Hill', 'george.hill@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'SM', '2024-04-07 10:00:00'),
(2, 'Hannah Irwin', 'hannah.irwin@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-08 10:00:00'),
(2, 'Ian Jackson', 'ian.jackson@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-09 10:00:00'),
(2, 'Julia King', 'julia.king@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-10 10:00:00');

-- Membros do Team Gamma
INSERT INTO members (team_id, name, email, password, role, created_at) VALUES
(3, 'Kyle Lee', 'kyle.lee@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'PO', '2024-04-11 10:00:00'),
(3, 'Laura Martin', 'laura.martin@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'SM', '2024-04-12 10:00:00'),
(3, 'Mike Nelson', 'mike.nelson@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-13 10:00:00'),
(3, 'Nina Olson', 'nina.olson@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-14 10:00:00'),
(3, 'Oscar Perez', 'oscar.perez@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-15 10:00:00'),
(3, 'Paula Quinn', 'paula.quinn@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-16 10:00:00'),
(3, 'Quincy Roberts', 'quincy.roberts@example.com', 'scrypt:32768:8:1$zhyhYltWuGMh1ZTu$930af693badc06704d40764c4417ed8bb594e8cfdaedcfa6fe5d4e3af94b67207c0874e44a11e34e9555ac4b973476e48816d3bbd838ece446bc8fc9288bbbbf', 'ST', '2024-04-17 10:00:00');



INSERT INTO projects (team_id, name, n_sprints, created_at) VALUES
(1, 'Project Alpha 1', 4, '2024-04-04 10:00:00'),
(1, 'Project Alpha 2', 3, '2024-04-05 11:00:00'),
(1, 'Project Alpha 3', 2, '2024-04-06 12:00:00');

INSERT INTO projects (team_id, name, n_sprints, created_at) VALUES
(2, 'Project Beta 1', 3, '2024-04-07 10:00:00'),
(2, 'Project Beta 2', 1, '2024-04-08 11:00:00');

INSERT INTO projects (team_id, name, n_sprints, created_at) VALUES
(3, 'Project Gamma 1', 4, '2024-04-09 10:00:00'),
(3, 'Project Gamma 2', 3, '2024-04-10 11:00:00');



-- Scores para Alice Johnson em Project Alpha 1
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 2, 3, 1, 2, 1, 1, '2024-04-04 10:00:00'),
(2, 3, 2, 2, 1, 1, 1, '2024-04-05 10:00:00'),
(3, 1, 2, 3, 3, 1, 1, '2024-04-06 10:00:00'),
(4, 2, 1, 2, 3, 1, 1, '2024-04-07 10:00:00');

-- Scores para Alice Johnson em Project Alpha 2
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 1, 3, 2, 2, 1, 2, '2024-04-08 10:00:00'),
(2, 3, 1, 3, 1, 1, 2, '2024-04-09 10:00:00'),
(3, 2, 2, 1, 3, 1, 2, '2024-04-10 10:00:00');

-- Scores para Alice Johnson em Project Alpha 3
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 2, 1, 2, 3, 1, 3, '2024-04-11 10:00:00'),
(2, 3, 3, 1, 2, 1, 3, '2024-04-12 10:00:00');

-- Scores para Bob Smith em Project Alpha 1
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 3, 2, 1, 3, 2, 1, '2024-04-04 11:00:00'),
(2, 2, 3, 2, 1, 2, 1, '2024-04-05 11:00:00'),
(3, 1, 1, 3, 2, 2, 1, '2024-04-06 11:00:00'),
(4, 2, 3, 1, 2, 2, 1, '2024-04-07 11:00:00');

-- Scores para Bob Smith em Project Alpha 2
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 2, 1, 3, 2, 2, 2, '2024-04-08 11:00:00'),
(2, 3, 2, 2, 1, 2, 2, '2024-04-09 11:00:00'),
(3, 1, 3, 1, 3, 2, 2, '2024-04-10 11:00:00');

-- Scores para Bob Smith em Project Alpha 3
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 3, 1, 2, 2, 2, 3, '2024-04-11 11:00:00'),
(2, 2, 3, 3, 1, 2, 3, '2024-04-12 11:00:00');

-- Scores para Charlie Davis em Project Alpha 1
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 2, 3, 1, 2, 3, 1, '2024-04-04 12:00:00'),
(2, 3, 2, 2, 1, 3, 1, '2024-04-05 12:00:00'),
(3, 1, 2, 3, 3, 3, 1, '2024-04-06 12:00:00'),
(4, 2, 1, 2, 3, 3, 1, '2024-04-07 12:00:00');

-- Scores para Charlie Davis em Project Alpha 2
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 1, 3, 2, 2, 3, 2, '2024-04-08 12:00:00'),
(2, 3, 1, 3, 1, 3, 2, '2024-04-09 12:00:00'),
(3, 2, 2, 1, 3, 3, 2, '2024-04-10 12:00:00');

-- Scores para Charlie Davis em Project Alpha 3
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 2, 1, 2, 3, 3, 3, '2024-04-11 12:00:00'),
(2, 3, 3, 1, 2, 3, 3, '2024-04-12 12:00:00');

-- Scores para David Evans em Project Alpha 1
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 3, 2, 1, 3, 4, 1, '2024-04-04 13:00:00'),
(2, 2, 3, 2, 1, 4, 1, '2024-04-05 13:00:00'),
(3, 1, 1, 3, 2, 4, 1, '2024-04-06 13:00:00'),
(4, 2, 3, 1, 2, 4, 1, '2024-04-07 13:00:00');

-- Scores para David Evans em Project Alpha 2
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 2, 1, 3, 2, 4, 2, '2024-04-08 13:00:00'),
(2, 3, 2, 2, 1, 4, 2, '2024-04-09 13:00:00'),
(3, 1, 3, 1, 3, 4, 2, '2024-04-10 13:00:00');

-- Scores para David Evans em Project Alpha 3
INSERT INTO scores (n_sprint, score_proatividade, score_autonomia, score_colaboracao, score_entrega, member_id, project_id, created_at) VALUES
(1, 3, 1, 2, 2, 4, 3, '2024-04-11 13:00:00'),
(2, 2, 3, 3, 1, 4, 3, '2024-04-12 13:00:00');


