

1. Install this py module

2. Enable salt hook in ironic.conf
processing_hooks = $default_processing_hooks,salt

3. Add discovery salt reactor configuration in /etc/salt/master.d/_reactor.conf:
- ironic/discovery:
  - salt://ironic_inspector/reactor/node_discovery.sls

