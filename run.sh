sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 install fake_useragent
pip3 install googletrans
sudo apt install docker
sudo apt intall snap
sudo snap install docker
sudo snap start docker
sudo docker run -d --restart=always --name tor-socks-proxy -p 127.0.0.1:9150:9150 peterdavehello/tor-socks-proxy:latest
sudo docker start tor-socks-proxy
pip3 install pysocks
