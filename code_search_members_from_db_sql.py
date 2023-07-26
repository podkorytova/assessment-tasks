import random
import sqlite3


class Member:
    def __init__(self, cur, conn):
        random.seed()
        self.name = f'FirstName{random.randint(0, 10)}'
        self.address = f'Prague{random.randint(0, 10)}Street{random.randint(0, 10)}{random.randint(0, 1000)}'
        self.phone_number = f'+420{random.randint(100000000, 999999999)}'
        self.age = random.randint(0, 122)
        cur.execute(
            f"INSERT INTO members (name, address, phone_number, age) VALUES ('{self.name}', '{self.address}', '{self.phone_number}', '{self.age}');")
        conn.commit()


class Organization:
    def __init__(self, cur, conn, member_id):
        random.seed()
        locations = ['Prague1', 'Prague2', 'Prague3', 'Prague4', 'Prague5']
        cur.execute(
            f"INSERT INTO organizations (member_id, location, dues) VALUES ('{member_id}', '{locations[random.randint(0, 4)]}', '{random.randint(0, 100)}')")
        conn.commit()


class DataBase:
    def __init__(self):
        self.connect = sqlite3.connect('search_members_from_db_sql.s3db')
        self.cursor = self.connect.cursor()
        if not self.check_exist_table('members'):
            self.cursor.execute(
                f"CREATE TABLE members (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT, phone_number TEXT,age INTEGER)")
            self.connect.commit()
        if not self.check_exist_table('organizations'):
            self.cursor.execute(
                f"CREATE TABLE organizations (id INTEGER PRIMARY KEY AUTOINCREMENT, member_id INTEGER, location TEXT, dues INTEGER)")
            self.connect.commit()

    def check_exist_table(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name};")
        except sqlite3.OperationalError:
            return False
        return True

    def get_connect(self):
        return self.connect

    def get_cursor(self):
        return self.cursor

    def print_members(self):
        print('Member Table')
        print(f"|ID                |Name              |Address           |Phone             |Age")
        member_data = self.cursor.execute(f"SELECT * from members").fetchall()
        for i in member_data:
            for x in map(str, i):
                print(f"|{x:18}", end='')
            print('\n')

    def print_organizations(self):
        print('Organization Table')
        print(f"|ID       |Member_ID|Location |Dues")
        organization_data = self.cursor.execute(f"SELECT * from organizations").fetchall()
        for i in organization_data:
            for x in map(str, i):
                print(f"|{x:9}", end='')
            print('\n')

    def clear_data(self):
        self.cursor.execute(f"DELETE FROM members")
        self.cursor.execute(f"DELETE FROM organizations")
        self.connect.commit()


db = DataBase()

for i in range(0, 5):
    member = Member(db.get_cursor(), db.get_connect())
    member_id = db.get_cursor().execute(f"SELECT last_insert_rowid();").fetchone()
    org = Organization(db.get_cursor(), db.get_connect(), member_id[0])

print(f"Query 1:\n SELECT m.name, m.address, o.dues, o.location\n FROM members m, organizations o\n WHERE m.id = o.member_id;")
result_query_1 = db.get_cursor().execute((f"SELECT m.name NAME, m.address ADDRRESS, o.dues DUES, o.location LOCATION FROM members m, organizations o WHERE m.id = o.member_id;")).fetchall()
print("Result of Query1:")
for i in result_query_1:
    print(i, "\n")

print(f"Query 2:\n SELECT m.name, m.address, o.dues, o.location\n FROM members m, organizations o\n WHERE m.id = o.member_id AND m.age > 45;")
result_query_2 = db.get_cursor().execute((f"SELECT m.name NAME, m.address ADDRRESS, o.dues DUES, o.location LOCATION FROM members m, organizations o WHERE m.id = o.member_id AND m.age > 45;")).fetchall()
print("Result of Query2:")
for i in result_query_2:
    print(i, "\n")

print(f"Query 3:\n SELECT m.name, m.address, o.dues, o.location\n FROM members m, organizations o\n WHERE m.id = o.member_id AND o.dues = 0;")
result_query_3 = db.get_cursor().execute((f"SELECT m.name NAME, m.address ADDRRESS, o.dues DUES, o.location LOCATION FROM members m, organizations o WHERE m.id = o.member_id AND o.dues = 0;")).fetchall()
print("Result of Query3:")
for i in result_query_3:
    print(i, "\n")

print("\n\nContent of DB:")
db.print_members()
db.print_organizations()
db.clear_data()
