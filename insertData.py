from sqliteConnect import *
import time

# create a subroutine to add songs to the songs table in the database


def addNode(valeu, next_node):
    # create an empty list
    nodes = []
    nodes.append(value)
    nodes.append(next_node)
    nodes.append(genre)

    # insert data from the list into songs table

    cursor.execute("INSERT INTO songs VALUES(NULL, ?, ?, ?)", songs)
    conn.commit()  # commit/write changes permanently to the database
    print(f"{title} added to songs table")

    time.sleep(3)

    # select all records from songs table
    cursor.execute("SELECT * FROM songs")

    row = cursor.fetchall()  # fetch all the songs that was selected in the table

    for (
        record
    ) in (
        row
    ):  # iterate through all the records held in the row variable and print one at a time
        print(record)


# addSongs()  # call/invoke the subroutine
