# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker
from testscraper.models import LaptopsDB, db_connect, create_laptops_table

class LaptopsPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_laptops_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        laptopsdb = LaptopsDB()
        laptopsdb.title = item["title"]
        laptopsdb.image = item["image"]
        laptopsdb.description = item["description"]
        laptopsdb.price = item["price"]

        try:
            session.add(laptopsdb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item