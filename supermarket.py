import pymysql

db = pymysql.connect('localhost', 'tester', '123456', 'supermarket')
cursor = db.cursor()


def insert(table, value):
    if table == 'goods':
        sql = "insert into goods values (%s, '%s', '%s', %s, %s)" % tuple(value)
    elif table == 'clothes_goods':
        sql = "insert into clothes_goods values (%s, '%s', '%s', '%s')" % tuple(value)
    elif table == 'food_goods':
        sql = "insert into food_goods values (%s, '%s', '%s')" % tuple(value)
    elif table == 'sale_record':
        sql = "insert into sale_record(gid, sale_time, sale_amount, sale_price, total_price) " \
              "values (%s, '%s', %s, %s, %s)" % tuple(value)
    elif table == 'stock_record':
        sql = "insert into stock_record(gid, stock_time, stock_amount, stock_price, total_price) " \
              "values (%s, '%s', %s, %s, %s)" % tuple(value)
    elif table == 'off_record':
        sql = "insert into off_record(gid, off_time, off_reason) " \
              "values (%s, '%s', '%s')" % tuple(value)
    else:
        return

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


def update(table, value, flag):
    tmp = list()
    sql = ''
    if flag == True:
        tmp.append('+ %s' % value[1])
    else:
        tmp.append('- %s' % value[1])
    tmp.append(value[0])

    if table == 'goods':
        sql = "update goods set amount = amount %s where gid = %s" % tuple(tmp)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


def select(table, value):
    sql = ''
    if table == 'goods':
        name_list = ["G.gid = %s", "gname = '%s'", "brand = '%s'", "price = %s", "amount = %s", "color = '%s'",
                     "size = '%s'", "suitable_crowds = '%s'", "quality_date = '%s'", "place = '%s'"]
        where_str = list_2_where(name_list, value)

        sql = "select G.gid, gname, brand, price, amount, color, size, suitable_crowds, quality_date, place " \
              "from goods G left join clothes_goods C on G.gid = C.gid left join food_goods F on G.gid = F.gid " \
              "where %s" % where_str

    if table == 'sale':
        if value == '*':
            sql = "select * from sale_record"
        else:
            name_list = ["gid = %s", "sale_time >= '%s'", "sale_time <= '%s'"]
            where_str = list_2_where(name_list, value)
            sql = "select gid, sale_time, sale_amount, sale_price, total_price " \
                  "from sale_record " \
                  "where %s" % where_str
        print(sql)

    if table == 'refresh':
        name_list = ["amount < %s"]
        where_str = list_2_where(name_list, value)
        sql = "select gid, gname, brand, price, amount " \
              "from goods " \
              "where %s" % where_str

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        data_dict = []
        for field in cursor.description:
            data_dict.append(field[0])
        return results
    except Exception as e:
        db.rollback()
        print(e)


def list_2_where(name_list, value):
    s = list()
    for i in range(len(value)):
        if value[i] == '':
            s.append('1')
        else:
            s.append(name_list[i] % value[i])
    where_str = '1'
    for i in s:
        where_str += ' and ' + i
    return where_str
