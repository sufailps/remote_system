import paramiko
import time

def connect(hostname, port, username, password):
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("Connecting.............")
	ssh_client.connect(hostname=hostname, port=port,username=username, password=password)
	return ssh_client

def get_shell(ssh_client):
	shell = ssh_client.invoke_shell()
	return shell

def send_cmd(shell,cmd):
	print(f"Sending...{cmd}")
	shell.send(cmd+"\n")
	time.sleep(1)

def show(shell):
	output = shell.recv(10000)
	return output.decode()

def close(ssh_client):
	if ssh_client.get_transport().is_active() == True:
		print("Disconnecting.............")
		ssh_client.close()


if __name__ == "__main__":
	client=connect("127.0.0.1",22,"superuser","root")
	shell=get_shell(client)

	send_cmd(shell,"ls")
	send_cmd(shell,"df")
	send_cmd(shell,"free")
	send_cmd(shell,"w")
	send_cmd(shell,"uptime")
	send_cmd(shell,"rout -n")
	send_cmd(shell)
	output = show(shell)
	print(output)

