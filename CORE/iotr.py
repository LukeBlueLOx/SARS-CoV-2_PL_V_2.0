from github import Github
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from datetime import timedelta
import csv
import yaml
import time

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
MAIN = config_vals['MAIN']
CORE = config_vals['CORE']

SERVICE_ACCOUNT_FILE = ''+str(CORE)+'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

with open(""+str(MAIN)+"config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
SPREADSHEET_ID1 = config_vals['ID1']
SPREADSHEET_ID2 = config_vals['ID3']
SPREADSHEET_ID3 = config_vals['ID4']
T4 = config_vals['T4']
formula1 = config_vals['formula1']
formula3 = config_vals['formula3']
save_path_extract4 = config_vals['save_path_extract4']
s = config_vals['g']
gg = Github(s)
sheet_id1 = '2025827439'
sheet_id2 = '2025827439'

t = config_vals['datetime']
sheet_id3 = t.strftime('%Y%m%d')
tt = t.strftime('%Y-%m-%d')
a = t
datetime = t
print(datetime)
b = datetime - timedelta(days=1)
c = datetime - timedelta(days=2)
d = datetime - timedelta(days=3)
e = datetime - timedelta(days=4)
f = datetime - timedelta(days=5)
g = datetime - timedelta(days=6)
h = datetime - timedelta(days=7)
i = datetime - timedelta(days=8)
j = datetime - timedelta(days=9)
k = datetime - timedelta(days=10)
l = datetime - timedelta(days=11)
m = datetime - timedelta(days=12)
n = datetime - timedelta(days=13)
o = datetime - timedelta(days=14)
p = datetime - timedelta(days=15)
r = datetime - timedelta(days=16)
s = datetime - timedelta(days=17)
t = datetime - timedelta(days=18)
u = datetime - timedelta(days=19)
v = datetime - timedelta(days=20)
w = datetime - timedelta(days=21)
x = datetime - timedelta(days=22)
y = datetime - timedelta(days=23)
z = datetime - timedelta(days=24)
aa = datetime - timedelta(days=25)
ab = datetime - timedelta(days=26)
ac = datetime - timedelta(days=27)
ad = datetime - timedelta(days=28)
ae = datetime - timedelta(days=29)
af = datetime - timedelta(days=30)
ag = datetime - timedelta(days=31)
ah = datetime - timedelta(days=32)
ai = datetime - timedelta(days=33)

RUN = [
    ["=({'"+str(ai)+"'!D2}+{'"+str(ah)+"'!D2}+{'"+str(ag)+"'!D2}+{'"+str(
     af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2})/7",
     "=({'"+str(ai)+"'!K2}+{'"+str(ah)+"'!K2}+{'"+str(ag)+"'!K2}+{'"+str(af)+
     "'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2})/7",
     "=({'"+str(ai)+"'!N2}+{'"+str(ah)+"'!N2}+{'"+str(ag)+"'!N2}+{'"+str(af)+
     "'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2})/7"],

    ["=({'"+str(ah)+"'!D2}+{'"+str(ag)+"'!D2}+{'"+str(af)+"'!D2}+{'"+str(
     ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2})/7",
     "=({'"+str(ah)+"'!K2}+{'"+str(ag)+"'!K2}+{'"+str(af)+"'!K2}+{'"+str(ae)+
     "'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2})/7",
     "=({'"+str(ah)+"'!N2}+{'"+str(ag)+"'!N2}+{'"+str(af)+"'!N2}+{'"+str(ae)+
     "'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2})/7"],

    ["=({'"+str(ag)+"'!D2}+{'"+str(af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(
     ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2})/7",
     "=({'"+str(ag)+"'!K2}+{'"+str(af)+"'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+
     "'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2})/7",
     "=({'"+str(ag)+"'!N2}+{'"+str(af)+"'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+
     "'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2})/7"],

    ["=({'"+str(af)+"'!D2}+{'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(
     ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2})/7",
     "=({'"+str(af)+"'!K2}+{'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+
     "'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2})/7",
     "=({'"+str(af)+"'!N2}+{'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+
     "'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2})/7"],

    ["=({'"+str(ae)+"'!D2}+{'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(
     ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2})/7",
     "=({'"+str(ae)+"'!K2}+{'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+
     "'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2})/7",
     "=({'"+str(ae)+"'!N2}+{'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+
     "'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2})/7"],

    ["=({'"+str(ad)+"'!D2}+{'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(
     aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2})/7",
     "=({'"+str(ad)+"'!K2}+{'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+
     "'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2})/7",
     "=({'"+str(ad)+"'!N2}+{'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+
     "'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2})/7"],

    ["=({'"+str(ac)+"'!D2}+{'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(
     z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2})/7",
     "=({'"+str(ac)+"'!K2}+{'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+
     "'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2})/7",
     "=({'"+str(ac)+"'!N2}+{'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+
     "'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2})/7"],

    ["=({'"+str(ab)+"'!D2}+{'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(
     y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2})/7",
     "=({'"+str(ab)+"'!K2}+{'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+
     "'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2})/7",
     "=({'"+str(ab)+"'!N2}+{'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+
     "'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2})/7"],

    ["=({'"+str(aa)+"'!D2}+{'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+
     "'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2})/7",
     "=({'"+str(aa)+"'!K2}+{'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+
     "'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2})/7",
     "=({'"+str(aa)+"'!N2}+{'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+
     "'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2})/7"],

    ["=({'"+str(z)+"'!D2}+{'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(
     w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2})/7",
     "=({'"+str(z)+"'!K2}+{'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+
     "'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2})/7",
     "=({'"+str(z)+"'!N2}+{'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+
     "'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2})/7"],

    ["=({'"+str(y)+"'!D2}+{'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(
     v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2})/7",
     "=({'"+str(y)+"'!K2}+{'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+
     "'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2})/7",
     "=({'"+str(y)+"'!N2}+{'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+
     "'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2})/7"],

    ["=({'"+str(x)+"'!D2}+{'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(
     u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2})/7",
     "=({'"+str(x)+"'!K2}+{'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+
     "'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2})/7",
     "=({'"+str(x)+"'!N2}+{'"+str(w)+"'!N2}+{'"+str(v)+
     "'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+
     "'!N2})/7"],

    ["=({'"+str(w)+"'!D2}+{'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(
     t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2})/7",
     "=({'"+str(w)+"'!K2}+{'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+
     "'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2})/7",
     "=({'"+str(w)+"'!N2}+{'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+
     "'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2})/7"],

    ["=({'"+str(v)+"'!D2}+{'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(
     s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2})/7",
     "=({'"+str(v)+"'!K2}+{'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+
     "'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2})/7",
     "=({'"+str(v)+"'!N2}+{'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+
     "'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2})/7"],

    ["=({'"+str(u)+"'!D2}+{'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(
     r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2})/7",
     "=({'"+str(u)+"'!K2}+{'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+
     "'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2})/7",
     "=({'"+str(u)+"'!N2}+{'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+
     "'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2})/7"],

    ["=({'"+str(t)+"'!D2}+{'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(
     p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2})/7",
     "=({'"+str(t)+"'!K2}+{'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+
     "'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2})/7",
     "=({'"+str(t)+"'!N2}+{'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+
     "'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2})/7"],

    ["=({'"+str(s)+"'!D2}+{'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(
     o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2})/7",
     "=({'"+str(s)+"'!K2}+{'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+
     "'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2})/7",
     "=({'"+str(s)+"'!N2}+{'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+
     "'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2})/7"],

    ["=({'"+str(r)+"'!D2}+{'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(
     n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(k)+"'!D2})/7",
     "=({'"+str(r)+"'!K2}+{'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+
     "'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+"'!K2})/7",
     "=({'"+str(r)+"'!N2}+{'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+
     "'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+"'!N2})/7"],

    ["=({'"+str(p)+"'!D2}+{'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(
     m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(k)+"'!D2}+{'"+str(j)+"'!D2})/7",
     "=({'"+str(p)+"'!K2}+{'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+
     "'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+"'!K2}+{'"+str(j)+"'!K2})/7",
     "=({'"+str(p)+"'!N2}+{'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+
     "'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+"'!N2}+{'"+str(j)+"'!N2})/7"],

    ["=({'"+str(o)+"'!D2}+{'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(
     l)+"'!D2}+{'"+str(k)+"'!D2}+{'"+str(j)+"'!D2}+{'"+str(i)+"'!D2})/7",
     "=({'"+str(o)+"'!K2}+{'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+
     "'!K2}+{'"+str(k)+"'!K2}+{'"+str(j)+"'!K2}+{'"+str(i)+"'!K2})/7",
     "=({'"+str(o)+"'!N2}+{'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+
     "'!N2}+{'"+str(k)+"'!N2}+{'"+str(j)+"'!N2}+{'"+str(i)+"'!N2})/7"],

    ["=({'"+str(n)+"'!D2}+{'"+str(m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(
     k)+"'!D2}+{'"+str(j)+"'!D2}+{'"+str(i)+"'!D2}+{'"+str(h)+"'!D2})/7",
     "=({'"+str(n)+"'!K2}+{'"+str(m)+"'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+
     "'!K2}+{'"+str(j)+"'!K2}+{'"+str(i)+"'!K2}+{'"+str(h)+"'!K2})/7",
     "=({'"+str(n)+"'!N2}+{'"+str(m)+"'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+
     "'!N2}+{'"+str(j)+"'!N2}+{'"+str(i)+"'!N2}+{'"+str(h)+"'!N2})/7"],

    ["=({'"+str(m)+"'!D2}+{'"+str(l)+"'!D2}+{'"+str(k)+"'!D2}+{'"+str(
     j)+"'!D2}+{'"+str(i)+"'!D2}+{'"+str(h)+"'!D2}+{'"+str(g)+"'!D2})/7",
     "=({'"+str(m)+"'!K2}+{'"+str(l)+"'!K2}+{'"+str(k)+"'!K2}+{'"+str(j)+
     "'!K2}+{'"+str(i)+"'!K2}+{'"+str(h)+"'!K2}+{'"+str(g)+"'!K2})/7",
     "=({'"+str(m)+"'!N2}+{'"+str(l)+"'!N2}+{'"+str(k)+"'!N2}+{'"+str(j)+
     "'!N2}+{'"+str(i)+"'!N2}+{'"+str(h)+"'!N2}+{'"+str(g)+"'!N2})/7"],

    ["=({'"+str(l)+"'!D2}+{'"+str(k)+"'!D2}+{'"+str(j)+"'!D2}+{'"+str(
     i)+"'!D2}+{'"+str(h)+"'!D2}+{'"+str(g)+"'!D2}+{'"+str(f)+"'!D2})/7",
     "=({'"+str(l)+"'!K2}+{'"+str(k)+"'!K2}+{'"+str(j)+"'!K2}+{'"+str(i)+
     "'!K2}+{'"+str(h)+"'!K2}+{'"+str(g)+"'!K2}+{'"+str(f)+"'!K2})/7",
     "=({'"+str(l)+"'!N2}+{'"+str(k)+"'!N2}+{'"+str(j)+"'!N2}+{'"+str(i)+
     "'!N2}+{'"+str(h)+"'!N2}+{'"+str(g)+"'!N2}+{'"+str(f)+"'!N2})/7"],

    ["=({'"+str(k)+"'!D2}+{'"+str(j)+"'!D2}+{'"+str(i)+"'!D2}+{'"+str(
     h)+"'!D2}+{'"+str(g)+"'!D2}+{'"+str(f)+"'!D2}+{'"+str(e)+"'!D2})/7",
     "=({'"+str(k)+"'!K2}+{'"+str(j)+"'!K2}+{'"+str(i)+"'!K2}+{'"+str(h)+
     "'!K2}+{'"+str(g)+"'!K2}+{'"+str(f)+"'!K2}+{'"+str(e)+"'!K2})/7",
     "=({'"+str(k)+"'!N2}+{'"+str(j)+"'!N2}+{'"+str(i)+"'!N2}+{'"+str(h)+
     "'!N2}+{'"+str(g)+"'!N2}+{'"+str(f)+"'!N2}+{'"+str(e)+"'!N2})/7"],

    ["=({'"+str(j)+"'!D2}+{'"+str(i)+"'!D2}+{'"+str(h)+"'!D2}+{'"+str(
     g)+"'!D2}+{'"+str(f)+"'!D2}+{'"+str(e)+"'!D2}+{'"+str(d)+"'!D2})/7",
     "=({'"+str(j)+"'!K2}+{'"+str(i)+"'!K2}+{'"+str(h)+"'!K2}+{'"+str(g)+
     "'!K2}+{'"+str(f)+"'!K2}+{'"+str(e)+"'!K2}+{'"+str(d)+"'!K2})/7",
     "=({'"+str(j)+"'!N2}+{'"+str(i)+"'!N2}+{'"+str(h)+"'!N2}+{'"+str(g)+
     "'!N2}+{'"+str(f)+"'!N2}+{'"+str(e)+"'!N2}+{'"+str(d)+"'!N2})/7"],

    ["=({'"+str(i)+"'!D2}+{'"+str(h)+"'!D2}+{'"+str(g)+"'!D2}+{'"+str(
     f)+"'!D2}+{'"+str(e)+"'!D2}+{'"+str(d)+"'!D2}+{'"+str(c)+"'!D2})/7",
     "=({'"+str(i)+"'!K2}+{'"+str(h)+"'!K2}+{'"+str(g)+"'!K2}+{'"+str(f)+
     "'!K2}+{'"+str(e)+"'!K2}+{'"+str(d)+"'!K2}+{'"+str(c)+"'!K2})/7",
     "=({'"+str(i)+"'!N2}+{'"+str(h)+"'!N2}+{'"+str(g)+"'!N2}+{'"+str(f)+
     "'!N2}+{'"+str(e)+"'!N2}+{'"+str(d)+"'!N2}+{'"+str(c)+"'!N2})/7"],

    ["=({'"+str(h)+"'!D2}+{'"+str(g)+"'!D2}+{'"+str(f)+"'!D2}+{'"+str(
     e)+"'!D2}+{'"+str(d)+"'!D2}+{'"+str(c)+"'!D2}+{'"+str(b)+"'!D2})/7",
     "=({'"+str(h)+"'!K2}+{'"+str(g)+"'!K2}+{'"+str(f)+"'!K2}+{'"+str(e)+
     "'!K2}+{'"+str(d)+"'!K2}+{'"+str(c)+"'!K2}+{'"+str(b)+"'!K2})/7",
     "=({'"+str(h)+"'!N2}+{'"+str(g)+"'!N2}+{'"+str(f)+"'!N2}+{'"+str(e)+
     "'!N2}+{'"+str(d)+"'!N2}+{'"+str(c)+"'!N2}+{'"+str(b)+"'!N2})/7"],

    ["=({'"+str(g)+"'!D2}+{'"+str(f)+"'!D2}+{'"+str(e)+"'!D2}+{'"+str(
     d)+"'!D2}+{'"+str(c)+"'!D2}+{'"+str(b)+"'!D2}+{'"+str(a)+"'!D2})/7",
     "=({'"+str(g)+"'!K2}+{'"+str(f)+"'!K2}+{'"+str(e)+"'!K2}+{'"+str(d)+
     "'!K2}+{'"+str(c)+"'!K2}+{'"+str(b)+"'!K2}+{'"+str(a)+"'!K2})/7",
     "=({'"+str(g)+"'!N2}+{'"+str(f)+"'!N2}+{'"+str(e)+"'!N2}+{'"+str(d)+
     "'!N2}+{'"+str(c)+"'!N2}+{'"+str(b)+"'!N2}+{'"+str(a)+"'!N2})/7"]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID1,
    range="IOTR!A1",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)

request = sheet.values().clear(
    spreadsheetId=SPREADSHEET_ID2,
    range="IOTR!A2:C29").execute()
print(request)

RUN = [
    ['' + formula1 + ',"IOTR!A1:C1")', "", "", str(ac)],
    ['' + formula1 + ',"IOTR!A2:C2")', "", "", str(ab)],
    ['' + formula1 + ',"IOTR!A3:C3")', "", "", str(aa)],
    ['' + formula1 + ',"IOTR!A4:C4")', "", "", str(z)],
    ['' + formula1 + ',"IOTR!A5:C5")', "", "", str(y)],
    ['' + formula1 + ',"IOTR!A6:C6")', "", "", str(x)],
    ['' + formula1 + ',"IOTR!A7:C7")', "", "", str(w)],
    ['' + formula1 + ',"IOTR!A8:C8")', "", "", str(v)],
    ['' + formula1 + ',"IOTR!A9:C9")', "", "", str(u)],
    ['' + formula1 + ',"IOTR!A10:C10")', "", "", str(t)],
    ['' + formula1 + ',"IOTR!A11:C11")', "", "", str(s)],
    ['' + formula1 + ',"IOTR!A12:C12")', "", "", str(r)],
    ['' + formula1 + ',"IOTR!A13:C13")', "", "", str(p)],
    ['' + formula1 + ',"IOTR!A14:C14")', "", "", str(o)],
    ['' + formula1 + ',"IOTR!A15:C15")', "", "", str(n)],
    ['' + formula1 + ',"IOTR!A16:C16")', "", "", str(m)],
    ['' + formula1 + ',"IOTR!A17:C17")', "", "", str(l)],
    ['' + formula1 + ',"IOTR!A18:C18")', "", "", str(k)],
    ['' + formula1 + ',"IOTR!A19:C19")', "", "", str(j)],
    ['' + formula1 + ',"IOTR!A20:C20")', "", "", str(i)],
    ['' + formula1 + ',"IOTR!A21:C21")', "", "", str(h)],
    ['' + formula1 + ',"IOTR!A22:C22")', "", "", str(g)],
    ['' + formula1 + ',"IOTR!A23:C23")', "", "", str(f)],
    ['' + formula1 + ',"IOTR!A24:C24")', "", "", str(e)],
    ['' + formula1 + ',"IOTR!A25:C25")', "", "", str(d)],
    ['' + formula1 + ',"IOTR!A26:C26")', "", "", str(c)],
    ['' + formula1 + ',"IOTR!A27:C27")', "", "", str(b)],
    ['' + formula1 + ',"IOTR!A28:C28")', "", "", str(a)]
]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID2,
    range="IOTR!A2",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
time.sleep(15)
print(request)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 1,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 3,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 1,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 3,
        },
        "pasteType": "Paste_Values",
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID2,
    body=RUN).execute()
