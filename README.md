# ![8.8] -> ![9.9] twitter_verified_blocker :seedling: 
A tool for blocking all verified users on Twitter. 



--------

### Run with:
 *  `python3 twitter_verified_blocker.py`
 
--------
 

Functional notes:


    1. You will need a Twitter APP Key (apps.twitter.com) for the account you are executing these blocking requests from.
    
    2. You may protect verified accounts (exclude them from being blocked and they will remain in your feed, etc). 
       To do this:
       A. create the Twitter list "exceptions" 
       B. add verified users to "exceptions" 
        
    3. This script will access 3 Twitter user lists, affirm verified users and block them. 
       The three lists are:
       A. the Twitter managed verified user list
       B. the your followers list
       C. the followers list of "@Twitter"

    4. This script has been built to observe rate limits and to use Twitter's API respectfully. 
       This script has been run for over 5 hours with no sign of interuption. 
       After running this script for 20 hours an estimated 300,000 verified users will have been ![9.9]blocked. 
       After 20 hours the user should experience the desired Twitter experience even though new acccounts will be verified regularly.
       
    5. This script can be interupted and when restarted it will skip previously blocked accounts.
    
    6. Do not use any of the code I have written with harmful intent. 
    
    7. By using this code you accept that every person has the right to choose their own gender identity.  
    

Comments, critiques, need help? Contact me [![alt text][6.3]][3]  [![alt text][1.2]][1]

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->
[1.2]: https://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[1]: https://www.twitter.com/AGreenDCBike
[6.3]: http://i.imgur.com/9I6NRUm.png (github icon without padding)
[3]: https://github.com/antoinemcgrath

[8.8]: http://i.imgur.com/ZgNGQi7.png (Twitter verified icon)
[9.9]: http://i.imgur.com/Ycvb3WC.png (Blocked Twitter verified icon)

