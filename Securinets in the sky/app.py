#!/usr /bin/python

from flask import Flask,request,render_template
import sys
import base64
from Crypto.Cipher import AES

app=Flask(__name__)
class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

'''
def getkey(key):
     n=18819881292060796383869723946165043980716356337941738270076335642298885971523466548531906060650474304531738801130339671619969232120573403187955065699622130516>
     e=65537
     return pow(int(key.encode('hex'),16),e,n)
'''
def read_flag():
    with open('flag','r') as f:
        res=f.read()
        f.close()
    return res
@app.route('/',methods=['GET','POST'])
def index():
    key = 'k4hl@&Sem4hKEEEY'
    #enc_key = getkey(key)
    cipher = AESCipher(key)
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        if cipher.encrypt(request.form['username'])=='o3qxyQUosgVEwnLz3hCCdhuD3dIlbPIC3yTZHoQXQxc=' and cipher.encrypt(request.form['password'])== 'EhQaDW0bN+abDTaC3Fmp7Q==' :
            return render_template('index.html',msg=read_flag())
        else :
            return render_template('index.html', msg='Try Again')

if __name__=='__main__':
    app.run(debug=True)