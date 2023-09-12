from mysite.unmasque.refactored.ConnectionHelper import ConnectionHelper
from mysite.unmasque.src.core import ExtractionPipeLine

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hq = "select c_mktsegment, l_orderkey, sum(l_extendedprice) as revenue, " \
              "o_orderdate, o_shippriority from customer, orders, lineitem where c_custkey = o_custkey " \
              "and l_orderkey = o_orderkey and o_orderdate > date '1995-10-11' " \
              "group by l_orderkey, o_orderdate, o_shippriority, c_mktsegment limit 4;"

    conn = ConnectionHelper("tpch", "postgres", "postgres", "5432", "localhost")
    conn.connectUsingParams()

    eq, time = ExtractionPipeLine.extract(conn, hq)

    print("=========== Extracted Query =============")
    print(eq)
    time.print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
