#Importando librerias necesarias
import wikipedia;
from gtts import gTTS;
import os;

#Definimos el lenguaje
wikipedia.set_lang("es");

#Funcion de busqueda
#Covertimos la consulta a un archivo de voz
def search_wikipedia():
    query = input();
    texto = wikipedia.summary(query, sentences=1);
    voz = gTTS(text=texto,lang="es");
    return voz.save("consulta.mp3");
    
    
#Definimos metodo 
search_wikipedia();