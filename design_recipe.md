# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._
```
As a User
So I can keep track of Pokemons I like
I'd like to store and view name of type of Pokemons
```

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `pokemons`*

```
# EXAMPLE

Table: pokemons

Columns:
id | name | type
```

## 2.1 Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
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
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 2.2 The initial SQL seed

```sql
-- SQL for database / initial seed file
-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS pokemons;
DROP SEQUENCE IF EXISTS pokemons_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS pokemons_id_seq;
CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO pokemons (name, type) VALUES ('Charmander', 'fire');
INSERT INTO pokemons (name, type) VALUES ('Squirtle', 'water');
INSERT INTO pokemons (name, type) VALUES ('Jigglypuff', 'fairy');
INSERT INTO pokemons (name, type) VALUES ('Meowth', 'normal');
INSERT INTO pokemons (name, type) VALUES ('Geotude', 'rock');
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: pokemons

# Model class
# (in lib/pokemon.py)
class Pokemon


# Repository class
# (in lib/pokemon_repository.py)
class PokemontRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: pokemon

# Model class
# (in lib/pokemon.py)

class Pokemon:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.type = ""

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> pokemon = Pokemon()
# >>> pokemon.name = "Caterpie"
# >>> pokemon.type = "bug"
# >>> pokemon.name
# 'Caterpie'
# >>> pokemon.type
# 'bug'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: pokemons

# Repository class
# (in lib/pokemon_repository.py)

class PokemonRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, type FROM pokemons;

        # Returns an array of Pokemon objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, type FROM pokemons WHERE id = $1;

        # Returns a single Pokemon object.

        # Add more methods below for each operation you'd like to implement.

    # def create(pokemon)
    # 

    # def update(pokemon)
    # 

    # def delete(pokemon)
    # 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all pokemons

repo = PokemonRepository()

pokemons = repo.all()

len(pokemons) # =>  2

pokemons[0].id # =>  1
pokemons[0].name # =>  'Pikachu'
pokemons[0].type # =>  'electric'

pokemons[1].id # =>  2
pokemons[1].name # =>  'Bulbasaur'
pokemons[1].type # =>  'grass/poison'

# 2
# Get a single Pokemon

repo = PokemonRepository()

pokemon = repo.find(1)

pokemon.id # =>  1
pokemons.name # =>  'Pikachu'
pokemons.type # =>  'electric'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
