### python多进程下日志服务

```
python logging 模块是线程安全的， 但是不是进程安全的

这里提供一种python在多进程下的日志服务解决方法

```

####  部署


```
mkdir -p /usr/local/unixLog/

cp etc/unixlog.service /usr/lib/systemd/system/

systemctl enable unixlog.service
systemctl start unixlog.service
systemctl status unixlog.service
```

