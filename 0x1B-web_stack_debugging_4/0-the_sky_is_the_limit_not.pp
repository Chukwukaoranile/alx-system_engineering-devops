# Increasing the amount of traffic an Nginx server can handle.

# Increasing the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restarting Your Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}