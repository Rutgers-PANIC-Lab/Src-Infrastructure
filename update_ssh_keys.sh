echo "Removing old key"
ssh-keygen -R $1
echo "Adding new key"
ssh-keyscan -t ssh-ed25519 $1 >> ~/.ssh/known_hosts
