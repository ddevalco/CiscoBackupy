
#!/usr/bin/env python

import paramiko
import time
import sys
import traceback
from conf.configurations import cisco_username, cisco_password, ip_list

#paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)


def export_show_run(ip):
    #connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=cisco_username, password=cisco_password, allow_agent=False, look_for_keys=False)

    #Interactive shell
    print "In user EXEC mode - " + ip
    remote_conn = ssh.invoke_shell()
    remote_conn.send("enable\n")
    time.sleep(1)
    remote_conn.send(cisco_password + "\n")
    time.sleep(1)
    output = remote_conn.recv(5000)
    if "#" in output:
        print "In privileged EXEC mode"
    else:
        remote_conn.close()
        raise Exception("Error - Could not login to Privileged Exec mode\n" + output)

    #Check if User already exists
    remote_conn.send("terminal length 0\n")
    remote_conn.send("show run\n")
    time.sleep(1)
    output = remote_conn.recv(50000)
    print "closing connection"
    remote_conn.send("terminal length 0\n")
    remote_conn.close()
    return output


def main():
    usage = "usage: [--backup-path path]"
    args = sys.argv[2:]
    if not args:
        print usage
        sys.exit(1)
    backup_path = str(args[0] + '/')
    for ip in ip_list:
        try:
            output = export_show_run(ip)
            if output:
                with open(backup_path + 'backup-' + ip + ".txt", 'a+') as f:
                    f.write(output)
        except:
            print traceback.print_exc()


if __name__ == "__main__":
    main()
