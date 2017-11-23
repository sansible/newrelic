# newrelic

Master: [![Build Status](https://travis-ci.org/sansible/newrelic.svg?branch=master)](https://travis-ci.org/sansible/newrelic)  
Develop: [![Build Status](https://travis-ci.org/sansible/newrelic.svg?branch=develop)](https://travis-ci.org/sansible/newrelic)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role installs Newrelic integrations, currently sysmond and php integrations
are available.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install run `ansible-galaxy install sansible.newrelic` or add this to your
`roles.yml`.

```YAML
- name: sansible.newrelic
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses tags: **build** and **configure**

* `build` - Installs New Relic packages and integrations
* `configure` - Configures New Relic, requires a valid license key




## Integrations

See the [Examples](#examples) section for details on how to setup these
integrations.

### PHP

Installs New Relic's PHP integration and configures an INI file with symlinks
to this file to enable it. Comes with default settings that setup license key,
log levels, app name and extension location.

### Sysmond

Installs New Relic's system metrics integration and configures an INI file with
settings. Comes with default settings that setup license key, log levels and
instance labels.

By default the service for this integration is not enabled on boot, this is so
you can start the service once an instance has finished booting. The intention
here is to prevent false alerts triggered by the high saturation encountered
during OS boot.




## Examples

Enable New Relic sysmond integration:

```YAML
- name: Install and configure newrelic
  hosts: "somehost"

  roles:
    - role: sansible.newrelic
      sansible_newrelic:
        integrations:
          sysmond:
            enabled: true
            ini_config:
              - option: /var/log/newrelic/nrsysmond.log
                value: logfile
            start_on_boot: yes
        labels: "org:sansible,role:some_role"
        license_key: 1234567891234567891234567891234567891234
```

Enable PHP7 integration:

```YAML
- name: Install and configure newrelic
  hosts: "somehost"

  roles:
    - role: sansible.newrelic
      sansible_newrelic:
        license_key: 1234567891234567891234567891234567891234
        integrations:
          php:
            enabled: true
```

Enable PHP5 integration:

```YAML
- name: Install and configure newrelic
  hosts: "somehost"

  roles:
    - role: sansible.newrelic
      sansible_newrelic:
        license_key: 1234567891234567891234567891234567891234
        integrations:
          php:
            enabled: true
            ini_paths:
              base: /etc/php/5.0/mods-available/newrelic.ini
              links:
                - /etc/php/5.0/fpm/conf.d/newrelic.ini
                - /etc/php/5.0/cli/conf.d/newrelic.ini
```
