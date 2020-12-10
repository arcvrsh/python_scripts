from sqlalchemy.orm import sessionmaker
from orm_file import Game
from sqlalchemy import create_engine

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()


print("Welcome to Gamedb")
while True:
    print("***MENU***")
    print("1. View Games")
    print("2. Add Game")
    print('3.exit')
    op = input('Choose any option : ')

    if op == '1':
        results = sess.query(Game).all()
        for game in results:
            print("ID : ",game.id)
            print("Game_Name :",game.game_name)
            print("Publisher :",game.publisher)
            print()
    elif op == '2':
        print('Add new game info')
        game_name = input("Game_Name ->")
        publisher = input("Publisher ->")
        yr = input("YEAR ->")

        if game_name and publisher and yr:
            yr = int(yr)

            obj = Game(game_name = game_name,publisher = publisher,year=yr)
            sess.add(obj)
            sess.commit()
            print("saved game info")

    elif op == '3': 
        import sys
        sys.exit(0)
    else:
        print("wrong option, choose correct options")