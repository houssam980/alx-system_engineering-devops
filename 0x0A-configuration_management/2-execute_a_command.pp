# killing process

exec { 'pkill':
  command => 'pkill killmenow',
  provider => 'shell',
}