print(request)

RUN = {'requests': [
    {'addSheet': {
        'properties': {
            "sheetId": sheet_id3 + str(1),
            "title": str(tt) + " - IOTR",
            "gridProperties": {
                "columnCount": 13,
                "rowCount": 29
            }
        },
    }},
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID3,
    body=RUN).execute()
print(request)

RUN = [[str(formula3)]]
request = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID3,
    range=""+str(tt)+" - IOTR",
    valueInputOption="USER_ENTERED",
    body={"values": RUN}).execute()
print(request)
time.sleep(7)

RUN = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id3 + str(1),
            'startRowIndex': 0,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 13,
        },
        "destination": {
            'sheetId': sheet_id3 + str(1),
            'startRowIndex': 0,
            'endRowIndex': 29,
            'startColumnIndex': 0,
            'endColumnIndex': 13,
        },
        "pasteType": "Paste_Values"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID3, body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheet_id3 + str(1),
            "startRowIndex": 1,
            "endRowIndex": 29,
            "startColumnIndex": 3,
            "endColumnIndex": 4
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID3,
    body=RUN).execute()
print(request)

RUN = {"requests": [
    {"repeatCell": {
        "range": {
            "sheetId": sheet_id3 + str(1),
            "startRowIndex": 1,
            "endRowIndex": 29,
            "startColumnIndex": 10,
            "endColumnIndex": 11
        },
        "cell": {
            "userEnteredFormat": {
                "numberFormat": {
                    "type": "DATE_TIME",
                    "pattern": "yyyy-mm-dd"
                }
            }
        },
        "fields": "userEnteredFormat.numberFormat"
    }}
]}
request = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID3,
    body=RUN).execute()
print(request)

client = gspread.authorize(creds)
spreadsheet = client.open_by_key(SPREADSHEET_ID3)
worksheetName = ""+str(tt)+" - IOTR"
worksheet = spreadsheet.worksheet(worksheetName)
filename = save_path_extract4 + sheet_id3 + "_IOTR" + ".csv"
with open(filename, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(worksheet.get_all_values())

repo = gg.get_user().get_repo("SARS-CoV-2_PL_V_2.0")

file_path = save_path_extract4 + str(sheet_id3) + "_IOTR" + ".csv"
with open(file_path, 'r') as file:
    content = file.read()
repo.create_file(
    file_path,
    "Save: DATA/IOTR/" + str(sheet_id3) + "_IOTR" + ".csv",
    content)
