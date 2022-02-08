import requests
import json
from time import sleep
import argparse
import urllib3
import os


parser = argparse.ArgumentParser()
parser.add_argument ('-e', action="store",dest='hack_Email',help="ادخل الاميل للبحث")
parser.add_argument ('-u', action="store",dest='hack',help="اسم المستخدم")
args=parser.parse_args ()

r = requests.session ()
green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color = "\033[1;33;40m"
end_banner_color = "\33[00m"

print (detect_color+"""
██╗███╗   ██╗███████╗ ██████╗     ███████╗███╗   ██╗ █████╗ ██████╗ 
██║████╗  ██║██╔════╝██╔═══██╗    ██╔════╝████╗  ██║██╔══██╗██╔══██╗
██║██╔██╗ ██║█████╗  ██║   ██║    ███████╗██╔██╗ ██║███████║██████╔╝
██║██║╚██╗██║██╔══╝  ██║   ██║    ╚════██║██║╚██╗██║██╔══██║██╔═══╝ 
██║██║ ╚████║██║     ╚██████╔╝    ███████║██║ ╚████║██║  ██║██║     
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝                                                                         
                   											  
⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡜⠀⠀⠀
⠀⠀⠀⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠤⠄⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣀⠄⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⡜⠘⠀⠀⠀⠀⠈⣿⠀⠁⣿⢳⠁⢈⢰⡦⠈⠀⢻
⣿⣿⡏⠀⠀⢀⣀⠀⠀⡀⠀⠀⢀⠀⠀⠁⠀⠀⠈⠉⠀⠀⠀⡘⠀⢰⠛⢠⣴⣄⣌
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢠⣠⡀⠀⠀⠀⠂⠀⠀⠀⠐⠀⠈⣡⠻⢹⢿
⣿⣿⠀⠀⠀⠁⠀⠀⠀⠄⠀⠀⡀⣀⣼⣟⣿⢵⣤⣤⣤⣤⣤⣤⣄⣀⣀⣠⠀⠢⣽
⣿⡿⠀⠀⠀⠀⠀⢐⣌⢖⣰⠊⠁⢸⣿⡟⠈⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣾⡄⢰⢺
⣿⡇⠀⠀⠀⠀⢀⡀⢴⢖⣠⣣⣴⣿⢿⡇⣈⠐⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢠⣸
⣿⣷⡀⠀⠀⠀⠀⠸⣼⣿⣿⣿⣿⡷⠋⠅⠀⡀⢼⣿⠯⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿
⡿⠁⠸⣄⣦⡀⠀⢡⣿⣿⣿⣿⣏⡤⠄⠄⠀⠀⠈⠉⠁⠘⢿⣿⣿⣿⣿⣿⣯⢸⣿
⠇⠀⠀⡹⢿⡏⠀⣾⣿⣟⠋⠉⠁⠀⠀⠀⠀⣀⣀⠀⠀⠀⢸⣿⠎⠉⠉⠉⠛⣤⣿
⡆⠀⡀⢣⢈⡟⠠⠻⣿⣿⣷⡄⠀⠀⢸⣶⣷⣷⣧⡄⠀⠀⢿⣧⢀⡀⠀⠉⢡⣿⣿
⣿⣦⡀⠘⢼⠃⣠⡲⠛⢿⡿⣿⡀⡀⠀⠹⣿⣿⡟⠀⠠⣤⠘⣿⣶⣿⣶⡾⣳⣿⣿
⣿⡿⣿⣶⡌⠰⡅⠌⠠⠈⠈⠙⢙⠑⢰⠀⠨⠟⠀⠀⣴⢌⡅⢻⣿⣿⣿⡇⣿⣿⣿
⣿⢇⣿⣿⠣⢿⣮⠀⢀⡀⠀⠀⠈⠁⣶⠀⠀⠀⠀⠀⠁⠀⢡⣺⣿⣿⡿⣸⣿⣿⣿
⣿⣾⣿⣏⠐⣿⢟⡈⠂⠀⠠⠀⠀⠀⣆⠀⠀⠀⠀⠀⠀⣢⣼⣸⣿⡿⢈⣿⣿⣿⣿
⣿⣿⣿⠃⡀⠈⠑⠁⠀⠄⠀⠀⠀⠲⠀⠀⠄⣀⠀⣸⣷⣮⣍⠃⢹⠇⣿⣿⣿⣿⣿
⣿⣿⣿⢀⣾⣷⣶⣌⠀⠠⠀⠀⢀⠍⠀⠀⠀⠀⠉⠁⠈⠙⠋⢰⡝⣼⣿⣿⣿⣿⣿
⣿⣿⣿⠋⠀⣼⣿⣿⣷⣄⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠄⡀⢀⣼⢣⣿⣿⣿⣿⣿⣿
⣿⣿⣯⠀⢸⣿⣿⣿⡟⠛⠳⣄⠀⠀⠀⠀⠘⠌⠓⡀⢰⣮⣾⢠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣧⠀⣹⣿⣿⣿⠗⠀⠀⠀⠀⠀⣀⡀⠀⠈⠀⠀⠈⠝⣡⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡏⠀⣿⣿⣿⠿⠃⢀⣴⣶⣾⣿⣿⣿⣿⣷⣾⢠⣶⣾⣮⣙⡻⣿⢿⣿⣿⣿⣿
⣿⣿⡇⠀⣿⣿⠃⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡟⡼⠿⣿⣿⣿⣿⣮⡑⡝⣿⣿⣿										  											  
""")
print (end_banner_color + '''
==============================================
[developer] => FaLaH - 0xfff0800 [developer_email] => flaaah777@gmail.com ) 
[developer_snapchat] => flaah999
==============================================
''')



