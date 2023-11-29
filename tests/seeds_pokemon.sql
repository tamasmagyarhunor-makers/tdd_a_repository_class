-- SQL for test database / just truncate and re-seed with data
-- EXAMPLE
-- (file: tests/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE pokemons RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO pokemons (name, type) VALUES ('Pikachu', 'electric');
INSERT INTO pokemons (name, type) VALUES ('Bulbasaur', 'grass/poison');