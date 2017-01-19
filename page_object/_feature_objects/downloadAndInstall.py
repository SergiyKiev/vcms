
import subprocess
import os
import wgetter

# This method works only if PyCharm is running with the admin cridentials (run PyCharm as administrator)

file_name = wgetter.download('https://testteamtest.cloudmanagementsuite.com/WebService/api/v1/Downloads/vRepSetup.msi',
                             outdir='C:\\')
# os.system('msiexec /i %s /qn' % 'D:\\vRepSetup-testteamdev.msi')
p = subprocess.call('msiexec /i %s /qn' % ('C:\\vRepSetup-testteamdev.msi'), shell=True)
print p
# subprocess.call('msiexec /i %s TRANSFORMS=%s /qn' % ('D:\\python\\vcms\\vcms\\page_object\\vRepSetup-testteamdev.msi',
#                                                      '%CD%\EXTRACT'), shell=True)
# os.system('msiexec /i %s TRANSFORMS=%s /qn' % ('E:\\python\\vcms\\vcms\\page_object\\vRepSetup-testteamdev.msi',
#                                                                                           'C:\\Program Files (x86)'))
