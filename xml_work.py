#!/usr/bin/python

import sys, getopt
import xml.etree.ElementTree as elementTree

# print(sys.argv)

opts, args = getopt.getopt(sys.argv[1:], 'f:x:g:p:h', ['file=', 'xmlText=', 'groupName=', 'pattern=', 'help'])

# print(opts)
# print(args)

help_ = False

# filename = 'config_2.xml'
# xmlText = '<role name="2iS_Dev_Builder" pattern="2iS/DEV.*"><permissions><permission>hudson.model.Item.Read</permission><permission>hudson.model.Item.Build</permission></permissions><assignedSIDs><sid>EKB33-DRP_DevOps_Developer_2is_dev</sid><sid>Ekb-devops_Jenkins</sid></assignedSIDs></role>'

for option, value in opts:
    if option in ('-f', '--file'):
        filename = value
    elif option in ('-x', '--xmlText'):
        xmlText = value
    elif option in ('-g', '--groupName'):
        groupname = value
    elif option in ('-p', '--pattern'):
        pattern = value
    elif option in ('-h', '--help'):
        help_ = True

if help_ or 'filename' not in locals() or ('xmlText' not in locals() and 'groupName' not in locals()):
    print("""use 
    python xml_work.py --file=config.xml --groupName=itsk-admins_reader --pattern='itsk-admins.*'
or 
    python xml_work.py --file=config.xml --xmlText='<xmltext>' """)
    exit()

addingElement = elementTree.fromstring(xmlText)

tree = elementTree.parse(filename)
root = tree.getroot()
roleMap_projectRoles = root.findall('./authorizationStrategy/roleMap[@type="projectRoles"]')[0]
roleMap_projectRoles.append(addingElement)

# or addingSubelement()

tree.write(open(filename, 'w'), encoding='unicode')

# if use args for example
def addingSubelement():
    
    role = elementTree.SubElement(roleMap_projectRoles, 'role', attrib={"name": groupName, "pattern": pattern})
    permissions = elementTree.SubElement(role, 'permissions')
    permission = elementTree.SubElement(permissions, 'permission')
    permission.text = 'hudson.model.Item.Read'
    assignedSIDs = elementTree.SubElement(role, 'assignedSIDs')
    sid = elementTree.SubElement(assignedSIDs, 'sid')
    sid.text = 'EKB33-DRP_DevOps_BusinessTester_ASPB'
