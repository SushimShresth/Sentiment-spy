import os
import nltk
import colorama #colortext
from colorama import Fore,Style #fore=text colors/Style=reset, bold
from textblob import TextBlob  # understand text
os.system("")

def print_welcome():
    print(f"{Fore.CYAN}\nWelcome to sentiment spy!{Style.RESET_ALL}\n")
def get_username():
    username=input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
    if username!="":
        return username
    else:
        username="Mystery Agent"
def print_instruction(username):
    print(f"\n{Fore.CYAN}Hello,{username}!{Style.RESET_ALL}")
    print(f"Type any text below, and I'll analyze it's sentiment or Enter '/exit' to quit.\n")

def analyze_sentiment(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity
    if polarity>0:
        sentiment="Positive"
        color="GREEN"
    elif polarity<0:
        sentiment = "Negetive"
        color = "RED"
    elif polarity > 0.5:
        sentiment = "Very Positive"
        color = "GREEN"
    else:
        sentiment = "Neutral"
        color = "YELLOW"
    return sentiment,color,polarity
def display_sentiment(sentiment,text,color,polarity):
    print(f"{Fore.color}Text: {text}{Style.RESET_ALL}")
    print(f"Sentiment: {sentiment}| Polarity: {polarity}\n")

def main():
    print_welcome()
    username=get_username()
    print_instruction(username)
    while True:
        user_input=input(f"{Fore.CYAN}You: {Style.RESET_ALL}").strip()
        if user_input.lower()=="/exit":
            print(f"{Fore.YELLOW}\n Goodbye!,{username} Thanks for using sentiment spy.{Style.RESET_ALL}")
            break
        else:
            sentiment,polarity,color=analyze_sentiment(user_input)
            display_sentiment(sentiment,user_input,color,polarity)

if __name__=="__main__":
    main()
