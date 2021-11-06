sudo apt update
# sudo apt upgrade -y

#安装python
sudo apt install python3 -y
#安装python库
pip install jupyter
pip install music21

#安装与配置musescore
sudo apt install musescore3 -y
python3 setup.py

#安装vscode插件
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter