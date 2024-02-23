# killing proc

exec { 'pkill_killmenow':
  command  => 'pkill killmenow',
  provider => shell,
}
