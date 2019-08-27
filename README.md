# Bitly url shorterer

This script allows you to create a new bitlink or count clicks on an existing bitlink, using API of https://app.bitly.com

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

You can start this script in two ways: 

1. If you need to create a new bitlink, use it!

   	Input:
      ```
      $ python3 create_bitlink.py https://{your_link} --domain {your_own_domain}
      ```

    Output:
   	  ```
      http://{your_own_domain}/{certain_sequence_of_characters}
      ```
   
   OR 

    Input:
      ```
      $ python3 create_bitlink.py https://{your_link} 
      ```
    
    Output:
   	  ```
      http://bit.ly/{certain_sequence_of_characters} 
      ```
    
    If you don't use --domain {your_own_domain}, you'll get a default domain, such as bit.ly

2. You can also count clicks on your existing bitlink!

    Input:
      ```
      $ python3 create_bitlink.py http://bit.ly/{certain_sequence_of_characters} 
      ```
    
    Output:
   	  ```
      Amount of clicks on user bitlink: {certain_value}
      ```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).