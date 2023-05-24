import mysql.connector
import pyodbc
import pandas as pd
import warnings
from tabulate import tabulate

warnings.filterwarnings('ignore')

mydb = mysql.connector.connect(host="localhost", user="root", password="Vista2733!@", auth_plugin='mysql_native_password', database="nba")

mycursor = mydb.cursor()

def options():
    print('''
    Select from the following menu options:\n
    1) Create a New Record\n
    2) Update an Existing Record\n
    3) Delete a Record\n
    4) Display a Table\n
    5) Generate a Report\n
    6) Find Specific Stats\n
    7) Exit
    ''')

    option = int(input("Option: "))

    return option

def update_existing_record():
    print("What table would you like to update?")
    print('''
    1) Player
    2) Team
    3) Games
    4) Game Details
    5) Ranking
    6) Back
    ''')

    option = int(input("Option: "))

    if option == 1:
        print("You have selected Player")
        print("What would you like to update?")
        print('''
        1) Team ID
        2) First Name
        3) Last Name
        4) Age
        5) Total Games Played
        6) Back to Main Menu
        ''')

        choice = int(input("Option: "))

        match choice:
            case 1:
                try:
                    ## Getting user input
                    player_id = input("Player ID: ")
                    team_id = input("New Team ID: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE players SET team_id = '"+str(team_id)+"' WHERE player_id = '"+str(player_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM players WHERE player_ID = '"+str(player_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))

            case 2:
                try:
                    ## Getting user input
                    player_id = input("Player ID: ")
                    first = input("New First Name: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE players SET playerFirst = '"+str(first)+"' WHERE player_id = '"+str(player_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM players WHERE player_ID = '"+str(player_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))

            case 3:
                try:
                    ## Getting user input
                    player_id = input("Player ID: ")
                    last = input("New Last Name: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE players SET playerLast = '"+str(last)+"' WHERE player_id = '"+str(player_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM players WHERE player_ID = '"+str(player_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))

            case 4:
                try:
                    ## Getting user input
                    player_id = input("Player ID: ")
                    age = input("New Age: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE players SET age = '"+str(age)+"' WHERE player_id = '"+str(player_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM players WHERE player_ID = '"+str(player_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))

            case 5:
                try:
                    ## Getting user input
                    player_id = input("Player ID: ")
                    games = input("New Total Games Played: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE players SET totalGames = '"+str(games)+"' WHERE player_id = '"+str(player_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM players WHERE player_ID = '"+str(player_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))

            case 6:
                return ""

            case _:
                print("Invalid option")

    elif option == 2:
        print("You have selected Team")
        print("What would you like to update?")
        print('''
        1) City
        2) Arena
        3) Team Name
        4) Back to Main Menu
        ''')

        choice = int(input("Option: "))

        match choice:
            case 1:
                try:
                    ## Getting user input
                    team_id = input("Team ID: ")
                    city = input("New City: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE team SET city = '"+str(city)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM team WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'teamName', 'city', 'arena'], tablefmt='psql', colalign=("right", "right", "right", "right")))

            case 2:
                try:
                    ## Getting user input
                    team_id = input("Team ID: ")
                    arena = input("New Arena: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE team SET arena = '"+str(arena)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM team WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'teamName', 'city', 'arena'], tablefmt='psql', colalign=("right", "right", "right", "right")))

            case 3:
                try:
                    ## Getting user input
                    team_id = input("Team ID: ")
                    team_name = input("New Team Name: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE team SET teamName = '"+str(team_name)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM team WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'teamName', 'city', 'arena'], tablefmt='psql', colalign=("right", "right", "right", "right")))

            case 4:
                return ""

            case _:
                print("Invalid option")

    elif option == 3:
        print("You have selected Games")
        print("What would you like to update?")
        print('''
        1) Game Date
        2) Home Team
        3) Away Team
        4) Victory
        5) Back to Main Menu
        ''')

        choice = int(input("Option: "))

        match choice:
            case 1:
                try:
                    ## Getting user input
                    game_id = input("Game ID: ")
                    game_date = input("New Game Date: ")

                    ## Creating the query and executing it
                    mycursor.execute("UPDATE games SET gameDATE = '"+str(game_date)+"' WHERE game_id = '"+str(game_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM games WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['game_ID', 'gameDATE', 'homeTeam', 'visitorTeam', 'victory'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 2:
                try:
                    ## Getting user input
                    game_id = input("Game ID: ")
                    home_team = input("New Home Team: ")

                    ## Creating the query and executing it
                    mycursor.execute("SELECT team_id FROM team WHERE teamName = '"+home_team+"'")
                    homeid = mycursor.fetchone()[0]
                    mycursor.execute("UPDATE games SET hometeam = '"+str(homeid)+"' WHERE game_id = '"+str(game_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM games WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['game_ID', 'gameDATE', 'homeTeam', 'visitorTeam', 'victory'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 3:
                try:
                    ## Getting user input
                    game_id = input("Game ID: ")
                    away_team = input("New Away Team: ")

                    ## Creating the query and executing it
                    mycursor.execute("SELECT team_id FROM team WHERE teamName = '"+away_team+"'")
                    awayid = mycursor.fetchone()[0]
                    mycursor.execute("UPDATE games SET visitorteam = '"+str(awayid)+"' WHERE game_id = '"+str(game_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Displaying the updated record
                mycursor.execute("SELECT * FROM games WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['game_ID', 'gameDATE', 'homeTeam', 'visitorTeam', 'victory'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 4:
                try:
                    ## Getting user input
                    game_id = input("Game ID: ")
                    victory = input("New Victory (0 for loss or 1 for win): ")

                    ## Creating the SQL query and executing it
                    mycursor.execute("UPDATE games SET victory = '"+str(victory)+"' WHERE game_id = '"+str(game_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Printing the updated record
                mycursor.execute("SELECT * FROM games WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['game_ID', 'gameDATE', 'homeTeam', 'visitorTeam', 'victory'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 5:
                return ""

            case _:
                print("Invalid option")

    elif option == 4:
        print("You have selected Game Details")
        print("What would you like to update?")
        print('''
        1) Game ID
        2) Team ID
        3) Minutes Played
        4) Points
        5) Rebounds
        6) Assists
        7) Field Goal Percentage
        8) Back to Main Menu
        ''')

        choice = int(input("Option: "))

        match choice:
            case 1:
                try:
                    ## Getting user input
                    detail_id = input("Detail ID: ")
                    game_id = input("New Game ID: ")

                    ## Creating the SQL query and executing it
                    mycursor.execute("UPDATE games_details SET game_id = '"+str(game_id)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Printing the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(detail_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 2:
                try:
                    ## Getting user input
                    detail_id = input("Detail ID: ")
                    team_id = input("New Team ID: ")

                    ## Creating SQL query and executing it
                    mycursor.execute("UPDATE games_details SET team_id = '"+str(team_id)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Printing the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(detail_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 3:
                try:
                    ## Getting user input
                    detail_id = input("Detail ID: ")
                    minutes = input("New Minutes Played: ")

                    ## Creating SQL query and executing it
                    mycursor.execute("UPDATE games_details SET minPlayed = '"+str(minutes)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Printing the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 4:
                try:
                    ## Getting user input
                    detail_id = input("Detail ID: ")
                    points = input("New Points: ")

                    ## Creating SQL query and executing it
                    mycursor.execute("UPDATE games_details SET points = '"+str(points)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Printing the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 5:
                try:
                    ## Getting user input
                    detail_id = input("Detail ID: ")
                    rebounds = input("New Rebounds: ")

                    ## Creating SQL query and executing it
                    mycursor.execute("UPDATE games_details SET rebounds = '"+str(rebounds)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Print the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 6:
                try:
                    ## Get user input
                    detail_id = input("Detail ID: ")
                    assists = input("New Assists: ")

                    ## Creating SQL query and executing it
                    mycursor.execute("UPDATE games_details SET assists = '"+str(assists)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Print the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 7:

                try:
                    ## Get user input
                    detail_id = input("Detail ID: ")
                    fieldGoal = input("New Field Goal Percentage: ")

                    ## Create SQL query and execute it
                    mycursor.execute("UPDATE games_details SET fieldGoal = '"+str(fieldGoal)+"' WHERE detail_id = '"+str(detail_id)+"'")
                    mydb.commit()

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()


                ## Print the updated record
                mycursor.execute("SELECT * FROM games_details WHERE game_ID = '"+str(game_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'playerID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

            case 8:
                return ""

            case _:
                print("Invalid option")

    elif option == 5:
        print("You have selected Ranking")
        print("What would you like to update?")
        print('''
        1) Conference
        2) Total Games
        3) Wins
        4) Losses
        5) Back to Main Menu
        ''')

        choice = int(input("Option: "))

        match choice:
            case 1:

                try:
                    ## Get user input
                    team_id = input("Team ID: ")
                    conference = input("New Conference: ")

                    ## Create SQL query and execute it
                    mycursor.execute("UPDATE ranking SET conference = '"+str(conference)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Print the updated record
                mycursor.execute("SELECT * FROM ranking WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'conference', 'totalGames', 'wins', 'losses'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 2:

                try:
                    ## Get user input
                    team_id = input("Team ID: ")
                    totalGames = input("New Total Games: ")

                    ## Create SQL query and execute it
                    mycursor.execute("UPDATE ranking SET totalGames = '"+str(totalGames)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Print the updated record
                mycursor.execute("SELECT * FROM ranking WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'conference', 'totalGames', 'wins', 'losses'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 3:

                try:
                    ## Get user input
                    team_id = input("Team ID: ")
                    wins = input("New Wins: ")

                    ## Create SQL query and execute it
                    mycursor.execute("UPDATE ranking SET wins = '"+str(wins)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Print the updated record
                mycursor.execute("SELECT * FROM ranking WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'conference', 'totalGames', 'wins', 'losses'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 4:

                try:
                    ## Get user input
                    team_id = input("Team ID: ")
                    losses = input("New Losses: ")

                    ## Create SQL query and execute it
                    mycursor.execute("UPDATE ranking SET losses = '"+str(losses)+"' WHERE team_id = '"+str(team_id)+"'")
                    mydb.commit()
                    print("Record updated successfully")

                ## If something went wrong, rollback changes
                except mysql.connector.Error as error:
                    print("Something went wrong: {}".format(error))

                    mydb.rollback()

                ## Print the updated record
                mycursor.execute("SELECT * FROM ranking WHERE team_ID = '"+str(team_id)+"'")
                myresult = mycursor.fetchall()
                print(tabulate(myresult, headers=['team_ID', 'conference', 'totalGames', 'wins', 'losses'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

            case 5:
                return ""

            case _:
                print("Invalid option")

    elif option == 6:
        return ""

    else:
        print("Invalid option")

def print_all_table():
    print("What table would you like to print?")
    print('''
    1) Player
    2) Team
    3) Games
    4) Game Details
    5) Ranking
    6) Back to Main Menu
    ''')

    option = int(input("Option: "))

    if option == 1:
        print("You have selected Player")

        ## Getting the data from the database
        mycursor.execute("SELECT * FROM players")
        myresult = mycursor.fetchall()

        ## Printing the data
        print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))
        print("\n")

    elif option == 2:
        print("You have selected Team")

        ## Getting the data from the database
        mycursor.execute("SELECT * FROM team")
        myresult = mycursor.fetchall()

        ## Printing the data
        print(tabulate(myresult, headers=['team_ID', 'teamName', 'city', 'arena'], tablefmt='psql', colalign=("right", "right", "right", "right")))
        print("\n")

    elif option == 3:
        print("You have selected Games")

        ## Getting the data from the database
        mycursor.execute("SELECT * FROM games")
        myresult = mycursor.fetchall()

        ## Printing the data
        print(tabulate(myresult, headers=['game_ID', 'gameDate', 'homeTeam', 'visitorTeam', 'victory'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))
        print("\n")

    elif option == 4:
        print("You have selected Game Details")

        ## Getting the data from the database
        mycursor.execute("SELECT * FROM games_details")
        myresult = mycursor.fetchall()

        ## Printing the data
        print(tabulate(myresult, headers=['detail_ID', 'game_ID', 'team_ID', 'player_ID', 'minPlayed', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right")))
        print("\n")

    elif option == 5:
        print("You have selected Ranking")

        ## Getting the data from the database
        mycursor.execute("SELECT * FROM ranking")
        myresult = mycursor.fetchall()
        
        ## Printing the data
        print(tabulate(myresult, headers=['team_ID', 'conference', 'totalGames', 'wins', 'losses'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))
        print("\n")

    elif option == 6:
        return ""

    else:
        print("Invalid option")

def generate_report():
    print("What table would you like to generate?")
    print('''
    1) Player
    2) Team
    3) Games
    4) Game Details
    5) Ranking
    6) Back to Main Menu
    ''')

    option = int(input("Option: "))

    if option == 1:

        ## Create a Pandas dataframe from the data.
        script = """
        SELECT * FROM players
        """

        ## Create a Pandas Excel writer using XlsxWriter as the engine.
        df = pd.read_sql_query(script, mydb)

        ## Convert the dataframe to an XlsxWriter Excel object.
        df = df.to_excel('players.xlsx', index=False)

    elif option == 2:

        ## Create a Pandas dataframe from the data.
        script = """
        SELECT * FROM team
        """

        ## Create a Pandas Excel writer using XlsxWriter as the engine.
        df = pd.read_sql_query(script, mydb)

        ## Convert the dataframe to an XlsxWriter Excel object.
        df = df.to_excel('team.xlsx', index=False)

    elif option == 3:

        ## Create a Pandas dataframe from the data.
        script = """
        SELECT * FROM games
        """

        ## Create a Pandas Excel writer using XlsxWriter as the engine.
        df = pd.read_sql_query(script, mydb)

        ## Convert the dataframe to an XlsxWriter Excel object.
        df = df.to_excel('games.xlsx', index=False)

    elif option == 4:

        ## Create a Pandas dataframe from the data.
        script = """
        SELECT * FROM games_details
        """

        ## Create a Pandas Excel writer using XlsxWriter as the engine.
        df = pd.read_sql_query(script, mydb)

        ## Convert the dataframe to an XlsxWriter Excel object.
        df = df.to_excel('games_details.xlsx', index=False)
    
    elif option == 5:

        ## Create a Pandas dataframe from the data.
        script = """
        SELECT * FROM ranking
        """

        ## Create a Pandas Excel writer using XlsxWriter as the engine.
        df = pd.read_sql_query(script, mydb)

        ## Convert the dataframe to an XlsxWriter Excel object.
        df = df.to_excel('ranking.xlsx', index=False)

    elif option == 6:
        return ""

    else:
        print("Invalid option")

def create_new_record():
    print("What table would you like to insert into?")
    print('''
    1) Player
    2) Team
    3) Games
    4) Game Details
    5) Ranking
    6) Back to Main Menu
    ''')

    option = int(input("Option: "))

    if option == 1:
        try:
            print("You have selected Player")

            ## Get user input
            player_id = input("Player ID: ")
            team_id = input("Team ID: ")
            first = input("First Name: ")
            last = input("Last Name: ")
            age = input("Age: ")
            gamesPlayed = input("Games Played: ")

            ## Create the SQL command
            sql = "INSERT INTO players (player_id, team_id, playerFirst, playerLast, playerAge, totalGames) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (player_id, team_id, first, last, age, gamesPlayed)

            ## Execute the SQL command and commit changes
            mycursor.execute(sql, val)
            mydb.commit()
            print("\nRecord inserted successfully\n")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

        ## Print the results
        mycursor.execute("SELECT * FROM players WHERE player_ID = '"+str(player_id)+"'")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['player_ID', 'team_ID', 'playerFirst', 'playerLast', 'playerAge', 'totalGames'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right")))

    elif option == 2:
        try:
            print("You have selected Team")

            ## Get user input
            team_id = input("Team ID: ")
            team_city = input("City: ")
            team_arena = input("Arena: ")

            ## Create the SQL command
            sql = "INSERT INTO team (team_id, city, arena) VALUES (%s, %s, %s)"
            val = (team_id, team_city, team_arena)

            ## Execute the SQL command and commit changes
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record inserted successfully")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

        ## Print the results
        mycursor.execute("SELECT * FROM team WHERE team_ID = '"+str(team_id)+"'")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['team_ID', 'city', 'arena'], tablefmt='psql', colalign=("right", "right", "right")))

    elif option == 3:
        try:
            print("You have selected Games")

            ## Get user input
            game_id = input("Game ID: ")
            game_date = input("Date (yyyy-mm-dd): ")
            home_team = input("Home Team: ")
            away_team = input("Away Team: ")
            victory = input("Victory for home team(0 for loss or 1 for win): ")

            mycursor.execute("SELECT team_id FROM team WHERE teamName = '"+home_team+"'")
            homeid = mycursor.fetchone()[0]
            mycursor.execute("SELECT team_id FROM team WHERE teamName = '"+away_team+"'")
            awayid = mycursor.fetchone()[0]

            ## Need to also change the wins from the Ranking table
            ## If home was the winner, add a win to the home team and a loss to the away team
            if victory == "1":
                mycursor.execute("SELECT wins FROM ranking WHERE team_id = '"+str(homeid)+"'")
                addWin = mycursor.fetchone()[0]
                addWin = addWin + 1
                mycursor.execute("UPDATE ranking SET wins = '"+str(addWin)+"' WHERE team_id = '"+str(homeid)+"'")
                mydb.commit()
                mycursor.execute("SELECT losses FROM ranking WHERE team_id = '"+str(awayid)+"'")
                addLoss = mycursor.fetchone()[0]
                addLoss = addLoss + 1
                mycursor.execute("UPDATE ranking SET losses = '"+str(addLoss)+"' WHERE team_id = '"+str(awayid)+"'")
                mydb.commit()

            ## If away was the winner, add a win to the away team and a loss to the home team
            elif victory == "0":
                mycursor.execute("SELECT wins FROM ranking WHERE team_id = '"+str(awayid)+"'")
                addWin = mycursor.fetchone()[0]
                addWin = addWin + 1
                mycursor.execute("UPDATE ranking SET wins = '"+str(addWin)+"' WHERE team_id = '"+str(awayid)+"'")
                mydb.commit()
                mycursor.execute("SELECT losses FROM ranking WHERE team_id = '"+str(homeid)+"'")
                addLoss = mycursor.fetchone()[0]
                addLoss = addLoss + 1
                mycursor.execute("UPDATE ranking SET losses = '"+str(addLoss)+"' WHERE team_id = '"+str(homeid)+"'")
                mydb.commit()

            ## Create the SQL command
            sql = "INSERT INTO games (game_id, gameDATE, hometeam, visitorteam, victory) VALUES (%s, %s, %s, %s, %s)"
            val = (game_id, game_date, home_team, away_team, victory)

            ## Execute the SQL command and commit changes
            mycursor.execute(sql, val)
            mydb.commit()

            print("Record inserted successfully")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

        ## Print the results
        mycursor.execute("SELECT * FROM games WHERE game_ID = '"+str(game_id)+"'")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['game_ID', 'gameDATE', 'home_team', 'away_team', 'victory'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

    elif option == 4:
        try:
            print("You have selected Game Details")

            ## Get user input
            detail_id = input("Detail ID: ")
            game_id = input("Game ID: ")
            team_id = input("Team ID: ")
            playerid = input("Player ID: ")
            minutes = input("Minutes Played: ")
            points = input("Points: ")
            rebounds = input("Rebounds: ")
            assists = input("Assists: ")
            fieldGoal = input("Field Goal Percentage (to two decimal places): ")

            ## Create the SQL command
            sql = "INSERT INTO games_details (detail_id, game_id, team_id, playerid, minplayed, points, rebounds, assists, fieldGoal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (game_id, team_id, playerid, minutes, points, rebounds, assists, fieldGoal)

            ## Execute the SQL command and commit changes
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record inserted successfully")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

        ## Print the results
        mycursor.execute("SELECT * FROM games_details WHERE detail_id = '"+str(detail_id)+"'")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['detail_id', 'game_id', 'team_id', 'playerid', 'minutes', 'points', 'rebounds', 'assists', 'fieldGoal'], tablefmt='psql', colalign=("right", "right", "right", "right", "right", "right", "right", "right", "right")))

    elif option == 5:
        try:
            print("You have selected Ranking")

            ## Get user input
            team_id = input("Team ID: ")
            conference = input("Conference: ")
            totalGames = input("Total Games: ")
            wins = input("Wins: ")
            losses = input("Losses: ")

            ## Create the SQL command
            sql = "INSERT INTO ranking (team_ID, conference, totalGames, wins, losses) VALUES (%s, %s, %s, %s, %s)"
            val = (team_id, conference, totalGames, wins, losses)

            ## Execute the SQL command and commit changes
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record inserted successfully")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

        ## Print the results
        mycursor.execute("SELECT * FROM ranking WHERE team_id = '"+str(team_id)+"'")
        myresult = mycursor.fetchall()
        print(tabulate(myresult, headers=['team_id', 'conference', 'totalGames', 'wins', 'losses'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))

    elif option == 6:
        return ""

    else:
        print("Invalid option")

def delete_record():
    print("What table would you like to delete from?")
    print('''
    1) Player
    2) Team
    3) Games
    4) Game Details
    5) Ranking
    6) Back to Main Menu
    ''')

    option = int(input("Option: "))

    if option == 1:
        try:
            print("You have selected Player")

            ## Get user input for player ID
            player_id = input("Player ID: ")

            ## Delete player from player table
            sql = "DELETE FROM players WHERE player_id = '"+str(player_id)+"'"

            ## Execute the SQL command and commit changes
            mycursor.execute(sql)
            mydb.commit()

            ## Need to also delete all records of this player from games_details table
            sql = "DELETE FROM games_details WHERE playerid = '"+str(player_id)+"'"

            ## Execute the SQL command and commit changes
            mycursor.execute(sql)
            mydb.commit()

            print("\nAll records of this player has been deleted successfully\n")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

    elif option == 2:
        try:
            print("You have selected Team")

            ## Get user input for team ID
            team_id = input("Team ID: ")
            sql = "DELETE FROM team WHERE team_id = '"+str(team_id)+"'"

            ## Execute the SQL command and commit changes
            mycursor.execute(sql)
            mydb.commit()
            print("All records of this team has been deleted successfully")

            ## Also need to delete all other records where the team ID is referenced
            sql = "DELETE FROM games WHERE hometeam = '"+str(team_id)+"' OR visitorteam = '"+str(team_id)+"'"
            mycursor.execute(sql)
            mydb.commit()

            sql = "DELETE FROM games_details WHERE team_id = '"+str(team_id)+"'"
            mycursor.execute(sql)
            mydb.commit()

            sql = "DELETE FROM team WHERE team_id = '"+str(team_id)+"'"
            mycursor.execute(sql)
            mydb.commit()

            sql = "DELETE FROM ranking WHERE team_id = '"+str(team_id)+"'"
            mycursor.execute(sql)
            mydb.commit()

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

    elif option == 3:
        try:
            print("You have selected Games")

            ## Get user input for game ID
            game_id = input("Game ID: ")
            sql = "DELETE FROM games WHERE game_id = '"+str(game_id)+"'"

            ## Execute the SQL command and commit changes
            mycursor.execute(sql)
            mydb.commit()
            print("All records of this game has been deleted successfully")

            ## Also need to delete all other records where the game ID is referenced
            sql = "DELETE FROM games_details WHERE game_id = '"+str(game_id)+"'"
            mycursor.execute(sql)
            mydb.commit()

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

    elif option == 4:
        try:
            print("You have selected Game Details")

            ## Get user input for game ID and player ID
            detail_id = input("Details ID: ")
            player_id = input("Player ID: ")
            sql = "DELETE FROM games_details WHERE detail_id = '"+str(detail_id)+"' AND player_id = '"+str(player_id)+"'"

            ## Execute the SQL command and commit changes
            mycursor.execute(sql)
            mydb.commit()
            print("All records of this game has been deleted successfully")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

    elif option == 5:
        try:
            print("You have selected Ranking")

            ## Get user input for team ID
            team_id = input("Team ID: ")
            sql = "DELETE FROM ranking WHERE team_id = '"+str(team_id)+"'"

            ## Execute the SQL command and commit changes
            mycursor.execute(sql)
            mydb.commit()
            print("All records of this team has been deleted successfully")

        ## If something went wrong, rollback changes
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))

            mydb.rollback()

    elif option == 6:
        return ""

    else:
        print("Invalid option")

## This function allows users to find specific stats
def find_stats():
    print("What stats do you want to see?")
    print('''
    1) All players who scored 20 or more points in a game and what day.\n
    2) All players who got 10 or more rebounds in a game and what day.\n
    3) All players who got 6 or more assists in a game and what day.\n
    4) All players who got a higher field goal percentage than 50% in a game and what day.\n
    5) Number of teams that (on average) play more than 10 players per game.\n
    6) All players who got at least 5 points, 5 assists, and 5 rebounds in a game and what day.\n
    7) Back to main menu
    ''')

    ## User Input
    option = int(input("Option: "))

    ## If user selects option 1
    if option == 1:
        print("You have selected All players who scored 20 or more points in a game and what day.")

        ## Creatin query using joins across three tables
        sql = '''SELECT CONCAT(playerFirst, " ", playerLast), g.gameDate, gd.points FROM players as p 
        INNER JOIN games_details AS gd ON p.player_ID = gd.playerID
        INNER JOIN games AS g on gd.game_ID = g.game_ID
        WHERE points >= 20;
        '''

        ## Execute the SQL command
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        ## Using tabulate to print the results in a table
        print(tabulate(myresult, headers=['Player Name', 'Game Date', 'Points'], tablefmt='psql', colalign=("right", "right", "right")))
        print("\n")

    ## If user selects option 2
    elif option == 2:
        print("You have selected All players who got 10 or more rebounds in a game and what day.")

        ## Creating query using joins across three tables
        sql = '''
        SELECT CONCAT(playerFirst, " ", playerLast), g.gameDate, gd.rebounds
        FROM players as p
        INNER JOIN games_details AS gd ON p.player_ID = gd.playerID
        INNER JOIN games AS g on gd.game_ID = g.game_ID
        WHERE rebounds >= 10;
        '''

        ## Execute the SQL command
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        ## Using tabulate to print the results in a table
        print(tabulate(myresult, headers=['Player Name', 'Game Date', 'Rebounds'], tablefmt='psql', colalign=("right", "right", "right")))
        print("\n")

    ## If user selects option 3
    elif option == 3:

        ## Creating query using joins across three tables
        print("You have selected All players who got 6 or more assists in a game and what day.")
        sql = '''
        SELECT CONCAT(playerFirst, " ", playerLast), g.gameDate, gd.rebounds
        FROM players as p
        INNER JOIN games_details AS gd ON p.player_ID = gd.playerID
        INNER JOIN games AS g on gd.game_ID = g.game_ID
        WHERE rebounds >= 6;
        '''

        ## Execute the SQL command
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        ## Using tabulate to print the results in a table
        print(tabulate(myresult, headers=['Player Name', 'Game Date', 'Assists'], tablefmt='psql', colalign=("right", "right", "right")))
        print("\n")

    ## If user selects option 4
    elif option == 4:
        print("You have selected All players who got a higher field goal percentage than 50% in a game and what day.")

        ## Query using joins across three tables
        sql = '''
        SELECT CONCAT(playerFirst, " ", playerLast), g.gameDate, gd.fieldGoal
        FROM players as p
        INNER JOIN games_details AS gd ON p.player_ID = gd.playerID
        INNER JOIN games AS g on gd.game_ID = g.game_ID
        WHERE fieldGoal >= .50;
        '''

        ## Execute the SQL command
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        ## Using tabulate to print the results in a table
        print(tabulate(myresult, headers=['Player Name', 'Game Date', 'Field Goal'], tablefmt='psql', colalign=("right", "right", "right")))
        print("\n")

    ## If user selects option 5
    elif option == 5:
        print("You have selected Number of teams that (on average) play more than 10 players per game.")

        ## Query using joins across three tables
        sql = '''
        SELECT COUNT(*)
        FROM (
            SELECT team_ID,  COUNT(DISTINCT playerID) as playerCount
            FROM games_details
            GROUP BY team_ID
            HAVING (playerCount / COUNT(DISTINCT game_ID) ) > 10
        ) AS ct;
        '''

        ## Execute the SQL command
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        ## Using tabulate to print the results in a table
        print(tabulate(myresult, headers=['Number of Teams'], tablefmt='psql'))
        print("\n")

    ## If user selects option 6
    elif option == 6:
        print("You have selected All players who got at least 5 points, 5 assists, and 5 rebounds in a game and what day.")

        ## Using a view to find the selected option
        sql = '''
        SELECT * FROM with5;
        '''

        ## Execute the SQL command
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        ## Using tabulate to print the results in a table
        print(tabulate(myresult, headers=['Player Name', 'Points', 'Rebounds', 'Assists', 'Game Date'], tablefmt='psql', colalign=("right", "right", "right", "right", "right")))
        print("\n")
    
    ## If user selects option 7
    elif option == 7:
        return ""

    else:
        print("Invalid option. Please try again.")

# # Main
# # Menu Screen
# print("Welcome to the NBA App!")
while True:
    match options():
        case 1:
            create_new_record()
            input("\nPress Enter to continue...\n")
        case 2:
            update_existing_record()
            input("\nPress Enter to continue...\n")
        case 3:
            delete_record()
            input("\nPress Enter to continue...\n")
        case 4:
            print_all_table()
            input("\nPress Enter to continue...\n")
        case 5:
            generate_report()
            input("\nPress Enter to continue...\n")
        case 6:
            find_stats()
            input("\nPress Enter to continue...\n")
        case 7:
            print("Goodbye!")
            break
        case _:
            print("Invalid option")
            input("\nPress Enter to continue...\n")