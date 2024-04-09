#!/bin/bash
echo "back_park_model.service is configured with mysql info ? (1) YES (2) NO: "
read var1
if [ $var1 -eq 1 ]
	then
		sudo apt-get update
		sudo apt-get upgrade
		sudo apt-get install -y mariadb-server
		sudo apt-get install -y npm
		sudo npm install --global yarn
		sudo yarn add vue-chartjs chart.js
		sudo yarn global add @vue/cli
		sudo apt install -y openjdk-17-jdk
		sudo apt install -y maven
		cp back_park_model.service /lib/systemd/system/
		sudo chmod 644 /lib/systemd/system/back_park_model.service
		sudo systemctl daemon-reload
		sudo systemctl enable back_park_model.service
		git clone "https://github.com/vininiciush/back_park_model.git"
		git clone "https://github.com/vininiciush/front_park_model.git"
		cd back_park_model
		mvn clean install -U
		cd ..
		cd front_park_model
		yarn install
	else
		echo "Config file before running install script"
fi
