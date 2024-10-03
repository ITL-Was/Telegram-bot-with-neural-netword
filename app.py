import os,telebot;from dotenv import load_dotenv;from groq import Groq;load_dotenv();a,b=Groq(api_key=os.getenv("G")),telebot.TeleBot(os.getenv("T"));c,d={},75
@b.message_handler(commands=['cont'])
def h(m):b.send_message(m.from_user.id,"Context cleared");c[m.from_user.id]=[]
@b.message_handler(content_types=['text'])
def k(x):e=x.from_user.id;c.setdefault(e,[]).append({"role":'user',"content":f"{x.from_user.username or'User'}:{x.text}"});c[e]=c[e][-d:]; b.send_message(e,(r:=a.chat.completions.create(model='llama-3.1-70b-versatile',messages=c[e]+[{"role":"system","content":os.getenv('S')}],temperature=0.3).choices[0].message.content.strip()));c[e].append({"role":'assistant',"content":r})
b.polling()