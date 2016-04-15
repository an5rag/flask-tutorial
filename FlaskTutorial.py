from flask import Flask
import database
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# cur = database.set_up_db("check.db");
# database.create_table(cur)


@app.route('/')
def hello_world():
    return render_template("index.html",name="isha", wow="wuff")
    # database.insert_comment(cur, "Anurag", "Trying my luck here")
    # print(database.get_comments(cur))

@app.route('/reveal')
def hello_fatty():
    return 'Anurag might have a belly'

@app.route('/okay')
def blah():

    name = request.args.get('name')
    comment = request.args.get('comment')
    con = database.set_up_db("check.db");
    cur= con.cursor()
    database.insert_comment(cur, name, comment)
    con.commit()
    con.close()
    return "Comment added!"

if __name__ == '__main__':
    app.run()
