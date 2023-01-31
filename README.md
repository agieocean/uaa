# uaa
Unity Answers Archive Search Engine

To run the docker you'll want to get unity_answers.zip from [here](https://f004.backblazeb2.com/file/unityanswers/questions_json.zip)

Once you download it extract the unity_answers folder directly to the working directory

Run 

`docker compose up`

`docker ps -a`

Get the id of the solr container

`docker exec -it [solir_id] /bin/bash`

`find /var/solr/data -name \*json | xargs bin/post -c gettingstarted`

You need to run it this way in order not to create a bash error regarding too many files

Once this is done make sure to configure an apache reverse proxy server to connect to the asp.net service

I've also included for reference the scripts used for both scraping the html (no longer possible as unity took the site down, hence the project) and parsing the html

The html itself is much larger at 80gb and so I don't host it, however you can request it from me and we can work out sharing it
