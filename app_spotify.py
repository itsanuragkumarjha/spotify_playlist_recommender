import pandas as pd
import streamlit as st

st.markdown("""# What songs were popular when we were in high school?
The algorithm doesn't get us, we hear that a lot. Maybe you want to rediscover the top songs from your high school days. Or maybe you just don't want to mess with making your own playlist. 

I present to you this tool to find a pre-generated playlist on Spotify of every song that made the Top 10 in the US for the years you select. Enjoy :-)
""")

df = pd.read_csv("playlists.csv")
years = list(range(1958, 2022))

year_range = st.slider(label="Start Year", min_value=1958, max_value=2022, value=(1995, 2010))


if st.button('Submit'):
    if (int(year_range[0]) - int(year_range[1])) == 0:
        playlist_name = f"Top US Singles: {year_range[0]}"
    else:
        playlist_name = f"Top US Singles: {year_range[0]}-{year_range[1]}"

    if df[df['name'] == playlist_name].shape[0] > 0:
        playlist = df[df['name'] == playlist_name].to_dict(orient='records')[0]
    else:
        playlist = "Ooops, it looks like we didn't make that playlist yet. Playlists with a range of 1-20 years were created. Try again with a more narrow year range."

    if isinstance(playlist, dict):
        link = f"### Your Spotify Playlist: [{playlist['name']}]({playlist['link']})"
        st.markdown(link, unsafe_allow_html=True)
    else:
        st.markdown(playlist)