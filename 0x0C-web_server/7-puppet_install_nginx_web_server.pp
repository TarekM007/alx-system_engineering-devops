# Script to install nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me google.com permanent;/" /etc/nginx/sites-enabled/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
