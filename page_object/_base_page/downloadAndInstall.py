# run PyCharm as administrator

import subprocess
from subprocess import Popen, PIPE
import os
import wgetter
import time
from _base_page.base_actions import BaseActions


# # x = subprocess.Popen(['D:\\verismicCleanUp.cmd']) #work
# clean_up = subprocess.Popen(['C:\\VCMS\\verismicCleanUp.cmd']) #home
# # print clean_up
# time.sleep(120)
# download_agent = \
#     wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/vRepSetup.msi', outdir='C:\\VCMS')
# print download_agent
# time.sleep(20)
# install_agent = os.system('msiexec /i %s /qn' % 'C:\\VCMS\\vRepSetup-testteamtest.msi')
# print install_agent
# time.sleep(60)

class DownloadAndInstall(BaseActions):
# x = subprocess.Popen(['D:\\verismicCleanUp.cmd']) #work
    def clean_up_device(self):
        subprocess.Popen(['C:\\VCMS\\verismicCleanUp.cmd'], shell = True) #home
        # subprocess.Popen(['runas', '/user:VKYV\igork', 'C:\\VCMS\\verismicCleanUp.cmd'], shell=True)  # home
        time.sleep(120)
        print "Clean_up is finished"

    def download_agent(self):
        installer = wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/vRepSetup.msi', outdir='C:\\VCMS')
        # wgetter.download(str(url), outdir='C:\\VCMS')
        print "Installer is downloaded", installer
        time.sleep(10)

    def install_agent(self):
        # os.system('msiexec /i %s /qn' % 'C:\\VCMS\\vRepSetup-testteamtest.msi')
        install = os.system('msiexec /i %s /qn' % 'C:\\VCMS\\vRepSetup-testteamtest.msi')
        time.sleep(60)
        print "Installation is finished", install
#








# class DownloadAndInstall:
#
#     def clean_up_agent_on_device(self):
#         x = subprocess.Popen(['D:\\verismicCleanUp.cmd'])
#         print x
#         time.sleep(60)
#
#     def download_installer(self, filename = None, path = None):
#         # This method works only if PyCharm is running with the admin cridentials (run PyCharm as administrator)
#         file_name = wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/vRepSetup.msi', outdir='D:\\')
#
#     def install_package(self):
#         os.system('msiexec /i %s /qn' % 'C:\\vRepSetup-testteamtest.msi')


# cmd = 'msiexec /i C:\\vRepSetup-testteamtest.msi /qn'
# p = subprocess.Popen(['runas', '/user:VKYV\igork', '', cmd], shell=True)
# print p
# p.poll()
# p.wait()
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
# p = subprocess.call(['runas', '/user:VKYV\igork', '', cmd], shell = True)
# file_name = wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/ResponderSetup.msi', outdir='C:\\')

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
