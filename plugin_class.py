from paramiko import SSHClient, WarningPolicy, SSHException
from scp import SCPClient
from enum import IntEnum
from plugin_class_errors import *

class NWConnType(IntEnum):
	Telnet = 1
	SSH = 2
	RS232 = 3


class NetWeaverPlugin:

	def _ssh_request(self):
		"""Make an ssh request and parse returncode"""

	def _build_ssh_client(self, hostname=None, accept_untrusted=False, username=None, password=None, port=22):
		"""Returns a paramiko ssh client object"""
		ssh = SSHClient()
		ssh.load_system_host_keys()
		ssh.set_missing_host_key_policy(WarningPolicy)
		ssh.connect(hostname=hostname, port=port, username=username, password=password)
		return ssh

	def _ssh_command(self, command):
		stdin, stdout, stderr = self.ssh.exec_command(command)
		if stderr.read():
			raise SSHCommandError(stderr.read()) #TODO For some reason this line returns empty on error when run from a child instance
		return stdout.read().decode('utf-8')