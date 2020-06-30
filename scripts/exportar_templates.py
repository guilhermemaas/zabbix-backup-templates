from pyzabbix import ZabbixAPI
from dicttoxml import dicttoxml
import sys

zapi = ZabbixAPI("http://localhost/")
#http://localhost/zabbix.php?
#http://localhost/api_jsonrpc.php
zapi.login("gmaas", "gmaas")
print("Connected to Zabbix API Version %s" % zapi.api_version())

for h in zapi.template.get(output="extend", query='selectGroups'):
    file_name = h['host']
    print(h['host'])
    xml = dicttoxml(h, custom_root='teste', attr_type=False)
    with open(f'..\\templates\\{file_name}.xml', 'ab') as out:
        out.write(xml)

