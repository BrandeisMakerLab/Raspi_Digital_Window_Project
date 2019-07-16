#Jacob Smith Brandeis University Makerlab 6/18/2019
#A library of functions useful in interacting with a RasberryPi
#Along with a main method to send a tweet when a button is pressed

#sends a tweet with a picture when a button ispressed
def main():
    import random
    #messages to selectfrom when tweeting
    messages=["HiFolks! Come check out the makerlab!","Look at what's going on over here!","#OurPublicityDepartmentIsAComputer","Automation is our motto, cooperation is our dream","#Collaboration"]
    hashtag="\nMeet us on first floor of Farber in the library\n#BrandeisMakerlab"

    #when the button is pressed,a randomly selected message will be tweeted with a picture
    twitter=importKeys()
    while(True):
        if isButtonPressed():
            print("Taking Picture for Tweet")
            #generate the message for the tweet
            message=random.choice(messages)+hashtag
            tweet(twitter,message)
            print("Tweeted:%s"%message)
    return


#imports a twitter account's keys from auth.py file
#see tweetfunction for link
def importKeys():
    from twython import Twython

    from auth import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

    twitter=Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )
    return twitter

#takes a picture and tweets it with a given message
#needs the twitter object and the message
#https://www.raspberrypi.org/documentation/usage/webcams/
#https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api
def tweet(twitter,message):
    import subprocess
    subprocess.call(["fswebcam","/home/pi/toSend.jpg"]);
    image=open('/home/pi/toSend.jpg','rb')
    response=twitter.upload_media(media=image)
    media_id=[response['media_id']]
    twitter.update_status(status=message,media_ids=media_id)
    return

#returns true if a button wired to ports 18 and ground is pressed
#http://razzpisampler.oreilly.com/ch07.html
def isButtonPressed():
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    input_state=GPIO.input(18)
    #delay for 200 milliseconds so multiple button presses aren't detected
    time.sleep(.2)
    return not input_state

#actually call the main method to run the program
main()