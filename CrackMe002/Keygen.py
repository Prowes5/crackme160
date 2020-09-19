# -*- coding: utf-8 -*-

username = raw_input("Please input username:")

length = len(username)
serial_number = length*0x17CFB+ord(username[0])

print "Serial number is AKA-"+str(serial_number) 