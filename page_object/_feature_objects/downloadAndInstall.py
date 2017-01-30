
import subprocess
from subprocess import Popen, PIPE
import os
import wgetter

# cmd = 'ping google.com -c 3'
# PIPE = subprocess.PIPE
# p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
#         stderr=subprocess.STDOUT, close_fds=True)
# while True:
#     s = p.stdout.readline()
#     if not s: break
#     print s,
# x = subprocess.Popen(['runas', '/user:VKYV\igork', '','C:\\Users\\igork.VKYV\\Desktop\\verismicCleanUp.cmd'], shell = True)
# print x
# cmd = 'msiexec /i %s /qb' %'D:\\ResponderSetup-testteamtest.msi'
cmd = 'msiexec /i C:\\vRepSetup-testteamtest.msi /qn'
# p = subprocess.call(['runas', '/user:VKYV\igork', '', cmd], shell = True)
p = subprocess.Popen(['runas', '/user:VKYV\igork', '', cmd], shell=True)
print p
p.poll()
p.wait()

# This method works only if PyCharm is running with the admin cridentials (run PyCharm as administrator)
# file_name = wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/vRepSetup.msi', outdir='D:\\')
# file_name = wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/ResponderSetup.msi', outdir='C:\\')
# os.system('msiexec /i %s /qn' % 'C:\\vRepSetup-testteamtest.msi')
# os.system('msiexec /i %s /qn' % 'C:\\vRepSetup-testteamtest.msi')
# x= os.system('Notepad.exe')
# print x
# p = subprocess.call('msiexec /i %s /qn' % ('C:\\vRepSetup-testteamdev.msi'), shell=True)
#run as administrator
# x = subprocess.Popen(['msiexec /i %s /qn' % 'C:\\vRepSetup-testteamtest.msi'], shell = True)
# x.poll()
# x.wait()
# z = subprocess.call(['runas', '/user:igork.VKYV', '','D:\\ResponderSetup-testteamtest.msi'])
# c = subprocess.Popen('runas / user:igork.VKYV' 'cmd.exe')
# y = subprocess.call(['runas/user:VKYV\igork', '','msiexec /i %s /qn' % 'D:\\vRepSetup-testteamtest.msi'], shell = True)
# x = subprocess.call(['runas', '/user:Administrator', 'ADMIN_PASS','vRepSetup-testteamdev.msi'])
# print "X is:", x
