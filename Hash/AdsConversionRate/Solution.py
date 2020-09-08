"""
The people who buy ads on our network don't have enough data about how ads are working for
their business. They've asked us to find out which ads produce the most purchases on their website.

Our client provided us with a list of user IDs of customers who bought something on a landing page
after clicking one of their ads:

# Each user completed 1 purchase.
completed_purchase_user_ids = [
  "3123122444","234111110", "8321125440", "99911063"]

And our ops team provided us with some raw log data from our ad server showing every time a
user clicked on one of our ads:
ad_clicks = [
 #"IP_Address,Time,Ad_Text",
 "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
 "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
 "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
 "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
 "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
 "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
       
The client also sent over the IP addresses of all their users.
       
all_user_ips = [
 #"User_ID,IP_Address",
  "2339985511,122.121.0.155",
 "234111110,122.121.0.1",
 "3123122444,92.130.6.145",
 "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
 "8321125440,82.1.106.8",
 "99911063,92.130.6.144"
]

Expected output:
Bought Clicked Ad Text
1 of 2  2017 Pet Mittens
0 of 1  The Best Hollywood Coats
3 of 3  Buy wool coats for your pets
"""
import collections

# construct {ip: userid}
# construct set(usersid)
def AdsConversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips):
    purchasedUserIds = set(completed_purchase_user_ids)
    ip_userId_dict = { pair.split(",")[1] : pair.split(",")[0] for pair in all_user_ips }
    text_ip_dict = collections.defaultdict(list)
    res = collections.defaultdict(list)
    for pair in ad_clicks:
        text = pair.split(",")[2]
        ip = pair.split(",")[0]
        # print("text: {}, ip: {}".format(text, ip))
        text_ip_dict[text].append(ip)
        res[text] = [0, 0]

    # print("purchasedUserIds: {}".format(purchasedUserIds))
    # print("ip_userId_dict: {}".format(ip_userId_dict))
    # print("res: {}".format(res))

    for text, ips in text_ip_dict.items():
        res[text][1] = len(ips)
        for ip in ips:
            if ip not in ip_userId_dict:
                continue
            user_id = ip_userId_dict[ip]
            if user_id in purchasedUserIds:
                res[text][0] += 1
    
    for text, v in res.items():
        purchased, total = v
        print("{} of {}  {}".format(purchased, total, text))

completed_purchase_user_ids = ["3123122444","234111110", "8321125440", "99911063"]

ad_clicks = [
 "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
 "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
 "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
 "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
 "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
 "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
  "2339985511,122.121.0.155",
 "234111110,122.121.0.1",
 "3123122444,92.130.6.145",
 "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
 "8321125440,82.1.106.8",
 "99911063,92.130.6.144"
]


AdsConversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips)
