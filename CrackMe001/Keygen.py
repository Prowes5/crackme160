# -*- coding: utf-8 -*-

print 'CrackMe001 Keygen'
username = raw_input('Input your name:')

if len(username) < 4:
    print 'Your Name length must be bigger than 4'
    exit(0)
Serial_Num = ord(username[0])*0x29*2
Serial = 'CW-'+str(Serial_Num)+'-CRACKED'

print 'Your Serial: '+Serial