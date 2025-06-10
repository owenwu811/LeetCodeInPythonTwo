#3368
#hard

#Write a solution to transform the text in the content_text column by applying the following rules:

#Convert the first letter of each word to uppercase
#Keep all other letters in lowercase
#Preserve all existing spaces
#Note: There will be no special character in content_text.

#Return the result table that includes both the original content_text and the modified text where each word starts with a capital letter.

#The result format is in the following example.

#my own solution using python3:

#copy content_text into a new column called converted text, and then use title on each row

import pandas as pd


def process_text(user_content: pd.DataFrame) -> pd.DataFrame:
    #user_content['original_text'] = user_content['content_text']
    #user_content['content_text'] = user_content['original_text']
    user_content['original_text'] = user_content['content_text']
    #for i, a in enumerate(user_content['content_text']):
        #print(a)
        #print(a)
        
        
    user_content['converted_text'] = user_content['content_text']
    for i, a in enumerate(user_content['converted_text']):
        user_content['converted_text'][i] = user_content['converted_text'][i].title()
    return pd.DataFrame(user_content, columns=['content_id', 'original_text', 'converted_text'])
