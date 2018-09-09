import json

import pymysql

'''
@marshal_with

City.query.all()


return data

'''




#json --> 数据库 ---》读取
def get_city_data():
    #port后民的值是一个整数    charset = utf8 没有杠
    db = pymysql.Connect(host="localhost", port=3306, user="root",
                         password="1234",
                         database="Tpp",
                         charset="utf8")
    cursor = db.cursor()

    with open("city.json") as city:
        city_collect = json.load(city)
        # A:{}{}
        returnValue = city_collect.get("returnValue")

        #获取字典中所有的key
        letters = returnValue.keys()

        for letter in letters:

            db.begin()
            #注意:values方法中的值 一定是一个字符串
            cursor.execute("INSERT INTO letter(letter) VALUES ('{}');".format(letter))
            db.commit()

            db.begin()
            #select * from letter where letter = 'A'  ---  1 A
            cursor.execute("SELECT  *  FROM  letter WHERE letter='{}';".format(letter))
            db.commit()

            result = cursor.fetchone()

            letter_id = result[0]

            print('*'*50)
            print(letter_id)
            print('*' * 50)
            #通过A 来获取对应的所有的城市
            letter_cities = returnValue.get(letter)

            for letter_city in letter_cities:
                regionName = letter_city.get("regionName")
                id = letter_city.get("id")
                cityCode = letter_city.get("cityCode")
                pinYin = letter_city.get("pinYin")
                db.begin()
                cursor.execute("INSERT INTO city (id, regionName, cityCode, pinYin, letter) VALUES ({}, '{}', {}, '{}', {});".format(id, regionName, cityCode, pinYin, letter_id))
                db.commit()


if __name__ == '__main__':
    get_city_data()



