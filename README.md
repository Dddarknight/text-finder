# text-finder
The app provides the opportunity for searching texts in the database on the server using Elasticsearch.
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
| [Logstash](https://www.elastic.co/logstash/) |  "is a free and open server-side data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to "stash" |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |

## Installation and usage

**Introductory information**

We have a database called 'texts' with a table 'db_texts'.
The fields of the table: 'id', 'text', 'created_date', 'rubrics'.
First, we need to put to the Elasticsearch index fields 'id', 'text'.
Then our app will search requested text in the Elasticsearch index, collect related information (ids) about the objects and search them in our database. 

**Tools**

You need to have Elasticsearch and Logstash installed to use the app.
If you don't, please, visit:

[Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

[Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

Example Logstash configuration file:
```
input {
    jdbc {
        jdbc_connection_string => "jdbc:postgresql://localhost:5432/texts"
        jdbc_user => "your_username_here"
        jdbc_password => "your_password_here"
        jdbc_validate_connection => true
        jdbc_driver_library => "/path-to/postgresql-42.5.1.jar"
        jdbc_driver_class => "org.postgresql.Driver"
        statement => "SELECT id, text FROM db_texts"
    }
}
filter {
    date {
        match => [ "event_date" ,"yyyy-MM-dd HH:mm:ss"]
        timezone => "Europe/Paris"
        target => "@timestamp"
    }
}
output {
    elasticsearch {
        index => "texts"
        hosts => "localhost:9200"
    }
}
```

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