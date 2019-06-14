LOMADEE_SUCESS_REQ = {
    "totallooseoffers": 0,
    "details": {
        "date": {
            "valid": True,
            "eonandyear": {
                "lowestsetbit": 0
            },
            "hour": 17,
            "month": 6,
            "year": 2019,
            "timezone": -180,
            "millisecond": 174,
            "xmlschematype": {
                "prefix": "",
                "localpart": "dateTime",
                "namespaceuri": "http://www.w3.org/2001/XMLSchema"
            },
            "day": 13,
            "minute": 51,
            "second": 1
        },
        "code": 0,
        "applicationversion": "v1",
        "applicationid": "3651516a44624e526551453d",
        "elapsedtime": 42,
        "message": "success",
        "status": "success"
    },
    "lomadeelinks": [
        {
            "lomadeelink": {
                "originallink": "http://americanas.com.br",
                "code": 0,
                "id": 1,
                "redirectlink": "https://iuuuupiiii.com"
            }
        }
    ],
    "page": 1,
    "totalpages": 1,
    "totalresultsreturned": 1,
    "totalresultsavailable": 1
}

LOMADEE_INVALID_URL_REQ = {
    "totallooseoffers": 0,
    "details": {
        "date": {
            "valid": True,
            "eonandyear": {
                "lowestsetbit": 0
            },
            "hour": 0,
            "month": 6,
            "year": 2019,
            "timezone": -180,
            "millisecond": 107,
            "xmlschematype": {
                "prefix": "",
                "localpart": "dateTime",
                "namespaceuri": "http://www.w3.org/2001/XMLSchema"
            },
            "day": 14,
            "minute": 12,
            "second": 36
        },
        "code": 0,
        "applicationversion": "v1",
        "elapsedtime": 31,
        "applicationid": "3651516a44624e526551453d",
        "message": "success",
        "status": "success"
    },
    "lomadeelinks": [
        {
            "lomadeelink": {
                "originallink": "https://www.saraiva.com.br",
                "code": 1,
                "id": 1,
                "message": "Link is invalid"
            }
        }
    ],
    "page": 1,
    "totalpages": 1,
    "totalresultsreturned": 1,
    "totalresultsavailable": 1
}

LOMADEE_INVALID_SOURCE_ID = {
    "totallooseoffers": 0,
    "details": {
        "date": {
            "valid": True,
            "eonandyear": {
                "lowestsetbit": 0
            },
            "hour": 0,
            "month": 6,
            "year": 2019,
            "timezone": -180,
            "millisecond": 949,
            "xmlschematype": {
                "prefix": "",
                "localpart": "dateTime",
                "namespaceuri": "http://www.w3.org/2001/XMLSchema"
            },
            "day": 14,
            "minute": 29,
            "second": 36
        },
        "code": 501,
        "applicationversion": "v1",
        "elapsedtime": 1,
        "applicationid": "3651516a44624e526551453d",
        "message": "SourceId is invalid",
        "status": "fail"
    },
    "totalresultsreturned": 0,
    "totalresultsavailable": 0
}

AFILIO_SUCESS = """<WSdeeplink><link><a href="http://yahoo!!!!" target="_blank">deeplink</a>
<br>deeplink<br></link></WSdeeplink>"""

ZANOX_SUCESS = {"error": 1, "message": "Success", "url": "http://yahoo!!!!"}

ZANOX_ERROR = {"error": 5, "message": "You have not applied for this program", "url": ""}
