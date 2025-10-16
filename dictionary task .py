chat_response={
'Hello! How can I help you today?': 0.9,
 'I’m sorry, I didn’t understand that.': 0.3,
 'Sure! Here’s what I found on your topic.': 0.8
}
#add uptades 
chat_response["hello !have a nice day "]=0.4
chat_response["give me proper details "]=0.6

#update one existing sentiment score
chat_response['I’m sorry, I didn’t understand that.']=0.97

#Step 3: Access and display data
print("all chatbots messege and sentements score :\n")

#using dictionary  items() 
for messege,scores in chat_response.items():
    print(f"'{messege}'")

#using max () key
highest_messege=max(chat_response,key=chat_response.get)
print("\nMessage with the highest sentiment score:")
print(f"'{highest_messege}'")

#4 perform analysis
#Using sum(Using sum(chat_responses.values()) / len(chat_responses)
average_score=sum(chat_response.values()) / len(chat_response)
print(f"\n average sentiment score of all responses:{average_score:.2f}")
#using chat_responses.values() and chat_responses.keys()
print("all sentement score:",list(chat_response.values()))
print("All Messages:", list(chat_response.keys()))
print("\n messege with the sentiment >0.7 (positive tone):")
for messege in chat_response.items():
    if scores>0.7:
       print(f"'{messege}' → {scores}")