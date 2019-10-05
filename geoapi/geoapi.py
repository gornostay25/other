import json,requests,csv,io,base64,math

def genmarker(c):
    for x in range(0,len(c)):
    #print(ist(float(b[x][0]),float(b[x][1]),float(b[x+1][0]),float(b[x+1][1]),float(b[x][2]),float(b[x+1][2])))
        print('addMarker({lat: '+c[x][0]+',lng: '+c[x][1]+'},'+c[x][2]+');')


def ist(a,b):
    x1,x2,y1,y2,r1,r2 = float(a[0]),float(b[0]),float(a[1]),float(b[1]),float(a[2]),float(b[2])
    l = distance(x1,y1,x2,y2)
    if l > r1+r2:
        return False
    elif l == r1+r2:
        return True
    elif l < r1+r2:
        return True

def peretun(b):
    for n in range(0,len(b)):    
        for x in range(0,len(b)):
            if ist(b[n],b[x]):
                b[n].append(x)
    m = 0
    c = []
    for y in range(0,len(b)):
        if len(b[y]) > m:
            m = len(b[y])
    for g in range(0,len(b)):
        if len(b[g]) == m:
            c.append(b[g][:3])
    return c


def frombase(bs):
    with io.BytesIO(base64.b64decode(bs.encode())) as f:
        b =[]
        for x in f.readlines():
            b.append(search(str(x.strip().decode()).split()))
    return b

def distance(llat1,llong1,llat2,llong2):
    rad = 6372795
    lat1 = llat1*math.pi/180.
    lat2 = llat2*math.pi/180.
    long1 = llong1*math.pi/180.
    long2 = llong2*math.pi/180.
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = long2 - long1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)
    y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
    x = sl1*sl2+cl1*cl2*cdelta
    ad = math.atan2(y,x)
    dist = ad*rad
    return dist

def infile(y):
    t = y[0]
    mcc = y[1]
    mc = y[2]
    tac = y[3]
    cid = y[4]
    with open('gsmdb.csv','r') as f:
        a = csv.DictReader(f)
        for x in a:
            if x['radio'] == str(t):
                if x['mcc'] == str(mcc):
                    if x['mnc'] == str(mc):
                        if x['tac'] == str(tac):
                            if x['cid'] == str(cid):
                                return [x['lat'],x['lon'],x['range']]

url = "https://eu1.unwiredlabs.com/v2/process.php"
#response = requests.request("POST", url, data=payload)
#j = json.loads(response.text)
#print(str(j['lat'])+str(j['lon'])+str(j['accuracy']+20))
def search(y):
    if not infile(y[:]):
        payload = '{ "token": "ca9076868b817a", "radio": "'+y[0]+'", "mcc": '+y[1]+', "mnc": '+y[2]+', "cells": [{ "lac": '+y[3]+', "cid": '+y[4]+' }], "address": 0 }'
        response = requests.request("POST", url, data=payload)
        j = json.loads(response.text)
        with open('gsmdb.csv','a') as n:
            b = csv.DictWriter(n,['radio','mcc','mnc','tac','cid','lat','lon','range'])
            b.writerow({'radio':y[0],'mcc':y[1],'mnc':y[2],'tac':y[3],'cid':y[4],'lat':str(j['lat']),'lon':str(j['lon']),'range':str(j['accuracy']+20)})
        return(infile(y[:]))
    else:
        return(infile(y[:]))
