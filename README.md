# ![9.9] twitter_blocker_tool :seedling: 
A python3 tool for blocking verified accounts. 
To run users will need the Tweepy python package and [Twitter APP Keys](https://apps.twitter.com/)


--------

### Run with:
 *  `python3 twitter_verified_blocker.py`
 
--------
 

Functional notes:

    1. You may protect verified accounts (exclude them from being blocked, they will remain in your feed, etc). To do this:
       A. create the Twitter list "exceptions" 
       B. add verified users to "exceptions" 
         
        
    2. This script will access 3 Twitter user lists, affirm verified users and block them. The three lists are:
       A. the Twitter managed verified user list
       B. the your followers list
       C. the followers list of "@Twitter"

    3. This script has been built to observe rate limits and to use Twitter's API respectfully. 
       A. this script has been run for over 5 hours with no sign of interuption. 
       B. after running this script for 20 hours 300,000 verified users will have been blocked. 
       C. after 20 hours the user should exeperience the desired Twitter experience even though new acccounts will be verified regularly.
    4. This script can be interupted and when restarted it will skip previosuly blocked accounts.
    5. This script can be rerun at will




Comments, critiques? Contact me [![alt text][6.3]][3]  [![alt text][1.2]][1]

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->
[1.2]: https://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[1]: https://www.twitter.com/AGreenDCBike
[6.3]: http://i.imgur.com/9I6NRUm.png (github icon without padding)
[3]: https://github.com/antoinemcgrath

[9.9]: http://i.imgur.com/Ycvb3WC.png (Blocked Twitter verified icon)

