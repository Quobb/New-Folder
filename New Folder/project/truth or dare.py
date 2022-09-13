import random

truth=['whats the craziest thing you ever did ','What is your biggest fear?','What is your biggest fantasy?','Do you have any fetishes?',
       'Do you have a hidden talent?','Who was your first celebrity crush?','What are your thoughts on polyamory?','Have you ever cheated in an exam?',
       'Have you ever broken the law?','What is your biggest insecurity?','Have you ever peed in the shower?','What is your biggest regret?']
dare=['Show the last five people you texted and what the messages said','Show the most embarrassing photo on your phone','Do 100 squats',
      'Yell out the first word that comes to your mind','Give a lap dance to someone of your choice','Send a sext to the last person in your phonebook',
      'Show off your orgasm face','Do your best sexy crawl','Pretend to be the person to your right for 10 minutes','Twerk for a minute',
      'Try to put your whole fist in your mouth','Try to lick your elbow','Post the oldest selfie on your phone on Instagram Stories']
print("welcome to truth or dare")

option=input("choice option \n1)Truth \n2)dare\n")
if option=='1':
    print(random.sample(truth,1))
    ask = input("1)continue\n 2)quit\n")
elif option=='2':
    print(random.sample(dare,1))
    ask = input("1)continue\n 2)quit\n")
while ask == '1':
    option = input("choice option \n1)Truth \n2)dare\n")
    if option == '1':
        print(random.sample(truth, 1))
        ask = input("1)continue\n 2)quit\n")
    elif option == '2':
        print(random.sample(dare, 1))
        ask = input("1)continue\n 2)quit\n")

