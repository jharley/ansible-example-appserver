An example appserver role
=========================

This Ansible role is intended to represent a trivial web application server

The role is tested by [Molecule](https://molecule.readthedocs.io/en/latest/) and [TestInfra](http://testinfra.readthedocs.io/en/latest/index.html).

Requirements
------------

 * Ansible 2.4


Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: all
      roles:
         - { role: ansible-example-appserver }
```

License
-------

Apache License 2.0

Author Information
------------------

Jason Harley - jharley@redmind.ca
