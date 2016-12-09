# Linux 常用命令
## ps 指令
> ps -ef | grep -v grep | grep name | awk '{print("PID: " "[" $2 "] ", "Command: " "[" $9 "]" )}' | cat
> name 为要查找的关键词