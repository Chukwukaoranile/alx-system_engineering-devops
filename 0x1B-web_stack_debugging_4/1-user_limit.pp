# Enable the user alx to login and open files without error.

# Increase hard file limit for alx user.
exec { 'increase-hard-file-limit-for-alx-user':
  command => 'sed -i "/alx hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for alx user.
exec { 'increase-soft-file-limit-for-alx-user':
  command => 'sed -i "alx sot/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
