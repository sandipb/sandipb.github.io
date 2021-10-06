# Linux / Ubuntu Notes and Runbooks

I have been primarily using Ubuntu in my personal systems and RHEL at my work. These

## Linux

## Ubuntu

### Restore original config files for a package

When I have mucked up the config file for a package and need to restore it to its pristine self.

```shell-session
$ sudo apt-get --reinstall -o Dpkg::Options::="--force-confask" install rsyslog
...
Preparing to unpack .../rsyslog_8.2001.0-1ubuntu1.1_amd64.deb ...
Unpacking rsyslog (8.2001.0-1ubuntu1.1) over (8.2001.0-1ubuntu1.1) ...
Setting up rsyslog (8.2001.0-1ubuntu1.1) ...

Configuration file '/etc/rsyslog.conf'
 ==> Modified (by you or by a script) since installation.
     Version in package is the same as at last installation.
   What would you like to do about it ?  Your options are:
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
      D     : show the differences between the versions
      Z     : start a shell to examine the situation
 The default action is to keep your current version.
*** rsyslog.conf (Y/I/N/O/D/Z) [default=N] ? y
Installing new version of config file /etc/rsyslog.conf ...
...
```
