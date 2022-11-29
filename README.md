# text-finder
The app provides the opportunity for searching texts in the database on the server using Elasticsearch and ZomboDB tools.
You can receive first 10 matching results from the database ordered by the date of creation. 

### CI status
[![Python CI](https://github.com/Dddarknight/text-finder/actions/workflows/pyci.yml/badge.svg)](https://github.com/Dddarknight/text-finder/actions)

## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | "Web framework for building APIs with Python" |
| [PostgreSQL](https://www.postgresql.org/) |  "An open source object-relational database system" |
| [Elasticsearch](https://www.elastic.co/elasticsearch/) |  "Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases." |
| [ZomboDB](https://www.zombodb.com/) |  "Integrate PostgreSQL and Elasticsearch" |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |

## Installation
**Tools**
You need to have Elasticsearch and ZomboDB installed to use the app.
If you don't, please, visit:
[Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
[ZomboDB](https://www.zombodb.com/documentation/SOURCE-INSTALLATION/)

**Copy a project**
```
$ git clone git@github.com:Dddarknight/text-finder.git
$ cd text-finder 
```

**Set up environment variables**
``` 
$ touch .env

# You have to fill .env file. See .env.example.
# You will have to fill username and password fields for PostgreSQL.
```

**Launch**
``` 
$ make run
```

## Example of usage
``` 
$ curl -X GET 'http://localhost:8000/texts?text_to_find=like'
```