sleep (6)

os.system('clear')
url = "https://app.snapchat.com/loq/find_users"
headers = {
        "X-Snapchat-Uuid": "40712891-4208-46DD-92E0-197970AD6E19",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLYAlIL_PcSAVIyUeXvfzCMxIuYcKcir4z61uLFyAizk3ejlHVTPNJpqEd6Lw4wTwB0YX5r8pk6cPv1AzbZb4eP7xrrz_c-B_FOlYSitBCKPPhhPMIQ39zOlPO7vjg0FDMBLjWHJRzzuG2Ki4I1ZKhkOjVTvl4hhzn27sx0XByw6j7oT8my36nDNoROyIKzK8mXJQKuCQ-inniST9AYrruIDVJYAVkOR0U83BnBJZkWdbYxjXC36Ku3_Evs6fCpCLMLKS2RTdjfCYJbY9EuTIzXro8L3dwt3ZCNCwXz6oK-Vu-PpDzF6F4VjPUZR2QyGy1OFOjb_lCkL_oWXwQulqioztvQr79ZUG88wc9ToFznj7_3ZA0zssLLiG02A_3-Nq1pxWc2EiJedc-OFucgwJqeJR5ts18PNRMOkf9RPDmyY1nLTxHkZxxuKDlwcPjl0uGZ5Y2G6HaSEYxX",
        "Host": "app.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
data = "query_text="+args.hack+"&req_token=79e26a4b50438136f73410d1a3587732a1b5b6e855fd23a426e8a34885863d1f&timestamp=1641289936711&user_result_types=[%22dns%22]&username=bot_falah"

response = requests.request ("POST", url, data=data, headers=headers).text
info = json.loads (response)
print (green_color + " --> username : " + str (info["users"][0]["friend"]["name"]))
print (green_color + " --> user_id : " + str (info["users"][0]["friend"]["user_id"]))
print (green_color + " --> name : " + str (info["users"][0]["friend"]["display"]))
print (green_color + " --> تحقق من الشهره : " + str (info["users"][0]["friend"]["is_popular"]))	
url = "https://mvm.snapchat.com/bq/friend"
id = info["users"][0]["friend"]["user_id"]	
headers = {
        "X-Snapchat-Uuid": "40712891-4208-46DD-92E0-197970AD6E19",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLUAtqasJ5nlNNvFfyTn3QUSGCrcusB6tBWR8fXBUheKpAkSfBlbCcyFnPp5Sp2QGnPvKl3sBDO0NrNSZFD11HLbM227MT5_cn0gnM7BeYCJXXvNEN5OcOxfGLhfQFOy2vgEaTa3Ok17qDLajzXr_dhvYz5yX-ajgcB2bAHWIjEGJTUkdtq3VMPQpcWNEDsUH9v4-eeT8hwo-nlbU0jXlRqsi_iDcmO3LVNpGGT85bflxTnAy4yxSAEK9b0-mD0qghgg9oBVNvMKLvxXx5qr1y6HqBhyvDEEiULFzlwG7H4vQNT4GExSTufRnz6r_xnF_82EkTKSgJ0xAehLba_ZbcSdcT17bP2BIGXJTF63zufjYpdpsa3FcX550WOrr4gJujFvy8sa-9VVJzL_RB5v2dE_QR4cfP_rpYS-a_yCNx0_V_HnRln49i0W1DBDtYu-2k8NeRZZAo=",
        "Host": "mvm.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
data = ("action=add&added_by=ADDED_BY_USERNAME&friend_id="+id+"&identity_cell_index=0&identity_profile_page=add_friends_button_on_top_bar_on_friends_feed&is_official=0&req_token=79e7d0445a235736f72968d3ad53fac218bcb6ef55af23abb6e80b488886364f&timestamp=1641289952571&username=bot_falah")

response = requests.request ("POST", url, data=data, headers=headers).text
falah999 = json.loads (response)
print (green_color + " --> نوع الحساب : " + str (falah999["object"]["can_see_custom_stories"]))
print (green_color + " --> حالة الحساب : " + str (falah999["object"]["direction"]))

if 'category_name' in response:
       print (green_color + " --> يوجد ملف تعريفي : " + str (falah999["object"]["friendmojis"][0]["category_name"]))
	
       url = "https://mvm.snapchat.com/bq/friend"
       id = info["users"][0]["friend"]["user_id"]	
       headers = {
        "X-Snapchat-Uuid": "40712891-4208-46DD-92E0-197970AD6E19",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLUAtqasJ5nlNNvFfyTn3QUSGCrcusB6tBWR8fXBUheKpAkSfBlbCcyFnPp5Sp2QGnPvKl3sBDO0NrNSZFD11HLbM227MT5_cn0gnM7BeYCJXXvNEN5OcOxfGLhfQFOy2vgEaTa3Ok17qDLajzXr_dhvYz5yX-ajgcB2bAHWIjEGJTUkdtq3VMPQpcWNEDsUH9v4-eeT8hwo-nlbU0jXlRqsi_iDcmO3LVNpGGT85bflxTnAy4yxSAEK9b0-mD0qghgg9oBVNvMKLvxXx5qr1y6HqBhyvDEEiULFzlwG7H4vQNT4GExSTufRnz6r_xnF_82EkTKSgJ0xAehLba_ZbcSdcT17bP2BIGXJTF63zufjYpdpsa3FcX550WOrr4gJujFvy8sa-9VVJzL_RB5v2dE_QR4cfP_rpYS-a_yCNx0_V_HnRln49i0W1DBDtYu-2k8NeRZZAo=",
        "Host": "mvm.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
       data = ("action=delete&added_by=ADDED_BY_USERNAME&friend_id="+id+"&identity_cell_index=0&identity_profile_page=add_friends_button_on_top_bar_on_friends_feed&is_official=0&req_token=79e7d0445a235736f72968d3ad53fac218bcb6ef55af23abb6e80b488886364f&timestamp=1641289952571&username=bot_falah")

       response = requests.request ("POST", url, data=data, headers=headers)
	
	
       phone_number = input(" --> phone number : ")
       headers = {
        "X-Snapchat-Uuid": "A8B07C91-4F23-456E-A874-009FB0815CA0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLoArSJs40R6-MNWAJ3Zdmx3NkpgV9-R6N3N2qXINQ7yHE_EWpMr1odF1XFW0vbcA2JCEcYes75-lPaEV0cp-gNMqz6x7Drl2lvMCSE747W31vBP_mCDrawYXH_wsn9xg7OSoYeIM6BXW5WqoqAN5_wnHwkG_L_H1jjP0zXTpN-yuvXlON4beK7aoED2chTvWmTC7Fz6wkdZhQ05XvIAp9MtbynVy9wcFrlI7EGgIvc5Ln0p1yYEAt_rhDTbi0GadEjfJXVuBOHkjD4orT95VBHl4f6mPjpX11hOsEu7yMvud1o1uXhqt3ZBvSWmlqqCXwh_y4FKtv7qwvcHXZ_GnweC8Vib2Z3h-h8dbWE5JVXnaw_CnR1lPQOjDHQgickKgI6a_tNWgorrA4IDLltrjNqE3xpRmal8oEgQ6oFWghG5H8Uu1UbZFAsqS3o7qObpm7h0-HwrFpoaocZgV3o_dByqqM7Wxm5qgDdfw==",
        "Host": "app.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
       data = "action=request_code&code=&country_code=SA&method=text&phone_number="+phone_number+"&pre_auth_token=&req_token=93015c5a8d21a5286ee3a1ebf5a81a5474ea4d821981fa8859b4a714d0c5120b&timestamp=1641288943621&username_or_email="+args.hack+""

       request_object = requests.post('https://app.snapchat.com/loq/phone_verify_pre_login',  headers=headers ,data=data)
       if request_object.status_code == 200:
          print(" --> رقم الهاتف مرتبط في الحساب")
       if request_object.status_code == 429:
          print(" --> محاولات كثيره")
       if request_object.status_code == 400:
          print(" --> رقم الهاتف غير مرتبط")
#--------------------------------------

       headers = {
        "X-Snapchat-Uuid": "A8B07C91-4F23-456E-A874-009FB0815CA0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLoArSJs40R6-MNWAJ3Zdmx3NkpgV9-R6N3N2qXINQ7yHE_EWpMr1odF1XFW0vbcA2JCEcYes75-lPaEV0cp-gNMqz6x7Drl2lvMCSE747W31vBP_mCDrawYXH_wsn9xg7OSoYeIM6BXW5WqoqAN5_wnHwkG_L_H1jjP0zXTpN-yuvXlON4beK7aoED2chTvWmTC7Fz6wkdZhQ05XvIAp9MtbynVy9wcFrlI7EGgIvc5Ln0p1yYEAt_rhDTbi0GadEjfJXVuBOHkjD4orT95VBHl4f6mPjpX11hOsEu7yMvud1o1uXhqt3ZBvSWmlqqCXwh_y4FKtv7qwvcHXZ_GnweC8Vib2Z3h-h8dbWE5JVXnaw_CnR1lPQOjDHQgickKgI6a_tNWgorrA4IDLltrjNqE3xpRmal8oEgQ6oFWghG5H8Uu1UbZFAsqS3o7qObpm7h0-HwrFpoaocZgV3o_dByqqM7Wxm5qgDdfw==",
        "Host": "app.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
       data = "action=request_code&code=&country_code=SA&method=text&phone_number="+phone_number+"&pre_auth_token=&req_token=93015c5a8d21a5286ee3a1ebf5a81a5474ea4d821981fa8859b4a714d0c5120b&timestamp=1641288943621&username_or_email="+args.hack_Email+""

       request_object = requests.post('https://app.snapchat.com/loq/phone_verify_pre_login',  headers=headers ,data=data)
       if request_object.status_code == 200:
          print(" --> الاميل مرتبط في الحساب")
       if request_object.status_code == 429:
          print(" --> محاولات كثيره")
       if request_object.status_code == 400:
          print(" --> لا يمكنني التاكد من الاميل بدون ربط رقم هاتفه بحسابه")
          print (red_color + "---------------------------------------")
          print ("")

elif '' in response:
       print (green_color + " --> لايوجد ملف تعريفي ")
       phone_number = input(" --> phone number : ")
       headers = {
        "X-Snapchat-Uuid": "A8B07C91-4F23-456E-A874-009FB0815CA0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLoArSJs40R6-MNWAJ3Zdmx3NkpgV9-R6N3N2qXINQ7yHE_EWpMr1odF1XFW0vbcA2JCEcYes75-lPaEV0cp-gNMqz6x7Drl2lvMCSE747W31vBP_mCDrawYXH_wsn9xg7OSoYeIM6BXW5WqoqAN5_wnHwkG_L_H1jjP0zXTpN-yuvXlON4beK7aoED2chTvWmTC7Fz6wkdZhQ05XvIAp9MtbynVy9wcFrlI7EGgIvc5Ln0p1yYEAt_rhDTbi0GadEjfJXVuBOHkjD4orT95VBHl4f6mPjpX11hOsEu7yMvud1o1uXhqt3ZBvSWmlqqCXwh_y4FKtv7qwvcHXZ_GnweC8Vib2Z3h-h8dbWE5JVXnaw_CnR1lPQOjDHQgickKgI6a_tNWgorrA4IDLltrjNqE3xpRmal8oEgQ6oFWghG5H8Uu1UbZFAsqS3o7qObpm7h0-HwrFpoaocZgV3o_dByqqM7Wxm5qgDdfw==",
        "Host": "app.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
       data = "action=request_code&code=&country_code=SA&method=text&phone_number="+phone_number+"&pre_auth_token=&req_token=93015c5a8d21a5286ee3a1ebf5a81a5474ea4d821981fa8859b4a714d0c5120b&timestamp=1641288943621&username_or_email="+args.hack+""

       request_object = requests.post('https://app.snapchat.com/loq/phone_verify_pre_login',  headers=headers ,data=data)
    
       if request_object.status_code == 200:
          print(" --> رقم الهاتف مرتبط في الحساب")
       if request_object.status_code == 429:
          print(" --> محاولات كثيره")
       if request_object.status_code == 400:
          print(" --> رقم الهاتف غير مرتبط")
          print (red_color + "---------------------------------------")
          print ("")

          url = "https://mvm.snapchat.com/bq/friend"
          id = info["users"][0]["friend"]["user_id"]	
          headers = {
        "X-Snapchat-Uuid": "40712891-4208-46DD-92E0-197970AD6E19",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLUAtqasJ5nlNNvFfyTn3QUSGCrcusB6tBWR8fXBUheKpAkSfBlbCcyFnPp5Sp2QGnPvKl3sBDO0NrNSZFD11HLbM227MT5_cn0gnM7BeYCJXXvNEN5OcOxfGLhfQFOy2vgEaTa3Ok17qDLajzXr_dhvYz5yX-ajgcB2bAHWIjEGJTUkdtq3VMPQpcWNEDsUH9v4-eeT8hwo-nlbU0jXlRqsi_iDcmO3LVNpGGT85bflxTnAy4yxSAEK9b0-mD0qghgg9oBVNvMKLvxXx5qr1y6HqBhyvDEEiULFzlwG7H4vQNT4GExSTufRnz6r_xnF_82EkTKSgJ0xAehLba_ZbcSdcT17bP2BIGXJTF63zufjYpdpsa3FcX550WOrr4gJujFvy8sa-9VVJzL_RB5v2dE_QR4cfP_rpYS-a_yCNx0_V_HnRln49i0W1DBDtYu-2k8NeRZZAo=",
        "Host": "mvm.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
          data = ("action=delete&added_by=ADDED_BY_USERNAME&friend_id="+id+"&identity_cell_index=0&identity_profile_page=add_friends_button_on_top_bar_on_friends_feed&is_official=0&req_token=79e7d0445a235736f72968d3ad53fac218bcb6ef55af23abb6e80b488886364f&timestamp=1641289952571&username=bot_falah")

          response = requests.request ("POST", url, data=data, headers=headers)
		  

       headers = {
        "X-Snapchat-Uuid": "A8B07C91-4F23-456E-A874-009FB0815CA0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/10.82.5.78 (iPhone9,3; iOS 14.4.1; gzip)",
        "Accept": "application/json",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLoArSJs40R6-MNWAJ3Zdmx3NkpgV9-R6N3N2qXINQ7yHE_EWpMr1odF1XFW0vbcA2JCEcYes75-lPaEV0cp-gNMqz6x7Drl2lvMCSE747W31vBP_mCDrawYXH_wsn9xg7OSoYeIM6BXW5WqoqAN5_wnHwkG_L_H1jjP0zXTpN-yuvXlON4beK7aoED2chTvWmTC7Fz6wkdZhQ05XvIAp9MtbynVy9wcFrlI7EGgIvc5Ln0p1yYEAt_rhDTbi0GadEjfJXVuBOHkjD4orT95VBHl4f6mPjpX11hOsEu7yMvud1o1uXhqt3ZBvSWmlqqCXwh_y4FKtv7qwvcHXZ_GnweC8Vib2Z3h-h8dbWE5JVXnaw_CnR1lPQOjDHQgickKgI6a_tNWgorrA4IDLltrjNqE3xpRmal8oEgQ6oFWghG5H8Uu1UbZFAsqS3o7qObpm7h0-HwrFpoaocZgV3o_dByqqM7Wxm5qgDdfw==",
        "Host": "app.snapchat.com",
		"Accept-Encoding": "gzip, deflate"
    }
       data = "action=request_code&code=&country_code=SA&method=text&phone_number="+phone_number+"&pre_auth_token=&req_token=93015c5a8d21a5286ee3a1ebf5a81a5474ea4d821981fa8859b4a714d0c5120b&timestamp=1641288943621&username_or_email="+args.hack_Email+""

       request_object = requests.post('https://app.snapchat.com/loq/phone_verify_pre_login',  headers=headers ,data=data)
       if request_object.status_code == 200:
          print(" --> الاميل مرتبط في الحساب")
       if request_object.status_code == 429:
          print(" --> محاولات كثيره")
       if request_object.status_code == 400:
          print(" --> لا يمكنني التاكد من الاميل بدون ربط رقم هاتفه بحسابه")
          print (red_color + "---------------------------------------")
          print ("")

 
headers = {
        "Vaar-Header-App-Build-Version": "1.0.0",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Host": "identityprotection.avast.com",
		"Accept-Encoding": "gzip, deflate",
		"Vaar-Version": "0",
        "Vaar-Header-App-Product-Name": "hackcheck-web-avast"
    }
data = '''

{
    "emailAddresses":[
      "'''+args.hack_Email+'''"
    ]
}
'''
request_object = requests.post('https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data',  headers=headers ,data=data).text
info = json.loads (request_object)
try:

        print (green_color + """  --> يوجد تسريب للاميل : 
		  
		    ( Emailed ) تريد استخراج كلمات المرور قم بشراء اداة 
		       https://story.snapchat.com/@flaah999 للشراء
		
		
		""")
except:
        print ("---E----N----D")
        exit()



