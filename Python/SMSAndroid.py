#!/usr/bin/python
import os
import sys
import socket
import time
import Utils
import sms
import SMSFuzzData
import random
from datetime import datetime
import fuzzutils
def udhrandfuzz(msisdn, smsc, ts, num):
	s = sms.SMSToMS()
	s._msisdn = msisdn
	s._msisdn_type = 0x91
	s._smsc = smsc
	s._smsc_type = 0x91
	s._tppid = 0x00
	s._tpdcs = random.randrange(0, 1)
	if s._tpdcs == 1:
 		s._tpdcs = 0x04
	s._timestamp = ts
	s._deliver = 0x04
	s.deliver_raw2flags()
	s._deliver_udhi = 1
	s.deliver_flags2raw()
	s._msg = ""
	s._msg_leng = 0
	s._udh = ""
	for i in range(0,num):
	 	tu = chr(random.randrange(0,0xff))
		tul = random.randrange(1,132)
		if s._udh_leng + tul > 138:
		 	break
		tud = SMSFuzzData.getSMSFuzzData()
		s._udh = s._udh + tu + chr(tul) + tud[:tul]
		s._udh_leng = len(s._udh)
		if s._udh_leng > 138:
			break
		s._msg_leng = 139 - s._udh_leng
		if s._msg_leng > 0:
			s._msg_leng = random.randrange(int(s._msg_leng / 2), s._msg_leng)
		if s._msg_leng > 0:
			tud = SMSFuzzData.getSMSFuzzData()
			s._msg = tud[:s._msg_leng]
		else:
			s._msg_leng = 0

		s.encode()
		return s._pdu
if __name__ == "__main__":
	out = []
	for i in range(0, int(sys.argv[1])):
		ts = Utils.hex2bin("99309251619580", 0)
		rnd = random.randrange(1,10)
		msg = udhrandfuzz("4917787654321", "49177123456", ts, rnd)
		line = Utils.bin2hex(msg, 1)
		leng = (len(line) / 2) - 8
		out.append((line, leng))
	fuzzutils.cases2file(out, sys.argv[2])