import wolframalpha
import wikipedia
import PySimpleGUI as sg
import pyttsx3 #for text to speech

client = wolframalpha.Client("RT85GL-4VV66LR9G6")

sg.theme('DarkBlack')
layout =[[sg.Text('Enter a command'), sg.InputText()],
[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('PVA', layout)

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')


while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=1)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say("Wolfram Result: "+wolfram_res)
        engine.say("Wikipedia Result: "+wiki_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)


    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say("Wolfram Result: "+wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res)


    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say("Wolfram Result: "+wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res)


    except:
        wiki_res = wikipedia.summary(values[0], sentences=1)
        engine.say("Wikipedia Result: "+wiki_res)
        sg.PopupNonBlocking("Wikipedia Result: "+wiki_res)

    engine.runAndWait()

window.close()