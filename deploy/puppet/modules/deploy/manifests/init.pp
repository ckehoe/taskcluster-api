# Puppet script to test and deploy the taskcluster-api to a linux server
# Tested on Ubuntu 14.04 but should work on most version of linux
class deploy {

    $pip_packages = ['nose', 'paste', 'web.py', 'requests']

    package { 'git':
        ensure => 'present',
        before => Exec['install_application'],
    }

    package { 'python':,
        ensure => 'present',
        before => Package['python-pip'],
    }

    package { 'python-pip': 
        ensure   => 'present',
        before   => Package[$pip_packages],
    }

    package { $pip_packages: 
        ensure   => 'present',
        provider => 'pip',
        before   => Exec['run_application'],
    }

    exec { 'install_application': 
        command   => 'git clone https://github.com/ckehoe/taskcluster-api.git /var/lib/taskcluster-api',
        path      => '/usr/bin',
        logoutput => 'on_failure',
        before    => Exec['run_application'],
        creates   => '/var/lib/taskcluster-api',
    }

    exec { 'run_application': 
        command   => 'nohup python /var/lib/taskcluster-api/api.py 80 &',
        path      => '/usr/bin',
        logoutput => 'on_failure',
    }
}
