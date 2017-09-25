# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Salt plugin."""

from oslo_log import log

from ironic_inspector.plugins import base
import json

LOG = log.getLogger('ironic_inspector.plugins.salt')

from subprocess import call

class SaltProcessingHook(base.ProcessingHook):  # pragma: no cover
    def before_processing(self, introspection_data, **kwargs):
        LOG.debug('before_processing: %s', introspection_data)
        discovery_data={"discovery": introspection_data}
        LOG.debug(discovery_data)
        call(["sudo", "salt-call", "event.send", "ironic/discovery", json.dumps(discovery_data)])
        LOG.debug('done')

    def before_update(self, introspection_data, node_info, **kwargs):
        LOG.debug('before_update: %s (node %s)', introspection_data,
                  node_info.uuid)


def salt_not_found_hook(introspection_data, **kwargs):
    LOG.debug('Processing node not found %s', introspection_data)


class SaltRuleAction(base.RuleActionPlugin):  # pragma: no cover
    def apply(self, node_info, params, **kwargs):
        LOG.debug('apply action to %s: %s', node_info.uuid, params)

def main():
  pass
  data_data={'macs': [u'aa:bb:cc:dd:01:00'], u'root_disk': {u'rotational': True, u'vendor': u'0x1af4', u'name': u'/dev/vda', u'hctl': None, u'wwn_vendor_extension': None, u'wwn_with_extension': None, u'model': u'', u'wwn': None, u'serial': None, u'size': 10737418240}, 'all_interfaces': {u'eth0': {'ip': u'192.168.100.100', 'mac': u'aa:bb:cc:dd:01:00', 'client_id': None}}, u'boot_interface': u'01-aa-bb-cc-dd-01-00', u'ipmi_address': u'', u'inventory': {u'bmc_address': u'', u'interfaces': [{u'lldp': None, u'product': u'0x0001', u'vendor': u'0x1af4', u'name': u'eth0', u'has_carrier': True, u'ipv4_address': u'192.168.100.100', u'client_id': None, u'mac_address': u'aa:bb:cc:dd:01:00'}], u'disks': [{u'rotational': True, u'vendor': u'0x1af4', u'name': u'/dev/vda', u'hctl': None, u'wwn_vendor_extension': None, u'wwn_with_extension': None, u'model': u'', u'wwn': None, u'serial': None, u'size': 10737418240}], u'boot': {u'current_boot_mode': u'bios', u'pxe_interface': u'01-aa-bb-cc-dd-01-00'}, u'system_vendor': {u'serial_number': u'Not Specified', u'product_name': u'Bochs', u'manufacturer': u'Bochs'}, u'memory': {u'physical_mb': 1024, u'total': 1048297472}, u'cpu': {u'count': 2, u'frequency': u'2394.488', u'flags': [u'fpu', u'de', u'pse', u'tsc', u'msr', u'pae', u'mce', u'cx8', u'apic', u'sep', u'mtrr', u'pge', u'mca', u'cmov', u'pat', u'pse36', u'clflush', u'mmx', u'fxsr', u'sse', u'sse2', u'syscall', u'nx', u'lm', u'nopl', u'pni', u'cx16', u'popcnt', u'hypervisor', u'lahf_lm', u'svm', u'abm', u'sse4a', u'3dnowprefetch', u'vmmcall'], u'model_name': u'QEMU Virtual CPU version 1.0', u'architecture': u'x86_64'}}, u'error': None, 'interfaces': {u'eth0': {'ip': u'192.168.100.100', 'mac': u'aa:bb:cc:dd:01:00', 'client_id': None}}}

  test_data={"discovery": data_data}
  discovery_data="{discovery: sss"+"}"
  call(["sudo", "salt-call", "event.send", "ironic/discovery", json.dumps(test_data)])
  


if __name__ == '__main__':
  main()


