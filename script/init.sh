iptables -t nat -I PREROUTING -p tcp --dport 10000:12000 -j REDIRECT --to-ports 8000
iptables -t nat -I OUTPUT -p tcp -o lo --dport 10000:12000 -j REDIRECT --to-ports 8000