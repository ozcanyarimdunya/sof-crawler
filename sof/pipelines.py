import records


class SofPipeline(object):
    def __init__(self, db_url):
        self.db_url = db_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_url=crawler.settings['DB_URL'],
        )

    def open_spider(self, spider):
        self.db = records.Database(db_url=self.db_url)
        self.db.query(
            """CREATE TABLE IF NOT EXISTS  sof(
                   id_ INTEGER PRIMARY KEY AUTOINCREMENT,
                   title_ TEXT,
                   description_ TEXT,
                   vote_ TEXT,
                   answer_ TEXT,
                   view_ TEXT,
                   asked_ TEXT,
                   user_ TEXT
               );"""
        )

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        self.db.query(
            """INSERT INTO sof(title_,description_,vote_,answer_,view_,asked_,user_) 
            values (:title_,:description_,:vote_,:answer_,:view_,:asked_,:user_);""",
            title_=item['title'], description_=item['description'], vote_=item['vote'], answer_=item['answer'],
            view_=item['view'], asked_=item['asked'], user_=item['user']
        )
        return item
