## Sof crawler

A Crawler for stackoverflow.com latest question by tag 

#### How to run locally

1. Clone the repository
    
2. Install the requirements
    
    `pip install -r requirements.txt`

3. Run the crawler

    `scrapy crawl sof`


### How to run with docker

1. Clone the repository

2. Run docker-compose

    `docker-compose up -d --build`

After this processes latest 50 questions will be inserted to sof.db database.
