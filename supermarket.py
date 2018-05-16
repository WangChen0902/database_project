import pymysql

db = pymysql.connect('localhost', 'tester', '123456', 'supermarket')
cursor = db.cursor()
SQL = 'select * from goods'


def insert(table, value):
    if table == 'goods':
        sql = "insert into goods values ('%d','%s','%s','%d','%d')" % value
    elif table == 'clothes_goods':
        sql = "insert into clothes_goods ('%d','%s','%s','%s')" % value
    elif table == 'food_goods':
        sql = "insert into food_goods ('%d','%s','%s')" % value
    elif table == 'sale_record':
        sql = "insert into sale_record ('%d','%d','%s','%d','%d','%d','%d')" % value
    elif table == 'stock_record':
        sql = "insert into sale_record ('%d','%d','%s','%d','%d','%d','%d')" % value
    elif table == 'off_record':
        sql = "insert into off_record ('%d','%s','%s')" % value
    else:
        return

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


def select(sql):
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        data_dict = []
        for field in cursor.description:
            data_dict.append(field[0])
        print(cursor.description)
        print(results)
        print(data_dict)
        return results
    except Exception as e:
        db.rollback()
        print(e)


data = (13, 'ss', 'sss', 2, 30)
insert('goods', data)
