import mysql.connector
import os

if (os.environ['USER']=='saurav'):
    pw = 'qwerty@123'
else:
    pw = 'qw'

dbase = 'web'

cnx = mysql.connector.connect(user='root', password=pw,
                                  host='127.0.0.1',
                                  database=dbase)

cursor = cnx.cursor(buffered=True)

def upvote(post_id, username):

	query = ("insert into Post_vote values(%s, %s)")
	cursor.execute(query, (post_id, username))

	cnx.commit()


def downvote(post_id, username):

	query = ("delete from Post_vote where post_id = %s and username = %s")
	cursor.execute(query, (post_id, username))

	cnx.commit()


if __name__ == '__main__':
	downvote(32, 'piyushrathipr')