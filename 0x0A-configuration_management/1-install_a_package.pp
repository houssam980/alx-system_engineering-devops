# installing flask using pip

exec { 'flask-installing':
  command    => '/usr/bin/pip3 -y install Flask -v 2.1.0',
}
