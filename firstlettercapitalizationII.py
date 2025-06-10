#3374
#hard

#Write a solution to transform the text in the content_text column by applying the following rules:

#Convert the first letter of each word to uppercase and the remaining letters to lowercase
#Special handling for words containing special characters:
#For words connected with a hyphen -, both parts should be capitalized (e.g., top-rated → Top-Rated)
#All other formatting and spacing should remain unchanged
#Return the result table that includes both the original content_text and the modified text following the above rules.

#The result format is in the following example.

#my own solution using python3:

#just copy the columns and then iterate and use .title()

import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    
    user_content['original_text'] = user_content['content_text']
    user_content['converted_text'] = user_content['content_text']
    for i, a in enumerate(user_content['converted_text']):
        user_content['converted_text'][i] = user_content['converted_text'][i].title()

    return pd.DataFrame(user_content, columns=['content_id', 'original_text', 'converted_text'])
