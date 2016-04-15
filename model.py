import database




con = database.set_up_db("check.db");
cur= con.cursor()
database.create_table(cur)



database.insert_comment(cur, "Isha", "Trying hard")

print(database.get_comments(cur))
# database.drop_all_tables(cur)

con.commit()
con.close()