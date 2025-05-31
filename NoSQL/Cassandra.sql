Cassandra

CREATE KEYSPACE cassandradb
    WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};

describe keyspaces;

use cassandradb;

CREATE TABLE pessoa(
                       id int PRIMARY KEY,
                       name text,
                       job text,
                       createdAt text,
);

desc pessoa;

select * from pessoa;

drop table pessoa;

INSERT INTO cassandradb.pessoa (id, name, job, createdAt)
VALUES(199,'Pedro', 'CEO','2020-02-20T11:00:28.107Z' );

INSERT INTO pessoa (id, name, job, createdAt)
VALUES(231,'Maysa', 'design', '2024-07-20T09:00:10.107Z' );
INSERT INTO pessoa (id, name, job, createdAt)
VALUES(387, 'Malu', 'AI Engineering', '2021-05-20T06:00:20.107Z');


select * from pessoa;


select * from cassandradb.pessoa
where job IN ('CEO', 'design') ALLOW FILTERING;
