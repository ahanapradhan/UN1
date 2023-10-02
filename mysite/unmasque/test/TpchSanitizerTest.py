import unittest

from mysite.unmasque.src.pipeline.abstract.TpchSanitizer import TpchSanitizer
from mysite.unmasque.test.util.BaseTestCase import BaseTestCase


class MyTestCase(BaseTestCase):
    def test_for_table(self):
        sanitizer = TpchSanitizer(self.conn)
        self.conn.connectUsingParams()
        self.assertEqual('table', sanitizer.is_view_or_table("lineitem").lower())  # add assertion here
        self.assertEqual('table', sanitizer.is_view_or_table('lineitem').lower())  # add assertion here
        self.conn.closeConnection()

    def test_for_view(self):
        sanitizer = TpchSanitizer(self.conn)
        self.conn.connectUsingParams()
        self.conn.execute_sql(["create view nation1 as select * from nation;"])
        self.assertEqual('table', sanitizer.is_view_or_table("nation").lower())  # add assertion here
        self.assertEqual('table', sanitizer.is_view_or_table('nation').lower())  # add assertion here
        self.assertEqual('view', sanitizer.is_view_or_table("nation1").lower())  # add assertion here
        self.assertEqual('view', sanitizer.is_view_or_table('nation1').lower())  # add assertion here
        self.conn.execute_sql(["drop view if exists nation1;"])
        self.conn.closeConnection()


if __name__ == '__main__':
    unittest.main()
