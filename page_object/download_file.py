import wget
import subprocess
import os


file_url = 'https://testteamdev.cloudmanagementsuite.com/WebService/api/v1/Downloads/vRepSetup.msi'
file_name = wget.download(file_url)
# os.system('msiexec /i %s /qn' % 'E:\\python\\vcms\\vcms\\page_object\\vRepSetup-testteamdev.msi')
# subprocess.call('msiexec /i %s TRANSFORMS=%s /qn' % ('E:\\python\\vcms\\vcms\\page_object\\vRepSetup-testteamdev.msi', 'C:\\Program Files'), shell=True)
subprocess.call('msiexec /i %s TRANSFORMS=%s /qn' % ('E:\\python\\vcms\\vcms\\page_object\\vRepSetup-testteamdev.msi',
                                                     'C:\\Program Files (x86)'), shell=True)
# os.system('msiexec /i %s TRANSFORMS=%s /qn' % ('E:\\python\\vcms\\vcms\\page_object\\vRepSetup-testteamdev.msi', 'C:\\Program Files (x86)'))

