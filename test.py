#!/usr/bin/env python3
# encoding: utf-8

a = [1,2,3,4]


if __name__ == '__main__':
    User = {
        "Uin": 62579400,
        "UserName": "@e8b93eb62c8984acb2944227957247bc",
        "NickName": "æ°",
        "HeadImgUrl": "/cgi-bin/mmwebwx-bin/webwxgeticon?seq=128234112&username=@e8b93eb62c8984acb2944227957247bc&skey=@crypt_9143f58_fcced891c4c0d1b3f40e68385f222d24",
        "RemarkName": "",
        "PYInitial": "",
        "PYQuanPin": "",
        "RemarkPYInitial": "",
        "RemarkPYQuanPin": "",
        "HideInputBarFlag": 0,
        "StarFriend": 0,
        "Sex": 1,
        "Signature": "å¾®ä¿¡1",
        "AppAccountFlag": 0,
        "VerifyFlag": 0,
        "ContactFlag": 0,
        "WebWxPluginSwitch": 0,
        "HeadImgFlag": 1,
        "SnsFlag": 17
    }
    for a in User.keys():
        if isinstance(User[a], str):
            print("private String " + a + ";")
        elif isinstance(User[a], int):
            print("private Integer " + a + ";")
