from netmiko import ConnectHandler

iosv_l2 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'arjun',
    'password': 'cisco'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int br')
print output


config_commands = ['int loop 0' , 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output

for i in range(101,110):
    print "Creating VLAN" + str(i)
    config_commands = ['vlan ' + str(i),'name Python_Vlan '  + str(i)]
    output = net_connect.send_config_set(config_commands)
    print output



from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.75',
    'username':'arjun',
    'password':'cisco'
}

iosv_l2_s2 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.76',
    'username':'arjun',
    'password':'cisco'
}


iosv_l2_s3 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.77',
    'username':'arjun',
    'password':'cisco'
}

iosv_l2_s4 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.78',
    'username':'arjun',
    'password':'cisco'
}


all_devices = [iosv_l2_s1,iosv_l2_s2,iosv_l2_s3,iosv_l2_s4]

for i in all_devices:
    net_connect = ConnectHandler(**i)
    for j in range(110,121):
        print "Creating Vlan" + str(j)
        config_commands = ['vlan ' + str(j), 'name Python_Vlan ' + str(j)]
        output = net_connect.send_config_set(config_commands)
        print output
