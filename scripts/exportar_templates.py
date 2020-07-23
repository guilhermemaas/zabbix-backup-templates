from pyzabbix import ZabbixAPI
from dicttoxml import dicttoxml
import sys

zapi = ZabbixAPI("http://localhost/api_jsonrpc.php")
#http://localhost/zabbix.php?
#http://localhost/api_jsonrpc.php
zapi.login("Admin", "zabbix")
print("Connected to Zabbix API Version %s" % zapi.api_version())

"""
for h in zapi.template.get(output="extend", query='selectGroups'):
    file_name = h['host']
    print(h['host'])
    xml = dicttoxml(h, custom_root='teste', attr_type=False)
    with open(f'..\\templates\\{file_name}.xml', 'ab') as out:
        out.write(xml)
    break
"""
export_options = {
    'templates': ['10265']
}

template_10265 = zapi.configuration.export(format="json", options=export_options)
print(template_10265)

"""
for t in zapi.configuration.export(format="xml", options=export_options):
    print(t)
    #file_name = h['xml']
    #print(h['host'])
    file_name = 'template_xml'
    #xml = dicttoxml(t, custom_root='teste', attr_type=False)
    #with open(f'..\\templates\\{file_name}.xml', 'ab') as out:
    #    out.write(xml)
    with open(f'..\\templates\\{file_name}.xml', 'rb') as out:
        out.write(t)
    break
"""