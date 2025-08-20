#!/bin/bash

set -e

APP_NAME="mermaid-flask-ai"
APP_DIR="/opt/$APP_NAME"
SERVICE_NAME="$APP_NAME"
USER="mermaid"

echo "========================================="
echo "  Installation Mermaid Flask AI"
echo "========================================="

# Vérifier les privilèges root
if [[ $EUID -ne 0 ]]; then
   echo "Ce script doit être exécuté en tant que root (sudo)" 
   exit 1
fi

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "Python 3 n'est pas installé. Installation..."
    apt update
    apt install -y python3 python3-pip python3-venv
fi

# Créer l'utilisateur système
if ! id "$USER" &>/dev/null; then
    echo "Création de l'utilisateur système $USER..."
    useradd --system --home $APP_DIR --shell /bin/false $USER
fi

# Créer le répertoire de l'application
echo "Création du répertoire $APP_DIR..."
mkdir -p $APP_DIR
chown $USER:$USER $APP_DIR

# Copier les fichiers de l'application
echo "Copie des fichiers de l'application..."
cp -r . $APP_DIR/
chown -R $USER:$USER $APP_DIR

# Créer l'environnement virtuel
echo "Création de l'environnement virtuel..."
cd $APP_DIR
sudo -u $USER python3 -m venv venv
sudo -u $USER ./venv/bin/pip install --upgrade pip
sudo -u $USER ./venv/bin/pip install -r requirements.txt

# Créer le fichier .env s'il n'existe pas
if [ ! -f "$APP_DIR/.env" ]; then
    echo "Création du fichier .env..."
    sudo -u $USER cp .env.example .env
fi

# Installer le service systemd
echo "Installation du service systemd..."
cat > /etc/systemd/system/$SERVICE_NAME.service << EOF
[Unit]
Description=Mermaid Flask AI
After=network.target

[Service]
Type=simple
User=$USER
Group=$USER
WorkingDirectory=$APP_DIR
Environment=PATH=$APP_DIR/venv/bin
ExecStart=$APP_DIR/venv/bin/python app.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Recharger systemd et activer le service
systemctl daemon-reload
systemctl enable $SERVICE_NAME

echo "========================================="
echo "  Installation terminée!"
echo "========================================="
echo
echo "Pour démarrer le service:"
echo "  sudo systemctl start $SERVICE_NAME"
echo
echo "Pour voir le status:"
echo "  sudo systemctl status $SERVICE_NAME"
echo
echo "Pour voir les logs:"
echo "  sudo journalctl -f -u $SERVICE_NAME"
echo
echo "Configuration:"
echo "  Editez $APP_DIR/.env pour configurer les clés API"
echo
echo "Interface web (par défaut):"
echo "  http://127.0.0.1:5173"