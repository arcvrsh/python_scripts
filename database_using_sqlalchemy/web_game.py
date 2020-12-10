from sqlalchemy.orm import sessionmaker
from orm_file import Game
from sqlalchemy import create_engine

import streamlit as st

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

choice = st.sidebar.selectbox("select option",['Add game','View games'])

if choice == 'Add game':
    st.header("Add game details")
    game_name = st.text_input('enter game name',)
    publisher = st.text_input('enter publisher name')
    year = st.number_input('year of publishing',min_value=1800,max_value=2020,value=2000)
    submit = st.button("save details")
    if submit and game_name and publisher:
        obj = Game(game_name=game_name, publisher = publisher,year = year)
        sess.add(obj)
        sess.commit()
        st.success("game data added")
    else:
        st.warning("please fill valid details")
elif choice =='View games':
    st.header("Displaying all games")
    results = sess.query(Game).all()
    for game in results:
        st.subheader(game.game_name)
        st.text(game.publisher)
        st.text(game.year)
        st.empty()

