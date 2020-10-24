import pymysql
import random

#随机数
def randomNumber(total,strNum):
    zf="1234567890qwertyuipasdfghjkzxcvbnm"
    b=[]
    for i in range(total):
        a=''
        for j in range(strNum):
          a+=""+random.choice(zf)
        b.append(a)

    return b

def save(res):
    db=pymysql.connect('localhost',"root",'123456','test')
    conn=db.cursor();
    conn.execute("CREATE TABLE code  (`id` bigint(20) NOT NULL AUTO_INCREMENT,"
                 "`code` varchar(255) NULL, PRIMARY KEY (`id`))")
    for num in res:
        conn.execute("insert into code(code) value(%s) ",(num))
        conn.connection.commit()
    db.close()

if __name__ == '__main__':
 res =randomNumber(2,3)
 print(res)
 save(res)
