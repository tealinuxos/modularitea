#! /bin/bash

# get directory where package located
package_dir="$(dirname $0)"

# rename folder to distinguish regular firefox and developer edition
sudo mv /opt/firefox /opt/firefox_dev

# install shortcut to firefox developer edition
sudo cp $package_dir/firefox-developer-edition.desktop /usr/share/applications
sudo chmod 755 /usr/share/applications/firefox-developer-edition.desktop

# change firefox deveoper edition as default browser
sudo update-alternatives --install /usr/bin/x-www-browser x-www-browser /opt/firefox_dev/firefox 99
sudo update-alternatives --set x-www-browser /opt/firefox_dev/firefox

sudo update-alternatives --install /usr/bin/gnome-www-browser gnome-www-browser /opt/firefox_dev/firefox 99
sudo update-alternatives --set gnome-www-browser /opt/firefox_dev/firefox
