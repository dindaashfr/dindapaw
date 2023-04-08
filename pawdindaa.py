# library
import streamlit as st

# write
st.title('DUNIA DINOSAURUS')
st.write('DINOSAURUS LUCU BANGET LOCHH!!!')

st.image('dino 5.jpg')

if st.button(''):
    st.balloons()
    
# macam macam dino
list_dino = ['tyrannosaurus','vulcanodon', 'pterodactylus']
jenis_dino = st.selectbox('Masukan Jenis Dinosaurus', list_dino)

if jenis_dino == 'tyrannosaurus':
    st.image('dino 1.jpg')
if jenis_dino == 'vulcanodon':
    st.image('dino 4.jpg')
if jenis_dino == 'pterodactylus':
    st.image('dino 3.jpg')
    
    
    
    
# write
st.title('SIAPA YANG MAU JADI VVIBU?!?!?')


if st.button('akuu'):
    st.write('aku bang aku banggggg :v')
    st.image('wibu 1.jpg')
    
# reccommen anime sad ending
st.writte('Kamu suka anime yang sedih?? mimin bakal kasih tau nih top 5 anime paling sedih')
# macam macam anime
list_anime = ['YOUR LIE IN APRIL','ANOHANA','YOUR NAME','HELLO WORLD','AO HARU RIDE']
judul_anime = st.selectbox('Masukkan judul anime',list_anime)
    
    
    
    
    
    
    
    
   
    
