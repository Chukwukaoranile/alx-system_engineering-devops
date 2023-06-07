# Script to find out why Apache is not returning error 500 and fixing it

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
