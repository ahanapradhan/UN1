import unittest

from mysite.unmasque.refactored.ConnectionHelper import ConnectionHelper
from mysite.unmasque.refactored.executable import Executable
from mysite.unmasque.refactored.util.utils import isQ_result_empty
from mysite.unmasque.src.core import OldPipeLine
from mysite.unmasque.test.util import queries, tpchSettings


class MyTestCase(unittest.TestCase):
    conn = ConnectionHelper("tpch", "postgres", "postgres", "5432", "localhost")

    def test_extraction_tpch_query1(self):
        self.conn.connectUsingParams()
        key = 'tpch_query1'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_tpch_query3(self):
        self.conn.connectUsingParams()
        key = 'tpch_query3'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q1(self):
        self.conn.connectUsingParams()
        key = 'Q1'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q3(self):
        self.conn.connectUsingParams()
        key = 'Q3'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q4(self):
        self.conn.connectUsingParams()
        key = 'Q4'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q5(self):
        self.conn.connectUsingParams()
        key = 'Q5'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q6(self):
        self.conn.connectUsingParams()
        key = 'Q6'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q7(self):
        self.conn.connectUsingParams()
        key = 'Q7'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q11(self):
        self.conn.connectUsingParams()
        key = 'Q11'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q16(self):
        self.conn.connectUsingParams()
        key = 'Q16'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q17(self):
        self.conn.connectUsingParams()
        key = 'Q17'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q18(self):
        self.conn.connectUsingParams()
        key = 'Q18'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)

        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q21(self):
        self.conn.connectUsingParams()
        key = 'Q21'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)

        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q23_1(self):
        self.conn.connectUsingParams()
        key = 'Q23_1'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)

        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q9_simple(self):
        self.conn.connectUsingParams()
        key = 'Q9_simple'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()

    def test_extraction_Q10_simple(self):
        self.conn.connectUsingParams()
        key = 'Q10_simple'
        from_rels = tpchSettings.from_rels[key]
        query = queries.queries_dict[key]
        app = Executable(self.conn)
        result = app.doJob(query)
        if isQ_result_empty(result):
            print("Hidden query doesn't produce a populated result. It is beyond the scope of Unmasque..skipping "
                  "query!")
            self.assertTrue(False)

        eq, tp = OldPipeLine.extract(self.conn, query,
                                     tpchSettings.relations,
                                     from_rels,
                                     tpchSettings.key_lists, tpchSettings.global_pk_dict)
        self.assertTrue(eq is not None)
        print(eq)
        tp.print()
        self.conn.closeConnection()


if __name__ == '__main__':
    unittest.main()
