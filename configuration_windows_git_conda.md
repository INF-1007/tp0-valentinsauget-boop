### Procédure additionnelle pour Windows : Ajouter `git` et `conda` aux variables d'environnement

Si vous utilisez un ordinateur Windows, il est possible qu'après l'installation, les commandes `git` et `conda` ne soient pas reconnues dans le terminal PowerShell de VS Code.

Pour régler ce problème, vous pouvez suivre la procédure suivante pour ajouter `git` et `Anaconda` à vos variables d'environnement sur votre ordinateur. 

### ÉTAPE 1. Ouvrir les paramètres de configuration des variables d'environnement:

<img height="500" alt="image" src="https://github.com/user-attachments/assets/09020edd-ae4d-45c5-a6a7-2e7fe01e4461" />


### ÉTAPE 2. Cliquez sur "environment variables"

<img height="500" alt="Image" src="https://github.com/user-attachments/assets/77994a45-af30-4485-b914-bd45894bc16a" />


### ÉTAPE 3. Dans "System variables", trouvez la variable "Path" et cliquez sur "Edit"

<img height="500" alt="Image" src="https://github.com/user-attachments/assets/f4549f9c-94d1-453d-91e0-089d33a325dc" />

### ÉTAPE 4. Ajoutez les chemins suivants (cliquez sur "New" pour ajouter)

**Pour git:**
-  C:\Program Files\Git\cmd

**Pour Anaconda:**
-  C:\Users\TON_NOM_UTILISATEUR\anaconda3\Scripts
-  C:\Users\TON_NOM_UTILISATEUR\anaconda3

*(Remplace "TON_NOM_UTILISATEUR" par le nom de ton compte Windows)*


### ÉTAPE 5.  Cliquez sur "OK" et redémarrez votre ordinateur

Une fois votre ordinateur redémarré, vous devriez pouvoir utiliser les commandes `git` et `conda` sur votre terminal dans VS Code. 
